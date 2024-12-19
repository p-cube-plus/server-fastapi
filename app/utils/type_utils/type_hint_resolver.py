from typing import Any, Callable, TypeVar, get_args, get_origin


def extract_type_vars(type_hint: Any) -> list[TypeVar]:
    if isinstance(type_hint, TypeVar):
        return [type_hint]

    type_vars = []

    for arg in get_args(type_hint):
        type_vars.extend(extract_type_vars(arg))

    return type_vars


def resolve_type_vars(cls: type, method_name: str, type_vars: list[TypeVar]):
    concrete_types = []

    for type_var in type_vars:
        for super_cls_idx, super_cls in enumerate(cls.__mro__):
            if method_name not in super_cls.__dict__:
                continue

            if type_var not in super_cls.__parameters__:
                continue

            concrete_type = type_var

            if super_cls_idx == 0:
                break

            type_var_owner = super_cls
            type_var_index = type_var_owner.__parameters__.index(type_var)

            for sub_cls in cls.__mro__[super_cls_idx - 1 :: -1]:
                for orig_base in sub_cls.__orig_bases__:
                    origin = get_origin(orig_base)

                    if origin is None or not issubclass(origin, type_var_owner):
                        continue

                    type_args = get_args(orig_base)
                    concrete_type = type_args[type_var_index]

                    if not isinstance(concrete_type, TypeVar):
                        type_var_index = -1
                        break

                    for type_arg in get_args(orig_base):
                        if isinstance(type_arg, TypeVar):
                            continue
                        type_var_index -= 1
                if type_var_index == -1:
                    break
            break
        if isinstance(concrete_type, TypeVar):
            concrete_type = concrete_type.__bound__

        concrete_types.append(concrete_type)

    return concrete_types


def construct_concrete_type_hint(type_hint: Any, type_var_map: dict[TypeVar, Any]):
    if isinstance(type_hint, TypeVar):
        return type_var_map[type_hint]

    origin = get_origin(type_hint)
    if origin is None:
        return type_hint

    args = get_args(type_hint)
    if not args:
        return type_hint

    new_args = tuple(construct_concrete_type_hint(arg, type_var_map) for arg in args)

    try:
        return origin[new_args]
    except TypeError:
        return type_hint


def resolve_type_hint(instance: object, method: Callable, type_hint: Any):
    type_vars = extract_type_vars(type_hint)

    if not type_vars:
        return type_hint

    concrete_types = resolve_type_vars(instance.__class__, method.__name__, type_vars)
    type_var_map = dict(zip(type_vars, concrete_types))

    resolved_type_hint = construct_concrete_type_hint(type_hint, type_var_map)

    return resolved_type_hint
