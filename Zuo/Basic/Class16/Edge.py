# -*- coding: utf-8 -*-

"""
@File: Edge.py
@Author: Sarah Shen
@Time: 25/10/2022 17:13
"""


# 边结构的表述
class Edge:

    def __init__(self, weight: int, fn, tn):
        self.weight = weight
        self.from_node = fn
        self.to_node = tn
