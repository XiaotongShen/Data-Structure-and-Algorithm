# -*- coding: utf-8 -*-

"""
@File: Code06_Dijkstra.py
@Author: Sarah Shen
@Time: 25/10/2022 17:13
"""
import sys


# no negative weight


def dijkstra1(f):
    # 定义一个距离哈希表，key：value = 结束节点：开始节点与结束节点距离的最小值
    # 定义一个set，放入选择的节点，也就与开始节点距离小于无穷的点的集合
    # 获取未被选择的点中，与开始节点最近的点
    distance_map = dict()
    distance_map[f] = 0
    selected_nodes = set()
    selected_nodes.add(f)
    min_node = get_min_distance_and_unselected_node(distance_map, selected_nodes)
    while min_node is not None:
        # 更新开始节点到min_node（跳转节点）的最小距离
        d = distance_map[min_node]
        for edge in min_node.edges:
            to_node = edge.t
            if not distance_map.keys().__contains__(to_node):
                distance_map[to_node] = d + edge.weight
            else:
                distance_map[to_node] = min(distance_map[to_node], d + edge.weight)
        selected_nodes.add(min_node)
        min_node = get_min_distance_and_unselected_node(distance_map, selected_nodes)
    return distance_map


def get_min_distance_and_unselected_node(distance_map, selected_nodes):
    min_node = None
    min_distance = sys.maxsize
    for entry in distance_map:
        n = entry.keys()
        d = entry.values()
        if not selected_nodes.__contains__(n) and d < min_distance:
            min_node = n
            min_distance = d
    return min_node


# TODO: 改进后的dijkstra算法

class NodeRecord:

    def __init__(self, node, distance):
        self.node = node
        self.distance = distance


class NodeHeap:

    def __init__(self, size):
        self.nodes = [None] * size
        self.heap_index_map = dict()
        self.distance_map = dict()
        self.size = 0

    def is_empty(self):
        return self.size == 0

        # 有一个点叫node，现在发现了一个从源节点出发到达node的距离为distance

    # 判断要不要更新，如果需要的话，就更新
    def add_or_update_or_ignore(self, node, distance):
        if self.in_heap(node):
            self.distance_map[node] = min(self.distance_map[node], distance)

    def pop(self):
        print(self.size)

    def insert_heapify(self, idx):
        print(self.size, idx)

    def heapify(self, idx, size):
        print(self.size, idx, size)

    def is_entered(self, node):
        print(self.size, node)

    def in_heap(self, node):
        print(self.size, node)

    def swap(self, idx1, idx2):
        print(self.size, idx1, idx2)


def dijkstra2(head, size: int):
    print(head, size)
