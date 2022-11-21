import pytest


# Тестируемая функция
def reverse(s):
    if type(s) != str:
        raise TypeError(f'Expected str, got {type(s)}')

    return s[::-1]


def test_empty():
    assert reverse('') == ''


def test_single():
    assert reverse('a') == 'a'


def test_palindrom():
    assert reverse('aba') == 'aba'


def test_normal():
    assert reverse('abc') == 'cba'


def test_wrong_type():
    with pytest.raises(TypeError):
        reverse(42)


def test_wrong_type2():
    with pytest.raises(TypeError):
        reverse(["a", "b", "c"])
