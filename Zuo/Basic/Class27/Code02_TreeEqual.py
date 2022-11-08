# -*- coding: utf-8 -*-

"""
@File: Code02_TreeEqual.py
@Author: Sarah Shen
@Time: 03/11/2022 12:59
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def is_sub_tree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        b = self.pre_serial(root)
        a = self.pre_serial(subRoot)
        s = [''] * len(b)
        for i in range(len(s)):
            s[i] = b[i]
        m = [''] * len(a)
        for j in range(len(m)):
            m[j] = a[j]
        return self.get_index_of(s, m) != -1

    def pre_serial(self, head):
        ans = list()
        self.pres(head, ans)
        return ans

    def pres(self, head, ans: list):
        if head is None:
            ans.append(None)
        else:
            ans.append(str(head.val))
            self.pres(head.left, ans)
            self.pres(head.right, ans)

    def get_index_of(self, str1: list, str2: list):
        if str1 is None or str2 is None or len(str2) < 1 or len(str1) < len(str2):
            return -1
        x = 0
        y = 0
        nxt = self.get_next_array(str2)
        while x < len(str1) and y < len(str2):
            if self.is_equal(str1[x], str2[y]):
                x += 1
                y += 1
            elif nxt[y] == -1:
                x += 1
            else:
                y = nxt[y]
        return x - y if len(str2) == y else -1

    def get_next_array(self, ms: [str]):
        if len(ms) == 1:
            return [-1]
        nxt = [0] * len(ms)
        nxt[0] = -1
        nxt[1] = 0
        i = 2
        cn = 0
        while i < len(nxt):
            if self.is_equal(ms[i - 1], ms[cn]):
                cn += 1
                nxt[i] = cn
                i += 1
            elif cn > 0:
                cn = nxt[cn]
            else:
                nxt[i] = 0
                i += 1
        return nxt

    @staticmethod
    def is_equal(a: str, b: str):
        if a is None and b is None:
            return True
        else:
            if a is None or b is None:
                return False
            else:
                return a == b
