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
        d = distance_map.get(min_node)
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
        # 第一种情况，node在heap上，需要更新
        if self.in_heap(node):
            self.distance_map[node] = min(self.distance_map[node], distance)
            # 因为node的distance变小了，所以只需要向上调整
            self.insert_heapify(self.heap_index_map.get(node))
            # 第二种情况，node还没有加入到index_map中，则需要加入
        if not self.is_entered(node):
            self.nodes[self.size] = None
            self.heap_index_map[node] = self.size
            self.distance_map[node] = distance
            self.insert_heapify(self.size)
            self.size += 1
        # 第三种情况，node已经在index_map中，即被加入过，但是没有在heap上，说明已经被弹出了，直接忽略

    def pop(self):
        # 获得加强堆顶的第一个节点及其距离
        node_record = NodeRecord(self.nodes[0], self.distance_map[self.nodes[0]])
        self.swap(0, self.size - 1)  # 交换堆顶和堆尾最后一个节点
        self.heap_index_map[self.nodes[self.size - 1]] = -1  # 交换过来的堆尾的节点，index放-1
        self.distance_map.pop(self.nodes[self.size - 1])  # 将最后一个几点从distance_map中移除
        self.nodes[self.size - 1] = None  # 堆尾最后一个节点置空
        self.size -= 1  # 堆长度-1
        self.heapify(0, self.size)  # 向下调整换上来的堆顶节点
        # 最后将获得的堆顶的节点返回
        return node_record

    def insert_heapify(self, idx):
        """ 向上调整idx位置的节点 """
        while self.distance_map[self.nodes[idx]] < self.distance_map[self.nodes[int((idx - 1) / 2)]]:
            # 如果该节点的distance 小于其父节点的distance，向上交换
            self.swap(idx, int((idx - 1) / 2))
            idx = int((idx - 1) / 2)

    def heapify(self, idx, size):
        """ 向下调整id位置的几点，在长度为size的堆上 """
        left = idx * 2 + 1  # idx 左树节点的index
        while left < size:  # 左树存在
            smallest = left + 1 if left + 1 < size and self.distance_map[self.nodes[left + 1]] < self.distance_map[
                self.nodes[left]] else left
            smallest = smallest if self.distance_map[self.nodes[smallest]] < self.distance_map[self.nodes[idx]] else idx
            if smallest == idx:
                break
            self.swap(smallest, idx)
            idx = smallest
            left = smallest * 2 + 1

    def is_entered(self, node):
        """ 判断节点是否加入过index_map """
        return self.heap_index_map.keys().__contains__(node)

    def in_heap(self, node):
        return self.is_entered(node) and self.heap_index_map[node] != -1

    def swap(self, idx1, idx2):
        # index_map交换值
        self.heap_index_map[self.nodes[idx1]] = idx2
        self.heap_index_map[self.nodes[idx2]] = idx1
        # nodes交换
        temp = self.nodes[idx1]
        self.nodes[idx1] = self.nodes[idx2]
        self.nodes[idx2] = temp

        print(self.size, idx1, idx2)


# 改进后的dijkstra算法
# 从head出发，所哟head能到达的节点，生成到达每个节点的最小路径记录并返回
def dijkstra2(head, size: int):
    # 生成长度为size的加强堆
    # 加入第一个节点，头节点
    # 生成结果字典表
    # 加强堆不为空，弹出堆顶节点记录
    # 获取当前节点distance
    # 遍历当前节点所有边，更新或加入所有边对应的to节点
    # 处理完当前节点后，将其加入结果字典表
    # 周而复始，至堆弹空，返回结果字典表
    node_heap = NodeHeap(size)
    node_heap.add_or_update_or_ignore(head, 0)
    res = dict()
    while not node_heap.is_empty():
        r = node_heap.pop()
        cur = r.node
        d = r.distance
        for e in cur.edges:
            node_heap.add_or_update_or_ignore(e.to, e.weight + d)
        res[cur] = d
    return res
