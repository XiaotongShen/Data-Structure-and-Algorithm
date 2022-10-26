# -*- coding: utf-8 -*-

"""
@File: Code03_TopologySort.py
@Author: Sarah Shen
@Time: 25/10/2022 17:12
"""
# 拓扑排序不唯一，但是每一个都对
# 思路：使用入do，入do为零的打印，消除影响
from queue import Queue


def sorted_topology(graph):
    # key是某个节点，value为剩余的入度
    in_map = dict()
    # 只有剩余入度是0的节点，才进这个队列
    zero_in_queue = Queue()
    for node in graph.nodes:
        in_map[node] = node.in_nodes
        if node.in_nodes == 0:
            zero_in_queue.put(node)
    res = list()
    while not zero_in_queue.empty():
        cur = zero_in_queue.get()
        res.append(cur)
        for nxt in cur.next_nodes:
            in_map[nxt] = in_map.get(nxt) - 1
            if in_map.get(nxt) == 0:
                zero_in_queue.put(nxt)
    return res
