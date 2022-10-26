# -*- coding: utf-8 -*-

"""
@File: Code01_BFS.py
@Author: Sarah Shen
@Time: 25/10/2022 17:12
"""
# TODO
# 所有图都是有向图，
# 图的标识方法：
# 1. 邻接表法 dict
# 2. 邻接指针法： 用矩阵
# 3. 最长遇到的表示方法：list of list[[from, weight, to]]
# 4. 用数组方式表示： index 指向指
# 图的算法题，难点在于图的表示方式多种多样，coding会很复杂
# 对策是，将不同的图结构，转化为固定的图结构，然后解题
from queue import Queue


def bfs(node):
    if node is None:
        return
    q = Queue()




