# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/3/18.
Author: 
    Sarah Shen
Date: 
    2022/3/18
"""

"""
图描述
start -> a : 10
a -> b : 20
b -> c : 1
b -> fin : 30
c -> a : 1
"""

# 定义图
graph = {}
graph["start"] = {}
graph["start"]["a"] = 10
graph["a"] = {}
graph["a"]["b"] = 20
graph["b"] = {}
graph["b"]["c"] = 1
graph["b"]["fin"] = 30
graph["c"] = {}
graph["c"]["a"] = 1
graph["fin"] = {}

# 定义costs
infinity = float("inf")
costs = {}
costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs["fin"] = infinity

# 定义parents
parents = {}
parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["fin"] = None

# 定义已处理
processed = []

# 定义图初始状态
graph_b = {}
graph_b["graph"] = graph
graph_b["costs"] = costs
graph_b["parents"] = parents
graph_b["processed"] = processed

def find_lowest_cost_path_to_fin(graph_start):
    """
    获取graph中起点到终点开销最小的路径
    :param graph:
    :return:
    """
    graph = graph_start["graph"]
    costs = graph_start["costs"]
    parents = graph_start["parents"]
    processed = graph_start["processed"]

    def find_lowest_cost_node(costs):
        """
        找到未处理的节点中，开销最小的节点
        :param costs:
        :return:
        """
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs.keys():
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    start_lowest_cost_node = find_lowest_cost_node(costs)
    print(" ")
    print("要处理的图：", graph)
    print(" ")
    print("起点处节点开销：", costs)
    print("起点处节点父节点：", parents)
    print("起点处已处理节点列表：", processed)
    print("起点处开销最小节点", start_lowest_cost_node)

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    print(" ")
    print("各节点最小开销：", costs)
    print("各节点最小开销父节点：", parents)
    print("处理过的所有节点：", processed)
    print("到达终点的最小开销：", costs["fin"])

    graph_fin = {}
    graph_fin["graph"] = graph
    graph_fin["costs"] = costs
    graph_fin["parents"] = parents
    graph_fin["processed"] = processed

    return graph_fin

result_for_graph_b = find_lowest_cost_path_to_fin(graph_b)
