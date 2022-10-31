# -*- coding: utf-8 -*-

"""
@File: Code03_NQueens.py
@Author: Sarah Shen
@Time: 30/10/2022 13:49
"""


def num(n: int):
    if n < 1:
        return 0
    record = [0] * n
    return process(0, record, n)


def process(i, record: [int], n: int):
    """
    当前来到i行，一共是0~n-1行
    在i行上方皇后，所有列都尝试
    必须要保证跟之前所有的皇后都不冲突
    record[x] = y表示第x行的皇后，放在了y列上
    返回：不关心i以上发生了什么，i,...后续有多少合法的方法数
    """
    if i == n:
        # i已经走到最后一行了，说明之前都没有冲突，返回一种方法
        return 1
    res = 0
    # i行的皇后放哪一列？ j列
    for j in range(n):
        if is_valid(record, i, j):
            record[i] = j
            res += process(i + 1, record, n)
    return res


def is_valid(record: [int], i: int, j: int):
    for k in range(i):
        if j == record[k] or abs(record[k] - j) == abs(i - k):
            return False
    return True


if __name__ == '__main__':
    print(num(1))
    print(num(2))
    print(num(3))
    print(num(4))
