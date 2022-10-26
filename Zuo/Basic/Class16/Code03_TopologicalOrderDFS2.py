# -*- coding: utf-8 -*-

"""
@File: Code03_TopologicalOrderDFS2.py
@Author: Sarah Shen
@Time: 25/10/2022 17:12
"""


# OJ链接：https://www.lintcode.com/problem/topological-sorting


class DirectedGraphNode:

    def __init__(self, x):
        self.label = x
        self.neighbors = list()


class Record:

    def __init__(self, n: DirectedGraphNode, o: int):
        self.node = n  # 节点本身
        self.nodes = o  # 节点往下走所有的点次


def comparator(o1, o2):
    return 0 if o1.nodes == o2.nodes else (o2.nodes - o1.nodes)


def cmp_to_key(mycmp):
    """
    Convert a cmp= function into a key= function
    """

    class K:
        def __init__(self, obj):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


def top_sort(graph):
    order = dict()
    for cur in graph:
        f(cur, order)
    record_arr = list()
    for r in order.values():
        record_arr.append(r)
    record_arr.sort(key=cmp_to_key(comparator))
    ans = list()
    for r in record_arr:
        ans.append(r.node)
    return ans


# 当前来到cur点，请返回cur点所到之处，所有的点次
# 返回（cur, 点次）
# 缓存入order
# key： 某一个点的点次，之前算过了
# value：点次是多少
def f(cur: DirectedGraphNode, order: dict):
    # cur的点次之前算过
    if order.keys().__contains__(cur):
        return order[cur]
    # cur的点次之前没算过
    nodes = 0
    for nxt in cur.neighbors:
        nodes += f(nxt, order).nodes
    ans = Record(cur, nodes + 1)
    order[cur] = ans
    return ans
