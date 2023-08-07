import strawberry
from strawberry.utils.str_converters import to_camel_case
from typing import Any, Dict

def is_authenticated(next_resolver):
    def wrapper(root, info, *args, **kwargs):
        user = info.context.user
        if user.is_authenticated:
            return next_resolver(root, info, *args, **kwargs)
        else:
            raise ValueError("Authentication required.")

    return wrapper