from __future__ import annotations

from typing import Any

from ..types import F, SupportsString

__all__ = [
    'CustomError',

    'CustomValueError',
    'CustomKeyError',
    'CustomTypeError'
]


class CustomErrorMeta(type):
    def __new__(cls: type[Self], *args: Any) -> Self:
        obj = type.__new__(cls, *args)

        if sys.stdout.isatty():
            obj.__qualname__ = f'\033[0;31;1m{obj.__qualname__}\033[0m'  # type: ignore

        obj.__module__ = Exception.__module__

        return obj


class CustomError(Exception, metaclass=CustomErrorMeta):
    def __init__(
        self, message: SupportsString | None = None, function: SupportsString | F | None = None, **kwargs: Any
    ) -> None:
        from ..functions import norm_func_name

        if message is None:
            return super().__init__()

        message = str(message)

        formatted = message.format(**kwargs)

        if function:
            func_name = norm_func_name(function)
            func_header = f'({func_name})'

            if sys.stdout.isatty():
                func_header = f'\033[0;36m{func_header}\033[0m'

            func_header += ' '
        else:
            func_header = ''

        super().__init__(func_header + formatted)


class CustomValueError(ValueError, CustomError):
    ...


class CustomKeyError(KeyError, CustomError):
    ...


class CustomTypeError(TypeError, CustomError):
    ...