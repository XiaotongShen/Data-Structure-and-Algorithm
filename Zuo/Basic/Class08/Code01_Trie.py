# -*- coding: utf-8 -*-

"""
@File: Code01_Trie.py
@Author: Sarah Shen
@Time: 19/10/2022 11:26
"""


# 测试链接 : https://leetcode.cn/problems/implement-trie-ii-prefix-tree/
# 提交Trie类可以直接通过
# 原代码是对的，但是既然找到了直接的测试的链接，那就直接测吧
# 这个链接上要求实现的功能和课上是一样的
# 该前缀数的路用数组实现


class Trie:

    class Node:
        """ 前缀树的节点 """
        # p(pass)：通过节点的字符串个数
        # e(end)：以节点结尾的字符串个数
        # nexts: 通向26个字母的路
        def __init__(self):
            self.p = 0
            self.e = 0
            self.nexts = [None] * 52

    def __init__(self):
        """ 定义一个空的前缀树 """
        self.root = self.Node()

    def insert(self, word: str):
        """ 向前缀树中插入字符串word """
        # 如果word是空值，直接退出
        # 将word转换成数组，str -> list
        # node从根节点开始：
        # node.p + 1 -> 定义路径 = 0 （代表小写字母“a”）
        # 从左往右遍历转化成list的word -> 检查走那条路 -> 如果路为空，新建路 -> node来到该通路下面的节点 -> 当前node.p + 1
        # 当所有元素遍历完后，字符串word结束，最后一个node的e + 1
        if word is None:
            return
        chs = list(word)
        node = self.root
        node.p += 1
        base = ord("A")
        for element in chs:
            index = (ord(element) - base - 6) if element.lower() == element else ord(element) - base  # 判断当前ele属于nexts中的哪一条路
            if node.nexts[index] is None:
                node.nexts[index] = self.Node()
            node = node.nexts[index]
            node.p += 1
        node.e += 1

    def erase(self, word: str):
        """ 移除前缀树中的字符串word """
        # 如果数组中word的个数非零
        # word -> list
        # 从根节点开始，p-1，初始化路径
        # 从左到右遍历字符，当前节点p-1，找到当前节点下一个路径，如果路径后节点p-1 = 0, 当前节点的下一个路径设为空，返回;否则当前节点来到下一个，
        # 最后一个节点e-1
        if self.count_words_equal_to(word) != 0:
            chs = list(word)
            node = self.root
            node.p -= 1
            base = ord("A")
            for element in chs:
                index = (ord(element) - base - 6) if element.lower() == element else ord(element) - base
                node.p -= 1
                node.nexts[index].p -= 1
                if node.nexts[index].p == 0:
                    node.nexts[index] = None
                    return
                node = node.nexts[index]
            node.e -= 1

    def count_words_equal_to(self, word: str):
        """ 检查数组中有字符串word的个数 """
        # 如果word为空，返回0
        # word -> list
        # 从左到右遍历：中间遇到空的Node，返回0；否则遍历到最后一个node,返回其e值
        if word is None:
            return 0
        chs = list(word)
        node = self.root
        base = ord("A")
        for element in chs:
            index = (ord(element) - base - 6) if element.lower() == element else ord(element) - base
            if node.nexts[index] is None:
                return 0
            node = node.nexts[index]
        return node.e

    def count_words_start_with(self, pre: str):
        """ 检查数组中有以pre开头的字符串的个数 """
        # 如果pre为空，返回0
        # pre -> list
        # 从左到右遍历：中间遇到空的Node，返回0；否则遍历到最后一个node,返回其p值
        if pre is None:
            return 0
        chs = list(pre)
        node = self.root
        base = ord("A")
        for element in chs:
            index = (ord(element) - base - 6) if element.lower() == element else ord(element) - base
            if node.nexts[index] is None:
                return 0
            node = node.nexts[index]
        return node.p


if __name__ == "__main__":
    lower = list("abcdefghijklmnopqrstuvwxyz")
    upper = list("abcdefghijklmnopqrstuvwxyz".upper())
    print(lower)
    print(upper)
    lower_ord = []
    for ele in lower:
        lower_ord.append(ord(ele))
    print(lower_ord)

    upper_ord = []
    for ele in upper:
        upper_ord.append(ord(ele))
    print(upper_ord)

    x = "a"
    y = "B"
    print(ord(x), ord(x.lower()))
    print(ord(y), ord(y.lower()))
    print(ord(y.lower()) - ord(y))
    print(ord("A"))
    print(ord("a") - 32)
    print(ord("A") - ord("A"))
    print(ord("a") - ord("A") - 6)

    # path = (ord(ele) - base) if ele.lower() != ele else ord(ele) - base - 6
