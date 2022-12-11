import random
import pytest
from unittest.mock import Mock
from unittest.mock import patch


def choice_one(cursor):
    res = cursor.execute("select name from product")
    r = random.choice(res)
    return r[0]


def test_wrong_type():
    with pytest.raises(AttributeError):
        choice_one(1)


def test_empty():
    fake_execute = Mock(return_value=[])
    fake_cursor = Mock()
    fake_cursor.execute = fake_execute
    with pytest.raises(IndexError):
        choice_one(fake_cursor)


def test_normal():
    fake_execute = Mock(return_value=["первое","второе","третье"])
    fake_cursor = Mock()
    fake_cursor.execute = fake_execute
    with patch('random.choice', return_value = "первое") as m:
        choice_one(fake_cursor) == "первое"