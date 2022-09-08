from __future__ import annotations

from ..types import F
from .base import CustomError, CustomValueError

__all__ = [
    'UndefinedMatrixError',
    'UndefinedTransferError',
    'UndefinedPrimariesError',

    'ReservedMatrixError',
    'ReservedTransferError',
    'ReservedPrimariesError',

    'InvalidMatrixError',
    'InvalidTransferError',
    'InvalidPrimariesError',

    'UnsupportedMatrixError',
    'UnsupportedTransferError',
    'UnsupportedPrimariesError',
    'UnsupportedColorRangeError'
]

########################################################
# Matrix


class UndefinedMatrixError(CustomValueError):
    """Raised when an undefined matrix is passed."""


class ReservedMatrixError(PermissionError, CustomError):
    """Raised when a reserved matrix is requested."""


class UnsupportedMatrixError(CustomValueError):
    """Raised when an unsupported matrix is passed."""


class InvalidMatrixError(CustomValueError):
    """Raised when an invalid matrix is passed."""

    def __init__(
        self, function: str | F, matrix: int = 2, message: str = 'You can\'t set a matrix of {matrix}!'
    ) -> None:
        super().__init__(message, function, matrix=matrix)


########################################################
# Transfer

class UndefinedTransferError(CustomValueError):
    """Raised when an undefined transfer is passed."""


class ReservedTransferError(PermissionError, CustomError):
    """Raised when a reserved transfer is requested."""


class UnsupportedTransferError(CustomValueError):
    """Raised when an unsupported transfer is passed."""


class InvalidTransferError(CustomValueError):
    """Raised when an invalid matrix is passed."""

    def __init__(
        self, function: str | F, transfer: int = 2, message: str = 'You can\'t set a transfer of {transfer}!'
    ) -> None:
        super().__init__(message, function, transfer=transfer)


########################################################
# Primaries

class UndefinedPrimariesError(CustomValueError):
    """Raised when an undefined primaries value is passed."""


class ReservedPrimariesError(PermissionError, CustomError):
    """Raised when reserved primaries are requested."""


class UnsupportedPrimariesError(CustomValueError):
    """Raised when a unsupported primaries value is passed."""


class InvalidPrimariesError(CustomValueError):
    """Raised when an invalid matrix is passed."""

    def __init__(
        self, function: str | F, primaries: int = 2, message: str = 'You can\'t set primaries of {primaries}!'
    ) -> None:
        super().__init__(message, function, primaries=primaries)


########################################################
# ColorRange

class UnsupportedColorRangeError(CustomValueError):
    """Raised when a unsupported color range value is passed."""