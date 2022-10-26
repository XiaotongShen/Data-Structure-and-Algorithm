# -*- coding: utf-8 -*-

"""
@File: Code04_Kruskal.py
@Author: Sarah Shen
@Time: 25/10/2022 17:12
"""
from queue import PriorityQueue


# 找到最小生成树的算法1：Kruskal
# undirected graph only
# 首先定义一个并查集的类
class UnionFind:

    def __init__(self):
        self.father_map = dict()
        self.size_map = dict()

    def make_sets(self, nodes):
        self.father_map.clear()
        self.size_map.clear()
        for node in nodes:
            self.father_map[node] = node
            self.size_map[node] = 1

    def find_father(self, n):
        path = list()
        while n != self.father_map[n]:
            path.append(n)
            n = self.father_map[n]
        while len(path) != 0:
            self.father_map[path.pop()] = n
        return n

    def is_same_set(self, a, b):
        return self.father_map[a] == self.father_map[b]

    def union(self, a, b):
        if a is None and b is None:
            return
        a_father = self.find_father(a)
        b_father = self.find_father(b)
        if a_father != b_father:
            a_set_size = self.size_map[a_father]
            b_set_size = self.size_map[b_father]
            if a_set_size >= b_set_size:
                self.father_map[b_father] = a_father
                self.size_map[a_father] += self.size_map[b_father]
                self.size_map.pop(b_father)
            else:
                self.father_map[a_father] = b_father
                self.size_map[b_father] += self.size_map[a_father]
                self.size_map.pop(a_father)


def kruskal_mst(graph):
    """ 用kruskal的方法获取最小生成树 """
    # 首先定义一个空的并查集，将graph的每一个节点的值放入并查集
    # 定义一个小根堆，将所以边放入小根堆，要求按照边的权重排序
    # 一个set作为结果
    # 当小根堆（边的小根堆）不为空的时候
    # 从小根堆中拿出一个边
    # 如果边的from和to不是同一个集合，则把边放入set中，并合并from与to
    # 周而复始，直到小根堆为空，即遍历完所有的边
    uf = UnionFind()
    uf.make_sets(graph.nodes.values())
    # 保存边的小根堆
    pq = PriorityQueue()
    for edge in graph.edges:
        pq.put((edge.weight, edge))  # 按权重排序，放入小根堆
    # 结果set，放入选中的边
    res = set()
    while not pq.empty():
        edge = pq.get()
        if not uf.is_same_set(edge.f, edge.t):
            res.add(edge)
            uf.union(edge.f, edge.t)
    return res
