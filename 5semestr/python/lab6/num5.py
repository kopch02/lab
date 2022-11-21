import pytest


def count_chars(s):
    if type(s) != str: raise TypeError(f'Expected str, got {type(s)}')
    res = dict()
    for i in s:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res


def test_wrong_type():
    with pytest.raises(TypeError):
        count_chars(42)


def test_empty():
    counts = count_chars('')
    assert counts == {}


def test_common():
    counts = count_chars('aabccc')
    assert counts == {'a': 2, 'b': 1, 'c': 3}