# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/3/15.
    第一种图算法 —— 广度优先搜索（breadth-first search, BFS)，可帮助回答两类问题：
        * 从节点A出发，有前往B点的路径吗？（在你的人际关系网中，有芒果销售商吗？）
        * 从节点A出发，前往B点的那条路径最短？（哪个芒果销售商与你的关系最近？）
Author: 
    Sarah Shen
Date: 
    2022/3/15
"""


# 最短路径问题(shortest-path problem) 从双子峰前往金门大桥

# 新的数据结构， 队列 queue （First In First Out） 先进先出
#           vs  栈 stack （Last In First Out）后进先出

# 用散列表来表示图(实现图)

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# print(graph["you"])

from collections import deque

search_queue = deque()        # 创建一个队列
search_queue += graph["you"]  # 将你的邻居创建到这个搜索队列中
# print(search_queue)

# while search_queue:                     # 只要队列不为空
#     person = search_queue.popleft()     # 就取出其中的第一个人
#     if person_is_seller(person):        # 检查这个人是否是芒果销售商
#         print(person + " is a mango seller!")       # 是芒果销售商
#         return True
#     else:
#         search_queue += graph[person]   # 不是芒果销售商，将这个人的朋友加入搜索队列
# return False
# # 如果到了这里，就说明队列中没有人是芒果销售商

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()          # 创建一个空的双端队列
    search_queue += graph[name]     # 将name的邻居加入到队列
    searched = []                   # 数组用于记录检查过的人
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person,"is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

print(search("you"))

print(search("peggy"))