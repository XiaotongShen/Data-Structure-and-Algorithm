# -*- coding: utf-8 -*-

"""
@File: GraphGenerator.py
@Author: Sarah Shen
@Time: 25/10/2022 17:14
"""


# 边结构的表述
class Edge:

    def __init__(self, weight: int, fn, tn):
        self.weight = weight
        self.from_node = fn
        self.to_node = tn


# 图结构的描述，图由点和边组成
class Graph:

    def __init__(self):
        self.nodes = dict()  # hashmap
        self.edges = dict()  # hashset


# 点结构的描述
class Node:
    def __init__(self, v):
        self.value = v
        self.in_nodes = 0
        self.out_nodes = 0
        self.next_nodes = list()
        self.edges = list()


# 定义一个图结构转化器，
# 初始的图结构是 N*3的矩阵
# [weight， from节点上面的值，to节点上面的值]
# 如
# [5, 0, 7]
# [3, 0, 1]
#
def create_graph(matrix):
    graph = Graph()
    for i in range(len(matrix)):
        # 拿到每一条边matrix[i]
        w = matrix[i][0]
        f = matrix[i][1]
        t = matrix[i][2]
        if not graph.nodes.keys().__contains__(f):
            graph.nodes[f] = Node(f)  # 如果node没有加到图中，则加入
        if not graph.nodes.keys().__contains__(t):
            graph.nodes[t] = Node(t)
        f_node = graph.nodes.get(f)
        t_node = graph.nodes.get(t)
        new_edge = Edge(w, f_node, t_node)
        f_node.next_nodes.append(t_node)
        f_node.out_nodes += 1
        t_node.in_nodes += 1
        graph.edges[new_edge] = True
    return graph
