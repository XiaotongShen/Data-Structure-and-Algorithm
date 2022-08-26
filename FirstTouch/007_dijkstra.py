# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/3/15.
    Dijkstra Algorithm 狄克斯特拉算法，用来处理有向无环加权图（DAG）
Author: 
    Sarah Shen
Date: 
    2022/3/15
"""

"""
图描述：
计算从起点到终点用时最短的路线
起点 -> A : 6 min
起点 -> B : 2 min
A -> 终点 : 1 min
B -> A : 3 min
B -> 终点 : 5 min
"""

# 首先编写3个散列表， 字典
# graph - 图，costs-开销， parents-父节点
print("有向无环，正权重，加权图最短路径问题的初始化")
# 定义图
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

print("要处理的图：", graph)
# print(graph["start"].keys())
# print(graph["start"]["a"])
# print(graph["start"]["b"])

# 定义开销
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity
print("从起点出发的节点开销：", costs)

# 定义父节点
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None
print("从起点出发的节点父节点",parents)


# 数组用于记录处理过的节点
processed = []
print("开始时处理过的节点：",processed)

# 算法描述
# 只要还有要处理的节点
# 获取离起点最近的节点
# 更新其邻居的开销
# 如果有邻居的开销被更新，同事更新其父节点
# 将该节点标记为处理过
# 回到第一步判断是否还有未处理的节点

# 首先定义找到最小开销的节点的公式
def find_lowest_cost_node(costs):
    """
    在未处理的节点中，找出开销最小的节点
    :param costs:
    :return: node
    """
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs.keys() :
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)     # 在未处理的节点中，找出开销最小的节点
while node is not None:                 # 这个while循环在所有节点都被处理过后结束
    cost = costs[node]                  # 获取正在处理的节点的开销
    neighbors = graph[node]             # 找到正在处理的节点的邻居
    for n in neighbors.keys():          # 对于每一个该节点的邻居
        new_cost = cost + neighbors[n]  # 计算从起点到邻居新的开销
        if costs[n] > new_cost:         # 如果新的开销更少
            costs[n] = new_cost        # 用新的开销更新该邻居的开销
            parents[n] = node           # 用正在处理的节点更新该邻居的父节点
    processed.append(node)              # 更新完节点的所有邻居，将正在处理的节点加入已处理的列表
    node = find_lowest_cost_node(costs) # 对于所有未处理的节点，找到其开销最小的节点，回到while的开头，如果还有未处理的节点，继续后面的步骤
print(" ")
print("找到最短路径后")
print("各节点最少开销：", costs)
print("最短路径中各节点的父节点：", parents)
print("结束时处理过的节点：", processed)


"""
小结
广度优先搜索用于在非加权图中查找最短路径
狄克斯特拉算法用于在加权图中查找最短路径
仅当权重为正时狄克斯特拉算法才管用
如果图中包含负权边，请使用贝尔曼-福德算法（Bellman-Ford Algorithm)
"""


