# -*- coding: utf-8 -*-

"""
@File: Code02_CardsInLine.py
@Author: Sarah Shen
@Time: 26/10/2022 10:04
"""


# 题意： 数组表示不重复的正整数纸牌，两人分先手和后手拿纸牌，两人均绝顶聪明，求胜出者的分数
# 方法1：暴力递归
def win1(arr: list):
    if arr is None or len(arr) == 0:
        return 0
    first = f1(arr, 0, len(arr) - 1)
    second = g1(arr, 0, len(arr) - 1)
    return max(first, second)


def f1(arr: list, left: int, right: int):
    """ arr[left,...,right]先手获得最好的分数返回 """
    if left == right:
        return arr[left]
    p1 = arr[left] + g1(arr, left + 1, right)
    p2 = arr[right] + g1(arr, left, right - 1)
    return max(p1, p2)


def g1(arr: list, left: int, right: int):
    """ arr[left,...,right]后手获得最好的分数返回 """
    if left == right:
        return 0
    p1 = f1(arr, left + 1, right)  # 对手拿走了left位置的数，那自己在left+1 ~ right位置上作为先手拿走最好的分数
    p2 = f1(arr, left, right - 1)  # 对手拿走了right位置的数，拿自己在left ~ right -1位置上作为先手拿走最好的分数
    return min(p1, p2)


# 带简单缓存矩阵的递归
def win2(arr: list):
    if arr is None or len(arr) == 0:
        return 0
    n = len(arr)
    fmap = [[-1] * n for i in range(n)]
    gmap = [[-1] * n for i in range(n)]
    first = f2(arr, 0, len(arr) - 1, fmap, gmap)
    second = g2(arr, 0, len(arr) - 1, fmap, gmap)
    return max(first, second)


def f2(arr: list, left: int, right: int, fmap, gmap):
    """ arr[left,...,right]先手获得最好的分数返回 """
    if fmap[left][right] != -1:
        return fmap[left][right]
    if left == right:
        ans = arr[left]
    else:
        p1 = arr[left] + g2(arr, left + 1, right, fmap, gmap)
        p2 = arr[right] + g2(arr, left, right - 1, fmap, gmap)
        ans = max(p1, p2)
    fmap[left][right] = ans
    return ans


def g2(arr: list, left: int, right: int, fmap, gmap):
    """ arr[left,...,right]后手获得最好的分数返回 """
    if gmap[left][right] != -1:
        return gmap[left][right]
    ans = 0
    if left != right:
        p1 = f2(arr, left + 1, right, fmap, gmap)
        p2 = f2(arr, left, right - 1, fmap, gmap)
        ans = min(p1, p2)
    gmap[left][right] = ans
    return ans


def win3(arr: list):
    if arr is None or len(arr) == 0:
        return 0
    n = len(arr)
    fmap = [[0] * n for i in range(n)]
    gmap = [[0] * n for i in range(n)]
    for i in range(n):
        fmap[i][i] = arr[i]
    for start_col in range(1, n):
        left = 0
        right = start_col
        while right < n:
            fmap[left][right] = max(arr[left] + gmap[left + 1][right], arr[right] + gmap[left][right - 1])
            gmap[left][right] = min(fmap[left + 1][right], fmap[left][right - 1])
            left += 1
            right += 1
    return max(fmap[0][n - 1], gmap[0][n - 1])


if __name__ == '__main__':
    test = [5, 7, 4, 5, 8, 1, 6, 0, 3, 4, 6, 1, 7]
    print(win1(test))
    print(win2(test))
    print(win3(test))
