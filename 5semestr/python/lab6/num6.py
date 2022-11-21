import pytest
import numpy as np

doska = []
n = range(1,9)
a = ["a","b","c","d","e","f","f","h"]
for i in a:
    for j in n:
        doska.append(i + str(j))

doska = np.array(doska)
doska = doska.reshape((8,8))
print(doska)

def is_under_queen_attack(position, queen_position):
    if type(position) != str: raise TypeError(f'Expected str for position, got {type(position)}')
    if type(queen_position) != str: raise TypeError(f'Expected str for queen_position, got {type(queen_position)}')
    if not (position in doska):raise ValueError('uncorrect position')
    if not (queen_position in doska):raise ValueError('uncorrect queen_position')
    if (position[0] == queen_position[0]) or (position[1] == queen_position[1]) :return True
    pos_i, pos_j = np.where(doska == queen_position)
    if position in np.diag(doska,k = abs(pos_j[0] - pos_i[0])): return True
    return False

is_under_queen_attack("b3", "e6")


def test_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack(None, 42)


def test_wrong_coordinate():
    with pytest.raises(ValueError):
        is_under_queen_attack("abc", "42")


def test_wrong_coordinate2():
    with pytest.raises(ValueError):
        is_under_queen_attack('c3', 'd4d')


def test_wrong_coordinate_out_of_bounds():
    with pytest.raises(ValueError):
        is_under_queen_attack("e1", "e9")


def test_attack_same_field():
    assert is_under_queen_attack("e5", "e5")


def test_attack_same_row():
    assert is_under_queen_attack("a1", "e1")


def test_attack_same_column():
    assert is_under_queen_attack("a1", "a8")


def test_attack_diagonal():
    assert is_under_queen_attack("b3", "e6")


def test_no_attack():
    assert not is_under_queen_attack("c4", "e5")