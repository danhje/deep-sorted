from deep_sorted import deep_sorted


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
