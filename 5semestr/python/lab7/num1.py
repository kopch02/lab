import pytest


class Rectangle:

    def __init__(self, a, b) -> None:
        if (type(a) != (int or float)) or (type(b) != (int or float)):
            raise TypeError
        if a < 0 or b < 0:
            raise ValueError
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def get_perimetr(self):
        return self.a * 2 + self.b * 2


@pytest.fixture
def app():
    test = Rectangle(10, 20)
    return test


def test_area(app):
    assert app.get_area() == 200


def test_perimetr(app):
    assert app.get_perimetr() == 60
