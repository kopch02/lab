import pytest


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


data = list(range(10))
res = []
for i in range(10):
    res.append(fib(i))

res[3] = 100000


@pytest.mark.parametrize("num, output", list(zip(data, res)))
def test_multiplication_11(num, output):
    assert fib(num) == output