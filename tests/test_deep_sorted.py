import random
from copy import deepcopy
from itertools import permutations
from typing import TypeVar

from deep_sorted import deep_sorted

T = TypeVar("T")
random.seed(42)


def _comp(ele):
    return random.random()


def deep_scrambled(obj: T) -> T:
    """Un-sort nested dicts and lists"""
    if isinstance(obj, dict):
        return {k: deep_scrambled(v) for k, v in sorted(obj.items(), key=_comp)}
    elif isinstance(obj, (list, tuple)):
        return obj.__class__(sorted((deep_scrambled(e) for e in obj), key=_comp))
    else:
        return obj


def test_deep_sorted_shallow_list():
    result = deep_sorted([3, 2, 1])
    assert result == [1, 2, 3]


def test_deep_sorted_shallow_dict():
    result = deep_sorted({3: ..., 2: ..., 1: ...})
    assert result == {1: ..., 2: ..., 3: ...}


def test_deep_sorted_nested_lists():
    result = deep_sorted([[3, 2, 1], [8, 7, 9], [6, 5, 4]])
    assert result == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_deep_sorted_nested_dicts():
    result = deep_sorted(
        {2: {"d": {"e": ..., "f": ...}}, 1: {"b": ..., "c": ..., "a": ...}}
    )
    assert result == {1: {"a": ..., "b": ..., "c": ...}, 2: {"d": {"e": ..., "f": ...}}}


def test_deep_sorted_nested_tuples():
    result = deep_sorted(((3, 2, 1), (7, 8, 9), (4, 5, 6)))
    assert result == ((1, 2, 3), (4, 5, 6), (7, 8, 9))


def test_deep_sorted_list_mixed_type():
    class A:
        pass

    result = deep_sorted([3, "a", A, 2, True, False])
    assert result == [False, True, 2, 3, A, "a"]


def test_deep_sorted_dict_mixed_type():
    class A:
        pass

    result = deep_sorted({"a": ..., 1: ..., False: ..., A: ...})
    assert result == {
        False: ...,
        1: ...,
        A: ...,
        "a": ...,
    }


def test_input_order_is_irrelevant():
    ordered = [deep_sorted(l) for l in permutations([0, False, None, [], {}, ""])]
    assert all(ordered[0] == l for l in ordered[1:])

    class Inty:
        def __init__(self, value, note):
            self.value = value
            self.note = note

        def __int__(self):
            return self.value

    ordered = [deep_sorted(l) for l in permutations([Inty(1, "a"), Inty(1, "b")])]
    assert all(ordered[0] == l for l in ordered[1:])


def test_deep_sorted_reverts_deep_scrambled(ordered_structs):
    for original in ordered_structs:
        ordered = deep_sorted(deep_scrambled(deepcopy(original)))
        assert ordered == original
