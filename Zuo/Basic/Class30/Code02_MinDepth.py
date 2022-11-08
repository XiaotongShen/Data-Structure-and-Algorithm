# -*- coding: utf-8 -*-

"""
@File: Code02_MinDepth.py
@Author: Sarah Shen
@Time: 08/11/2022 11:41
"""
import sys


# 本题测试链接 : https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    def max_depth1(self, root):
        """ 二叉树递归的方式解题, 一般解 """
        if root is None:
            return 0
        return self.process(root)

    def process(self, x):
        """ 返回x为头的树，最小深多是多少 """
        if x.left is None and x.right is None:
            return 1
        left_height = sys.maxsize  # 左右子树至少有一个不为空
        if x.left is not None:
            left_height = self.process(x.left)
        right_height = sys.maxsize
        if x.right is not None:
            right_height = self.process(x.right)
        return 1 + min(left_height, right_height)


class Solution2:

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    @staticmethod
    def max_depth2(root):
        """ 此方法是morris遍历的解 """
        if root is None:
            return 0
        cur = root
        cur_level = 0
        min_height = sys.maxsize
        while cur is not None:
            most_right = cur.left
            if most_right is not None:
                right_board_size = 1
                while most_right.right is not None and most_right.right != cur:
                    right_board_size += 1
                    most_right = most_right.right
                if most_right.right is None:
                    # 第一次到达cur
                    cur_level += 1
                    most_right.right = cur
                    cur = cur.left
                    continue
                else:  # 第二次达到粗人
                    if most_right.left is None:
                        min_height = min(min_height, cur_level)
                    cur_level -= right_board_size
                    most_right.right = None
            else:  # 只有一次到达
                cur_level += 1
        final_right = 1
        cur = root
        while cur.right is not None:
            final_right += 1
            cur = cur.right
        if cur.left is None and cur.right is None:
            min_height = min(min_height, final_right)
        return min_height
