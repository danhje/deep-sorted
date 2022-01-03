"""Sorting of nested dicts and lists"""
from typing import TypeVar

T = TypeVar("T")


def _comp(ele):
    # noinspection PyBroadException
    try:
        return 0, int(ele), str(type(ele)), id(ele)
    except BaseException:
        return 1, str(ele), str(type(ele)), id(ele)


def deep_sorted(obj: T) -> T:
    """Sort nested dicts and lists"""
    if isinstance(obj, dict):
        return {k: deep_sorted(v) for k, v in sorted(obj.items(), key=_comp)}
    elif isinstance(obj, (list, tuple)):
        return obj.__class__(sorted((deep_sorted(e) for e in obj), key=_comp))
    else:
        return obj
