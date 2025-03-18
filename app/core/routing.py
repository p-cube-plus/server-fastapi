import traceback
from typing import Any, Callable, Coroutine, Type

from fastapi import APIRouter, Depends, Request, Response
from fastapi.routing import APIRoute

from app.constant.user import UserRole
from app.core.security import JWTAuthenticator
from app.dto.base import BaseDTO, QueryParamsDTO


class CustomAPIRoute(APIRoute):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dependency_modified: bool = False

    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(
            request: Request,
        ) -> Coroutine[Any, Any, Response]:
            if not self.__dependency_modified:
                dependencies = self.dependant.dependencies
                for dependency in dependencies:
                    if isinstance(dependency.call, type) and issubclass(
                        dependency.call, QueryParamsDTO
                    ):
                        dto_cls: Type[BaseDTO] = dependency.call

                        def dependency_call(request: Request):
                            query_params = dict(request.query_params)
                            for field_name, field in query_params.items():
                                dto_field = dto_cls.model_fields[field_name]
                                if field == "" and dto_field.annotation is not str:
                                    query_params[field_name] = None
                            return dto_cls(**query_params)

                        dependency.query_params = []
                        dependency.request_param_name = "request"
                        dependency.call = dependency_call
                        dependency.cache_key = (dependency_call, tuple())

                self.__dependency_modified = True
            return await original_route_handler(request)

        return custom_route_handler


class CustomAPIRouter(APIRouter):
    def __init__(self, *args, route_class: Type[APIRoute] = CustomAPIRoute, **kwargs):
        super().__init__(*args, route_class=route_class, **kwargs)

    def api_route(self, path: str, *args, **kwargs):
        def decorator(func):
            required_role = getattr(func, "required_role", UserRole.NONE)
            dependencies = kwargs.get("dependencies")
            if dependencies is None:
                dependencies = []
            dependencies.append(Depends(JWTAuthenticator(required_role=required_role)))
            kwargs["dependencies"] = dependencies
            self.add_api_route(path, func, *args, **kwargs)
            return func

        return decorator
