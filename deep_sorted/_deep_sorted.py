"""Sorting of nested dicts and lists"""
from typing import TypeVar

T = TypeVar("T")


def deep_sorted(obj: T) -> T:
    """Sort nested dicts and lists"""
    if isinstance(obj, dict):
        return {k: deep_sorted(v) for k, v in sorted(obj.items())}
    elif isinstance(obj, list) or isinstance(obj, tuple):
        return obj.__class__(sorted(deep_sorted(x) for x in obj))
    else:
        return obj
