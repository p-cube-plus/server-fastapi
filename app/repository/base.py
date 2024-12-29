import inspect
from dataclasses import dataclass
from functools import wraps
from types import NoneType, UnionType
from typing import (
    Annotated,
    Any,
    Callable,
    Collection,
    Generic,
    TypeVar,
    Union,
    get_args,
    get_origin,
    get_type_hints,
)

from fastapi import Depends
from sqlalchemy import Result, Row, delete, insert, select, update

from app.database.base import DatabaseSession
from app.database.mysql import MySQLDatabase
from app.dto.base import BaseDTO
from app.entity.base import BaseEntity
from app.utils.type_utils import resolve_type_hint

Entity = TypeVar("Entity", bound=BaseEntity)
DTO = TypeVar("DTO", bound=BaseDTO)


class ResultConverterMeta(type):
    def __convert_atomic_result(result: Result, result_type: Any):
        rows = result.mappings().all()
        origin = get_origin(result_type)

        if origin is list:
            item_type = get_args(result_type)[0]
            if not issubclass(item_type, BaseDTO):
                raise TypeError(
                    f"Expected list items to be of BaseDTO type, but got {item_type}"
                )
            return [item_type(**row) for row in rows]

        if origin is Union:
            args = get_args(result_type)
            if len(args) == 2 and type(None) in args:
                item_type = next(arg for arg in args if arg is not type(None))
                if not issubclass(item_type, BaseDTO):
                    raise TypeError(
                        f"Optional value must be of BaseDTO type, but got {item_type}"
                    )
                if not rows:
                    return None
                return item_type(**rows[0])
            raise TypeError(f"Union types are only supported for Optional[BaseDTO]")

        if origin is None and issubclass(result_type, BaseDTO):
            return result_type(**rows[0])

        raise TypeError(
            f"Unable to convert Result to type {result_type} - expected BaseDTO, list[BaseDTO], or Optional[BaseDTO]"
        )

    def __convert_result(result: Any, result_type: type):
        if isinstance(result, Result):
            return ResultConverterMeta.__convert_atomic_result(result, result_type)

        if isinstance(result, list):
            if not get_origin(result_type) is list:
                raise TypeError(f"Expected {result_type}, but got list")
            item_type = get_args(result_type[0])
            return [
                ResultConverterMeta.__convert_result(item, item_type) for item in result
            ]

        if isinstance(result, dict):
            if not get_origin(result_type) is dict:
                raise TypeError(f"Expected {result_type}, but got dict")
            key_type, value_type = get_args(result_type)
            return {
                ResultConverterMeta.__convert_result(
                    k, key_type
                ): ResultConverterMeta.__convert_result(v, value_type)
                for k, v in result.items()
            }

        return result

    def __result_converter(func: Callable, resolved_type: type):
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            result = await func(self, *args, **kwargs)
            return ResultConverterMeta.__convert_result(result, resolved_type)

        return wrapper

    def __type_resolver(func: Callable, return_hint: Any):
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            resolved_type = resolve_type_hint(self, func, return_hint)
            converted_func = ResultConverterMeta.__result_converter(func, resolved_type)
            setattr(
                self, converted_func.__name__, converted_func.__get__(self, type(self))
            )
            return await converted_func(self, *args, **kwargs)

        return wrapper

    def __new__(mcs, name, bases, attrs, **kwargs):
        for attr_name, attr_value in attrs.items():
            if not inspect.isfunction(attr_value):
                continue

            hints = get_type_hints(attr_value)
            return_hint = hints.get("return")
            if not return_hint:
                continue

            attrs[attr_name] = ResultConverterMeta.__type_resolver(
                attr_value, return_hint
            )

        return super().__new__(mcs, name, bases, attrs, **kwargs)


class RepositoryMeta(ResultConverterMeta):
    pass


@dataclass
class BaseRepository(metaclass=RepositoryMeta):
    session: Annotated[DatabaseSession, Depends()]


class CRUDRepositoryMeta(RepositoryMeta):
    def __new__(mcs, name, bases, attrs, **kwargs):
        cls = super().__new__(mcs, name, bases, attrs, **kwargs)

        for base in cls.__orig_bases__:
            if (
                hasattr(base, "__origin__")
                and base.__origin__.__name__ == "CRUDRepository"
            ):
                entity_type = get_args(base)[0]
                if isinstance(entity_type, TypeVar):
                    raise TypeError(
                        "CRUDRepository requires concrete entity type, not TypeVar"
                    )
                cls._entity_type = entity_type
                break

        return cls


@dataclass
class CRUDRepository(
    BaseRepository,
    Generic[Entity, DTO],
    metaclass=CRUDRepositoryMeta,
):

    async def get(self, **filters) -> list[DTO]:
        stmt = (
            select(*self._entity_type.columns())
            .select_from(self._entity_type)
            .filter_by(**filters)
        )
        return await self.session.execute(stmt)

    async def create(self, dto_list: list[BaseDTO]) -> list[DTO]:
        stmt = insert(self._entity_type).values([dto.dict() for dto in dto_list])

        result = await self.session.execute(stmt)

        stmt = (
            select(*self._entity_type.columns())
            .select_from(self._entity_type)
            .where(self._entity_type.id >= result.lastrowid)
        )

        return await self.session.execute(stmt)

    async def update(self, dto: BaseDTO, *, exclude_unset=True, **filters) -> list[DTO]:
        stmt = (
            update(self._entity_type)
            .filter_by(**filters)
            .values(dto.dict(exclude_unset=exclude_unset))
        )

        await self.session.execute(stmt)

        stmt = select(*self._entity_type.columns()).filter_by(**filters)

        return await self.session.execute(stmt)

    async def delete(self, **filters) -> list[DTO]:
        stmt = select(*self._entity_type.columns()).filter_by(**filters)

        result = await self.session.execute(stmt)

        stmt = delete(self._entity_type).filter_by(**filters)

        await self.session.execute(stmt)

        return result
