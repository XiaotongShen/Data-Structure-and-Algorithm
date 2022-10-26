# -*- coding: utf-8 -*-

"""
@File: Code05_Prim.py
@Author: Sarah Shen
@Time: 25/10/2022 17:13
"""
import sys
from queue import PriorityQueue


# 找到最小生成树的算法1：Kruskal
# undirected graph only
def prim_mst(graph):
    # 定义一个小根堆，放入解锁的边
    # 定义一个set，放入解锁的点
    # 定义一个set，放入挑选的点
    # 随便挑一个点，当其没被解锁的时候，将其所有的边放入小根堆
    #   当小跟堆不为空时，弹出解锁的边中最小的边，
    #   当to未解锁时，将当前边压入结果
    #   并将to的所有边解锁，压入小根堆
    #   周而复始，直到所有边解锁完毕
    pq = PriorityQueue()
    node_set = set()
    res = set()
    for node in graph.nodes.values():
        if not node_set.__contains__(node):
            node_set.add(node)  # 解锁node
            for edge in node.edges:
                pq.put(edge)  # 解锁node所有的边
            while not pq.empty():
                edge = pq.get()
                to_node = edge.t  # 可能的一个新点，即当前边的to
                if not node_set.__contains__(edge.t):
                    # 如果是新点
                    node_set.add(to_node)  # 加入集合
                    res.add(edge)  # 当前边加入结果
                    # 新点所有边压入优先级队列
                    for next_edge in to_node.edges:
                        pq.put(next_edge)
    return res


def prim(graph):
    size = len(graph)
    distances = [0] * size
    visit = [False] * size
    visit[0] = True
    for i in range(size):
        distances[i] = graph[0][i]
    total = 0
    for i in range(size):
        min_path = sys.maxsize
        min_index = -1
        for j in range(size):
            if not visit[j] and distances[j] < min_path:
                min_path = distances[j]
                min_index = j
        if min_index == -1:
            return total
        visit[min_index] = True
        total += min_path
        for j in range(size):
            if not visit[j] and distances[j] > graph[min_index][j]:
                distances[j] = graph[min_index][j]
        return total
