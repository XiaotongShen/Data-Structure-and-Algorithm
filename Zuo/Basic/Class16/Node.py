# -*- coding: utf-8 -*-

"""
@File: Node.py
@Author: Sarah Shen
@Time: 25/10/2022 17:14
"""


# 点结构的描述
class Node:
    def __int__(self, v):
        self.value = v
        self.in_nodes = 0
        self.out_nodes = 0
        self.next_nodes = list()
        self.edges = list()
