# -*- coding: utf-8 -*-

"""
@File: Code05_ReversStackUsingRecursive.py
@Author: Sarah Shen
@Time: 26/10/2022 10:04
"""


def reverse(stack):
    if stack is None or len(stack) == 0:
        return
    i = f(stack)
    reverse(stack)
    stack.append(i)


def f(stack):
    res = stack.pop()
    if len(stack) == 0:
        return res
    else:
        last = f(stack)
        stack.append(res)
        return last


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6]
    reverse(test)
    while len(test) != 0:
        print(test.pop())
