# -*- coding: utf-8 -*-

"""
@File: Code02_Hanoi.py
@Author: Sarah Shen
@Time: 26/10/2022 10:04
"""


# 汉诺塔游戏， 焚天游戏


def hanoi1(n: int):
    left_to_right(n)


def left_to_right(n: int):
    if n == 1:
        print("Move 1 from left to right")
        return
    left_to_mid(n - 1)
    print("Move %i from left to right" % n)
    mid_to_right(n - 1)


def left_to_mid(n: int):
    if n == 1:
        print("Move 1 from left to mid")
        return
    left_to_right(n - 1)
    print("Move %i from left to mid" % n)
    right_to_mid(n - 1)


def mid_to_left(n: int):
    if n == 1:
        print("Move 1 from mid to left")
        return
    mid_to_right(n - 1)
    print("Move %i from mid to left" % n)
    right_to_left(n - 1)


def mid_to_right(n: int):
    if n == 1:
        print("Move 1 from mid to right")
        return
    mid_to_left(n - 1)
    print("Move %i from mid to right" % n)
    left_to_right(n - 1)


def right_to_left(n: int):
    if n == 1:
        print("Move 1 from right to left")
        return
    right_to_mid(n - 1)
    print("Move %i from right to left" % n)
    left_to_mid(n - 1)


def right_to_mid(n: int):
    if n == 1:
        print("Move 1 from right to mid")
        return
    right_to_left(n - 1)
    print("Move %i from right to mid" % n)
    left_to_mid(n - 1)


def hanoi2(n: int):
    if n > 0:
        func(n, "left", "right", "mid")


def func(n: int, f: str, t: str, o: str):
    if n == 1:
        print("Move 1 form %s to %s" % (f, t))
    else:
        func(n - 1, f, o, t)
        print("move %i from %s to %s" % (n, f, t))
        func(n - 1, o, t, f)


if __name__ == '__main__':
    num = 3
    hanoi1(num)
    print("===========")
    hanoi2(num)
