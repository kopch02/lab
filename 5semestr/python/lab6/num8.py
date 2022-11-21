import re
import pytest


def fun(s):
    """возвращает True если адрес корректный,
    иначе возвращает False"""
    p = r"^[a-zA-Z|\d|_|-]+\@[a-zA-Z|\d]+\.[a-zA-Z]{1,3}$"
    if re.search(p, s) == None:
        return False
    return True


def filter_mail(emails):
    return list(sorted(filter(fun, emails)))


def main():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = filter_mail(emails)
    print(filtered_emails)


def t0():
    for i in range(10):
        inp = open(f"test_data\input\input0{i}.txt", "rt")
        inp.read(2)
        out = open(f"test_data\output\output0{i}.txt", "rt")
        #print(str(filter_mail(inp.read().splitlines())))
        #print(out.read())
        assert str(filter_mail(inp.read().splitlines())) == out.read()


def test_0():
    inp = open("test_data\input\input00.txt", "rt")
    inp.read(2)
    out = open("test_data\output\output00.txt", "rt")
    assert str(filter_mail(inp.read().splitlines())) == out.read()


def test_1():
    inp = open("test_data\input\input01.txt", "rt")
    inp.read(2)
    out = open("test_data\output\output01.txt", "rt")
    assert str(filter_mail(inp.read().splitlines())) == out.read()


def test_2():
    inp = open("test_data\input\input02.txt", "rt")
    inp.read(2)
    out = open("test_data\output\output02.txt", "rt")
    assert str(filter_mail(inp.read().splitlines())) == out.read()


def test_3():
    inp = open("test_data\input\input03.txt", "rt")
    inp.read(2)
    out = open("test_data\output\output03.txt", "rt")
    assert str(filter_mail(inp.read().splitlines())) == out.read()


def test_4():
    inp = open("test_data\input\input04.txt", "rt")
    inp.read(2)
    out = open("test_data\output\output04.txt", "rt")
    assert str(filter_mail(inp.read().splitlines())) == out.read()


def test_5():
    inp = open("test_data\input\input05.txt", "rt")
    inp.read(2)
    out = open("test_data\output\output05.txt", "rt")
    assert str(filter_mail(inp.read().splitlines())) == out.read()


def test_6():
    inp = open("test_data\input\input06.txt", "rt")
    inp.read(2)
    out = open("test_data\output\output06.txt", "rt")
    assert str(filter_mail(inp.read().splitlines())) == out.read()


def test_7():
    inp = open("test_data\input\input07.txt", "rt")
    inp.read(2)
    out = open("test_data\output\output07.txt", "rt")
    assert str(filter_mail(inp.read().splitlines())) == out.read()


def test_8():
    inp = open("test_data\input\input08.txt", "rt")
    inp.read(2)
    out = open("test_data\output\output08.txt", "rt")
    assert str(filter_mail(inp.read().splitlines())) == out.read()


def test_9():
    inp = open("test_data\input\input09.txt", "rt")
    inp.read(2)
    out = open("test_data\output\output09.txt", "rt")
    assert str(filter_mail(inp.read().splitlines())) == out.read()


if __name__ == '__main__':
    t0()