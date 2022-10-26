# -*- coding: utf-8 -*-

"""
@File: Graph.py
@Author: Sarah Shen
@Time: 25/10/2022 17:13
"""


# 图结构的描述，图由点和边组成
class Graph:

    def __init__(self):
        self.nodes = dict()  # hashmap
        self.edges = dict()  # hashset
