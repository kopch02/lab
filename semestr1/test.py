import math
from math import e
import time

# def q() -> int:
#     y:int
#     x1:int
#     x2:int
#     print("x1 = ")
#     x1 = int(input())
#     print("x2 = ")
#     x2 = int(input())
#     y = (math.pow(math.e, -x1) + math.pow(math.e, -x2)) / 2
#     print(f"{y =}")
#     return

# if __name__ == "__main__":
#     q()


def q():
    x1,x2 = int(input()), int(input())
    print(f"y = {((e ** x1) + (e ** x2)) / 2}")

q()