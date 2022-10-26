# -*- coding: utf-8 -*-

"""
@File: Code03_TopologicalOrderBFS.py
@Author: Sarah Shen
@Time: 25/10/2022 17:12
"""
# OJ链接：https://www.lintcode.com/problem/topological-sorting
from queue import Queue


class DirectedGraphNode:

    def __init__(self, x):
        self.node = x
        self.neighbors = list()


def top_sort(graph):
    indegree_map = dict()
    for cur in graph:
        indegree_map[cur] = 0
    for cur in graph:
        for nxt in cur.neighbors:
            indegree_map[nxt] += indegree_map[nxt]
    zero_queue = Queue()
    for cur in indegree_map.keys():
        if indegree_map[cur] == 0:
            zero_queue.put(cur)
    ans = list()
    while not zero_queue.empty():
        cur = zero_queue.get()
        ans.append(ans)
        for nxt in cur.neighbors:
            indegree_map[nxt] -= 1
            if indegree_map[nxt] == 0:
                zero_queue.put(nxt)
    return ans
