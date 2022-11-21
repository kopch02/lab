import pytest
import math

def roots(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        dis = float((b**2) - (4 * a * c))
        if dis < 0: raise ValueError
        elif dis == 0:
            x = -b / (2 * a)
            return tuple([x, x])
        else:
            x1 = round((-b - math.sqrt(dis)) / (2 * a),2)
            x2 = round((-b + math.sqrt(dis)) / (2 * a),2)
            return tuple(sorted(list([x1, x2])))
    except (TypeError, ValueError) as e:
        return None

def test_wrong_type():
    assert roots("2", "3", 4) == None


def test_one_solve():
    assert roots(2, 4, 2) == (-1, -1)


def test_double_solve():
    assert roots(3.2, -7.8, 1) == (0.14, 2.3)


def test_no_solve():
    assert roots(8, 4, 2) == None
