# -*- coding: utf-8 -*-

"""
@File: Code07_PaperFolding.py
@Author: Sarah Shen
@Time: 21/10/2022 15:50
"""


def print_all_folds(n: int):
    process(1, n, True)
    print()


# 当前你来到了一个节点，脑海中想想
# 这个节点在第i层，一共有n层，n固定不变
# 如果这个节点是凹的话，down = T
# 如果这个节点是凸的话，down = F
# 函数的功能：中序打印以你想想的节点为头的整棵树


def process(i: int, n: int, down: bool):
    if i > n:
        return
    process(i + 1, n, True)
    print("凹" if down else "凸")
    process(i + 1, n, False)


if __name__ == "__main__":
    print_all_folds(3)
