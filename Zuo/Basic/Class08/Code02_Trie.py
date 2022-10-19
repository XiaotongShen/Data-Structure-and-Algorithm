# -*- coding: utf-8 -*-

"""
@File: Code02_Trie.py
@Author: Sarah Shen
@Time: 19/10/2022 11:27
"""


# 测试链接 : https://leetcode.cn/problems/implement-trie-ii-prefix-tree/
# 提交Trie类可以直接通过
# 原代码是对的，但是既然找到了直接的测试的链接，那就直接测吧
# 这个链接上要求实现的功能和课上是一样的
# 该前缀数的路用哈希表实现


class Trie:
    class Node:
        """ 定义前缀树的节点 """

        def __init__(self):
            self.p = 0
            self.e = 0
            self.nexts = dict()

    def __init__(self):
        """ 初始化类属性 """
        self.root = self.Node()

    def insert(self, word: str):
        if word is None:
            return
        chs = list(word)  # word -> list
        node = self.root  # 当前节点来到根节点
        node.p += 1  # 根节点pass + 1
        for element in chs:  # 从左到右遍历word字符
            index = ord(element)
            if not node.nexts.keys().__contains__(index):
                # 如果nexts中没有index，表示没有element通路
                node.nexts[index] = self.Node()  # 新建通路
            node = node.nexts.get(index)  # node来到下一个节点
            node.p += 1  # 当前节点pass + 1
        node.e += 1  # 遍历后最后一个节点

    def erase(self, word):
        if self.count_words_equal_to(word) != 0:
            chs = list(word)
            node = self.root
            node.p -= 1
            for element in chs:
                index = ord(element)
                if node.nexts.get(index).p - 1 == 0:
                    node.nexts.pop(index)
                    return
                node = node.nexts.get(index)
            node.e -= 1

    def count_words_equal_to(self, word: str):
        if word is None:
            return 0
        chs = list(word)
        node = self.root
        for element in chs:
            index = ord(element)
            if not node.nexts.keys().__contains__(index):
                return 0
            node = node.nexts.get(index)
        return node.e

    def count_words_starting_with(self, prefix: str):
        if prefix is None:
            return 0
        chs = list(prefix)
        node = self.root
        for element in chs:
            index = ord(element)
            if not node.nexts.keys().__contains__(index):
                return 0
            node = node.nexts.get(index)
        return node.p
