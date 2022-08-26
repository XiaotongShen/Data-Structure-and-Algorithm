# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/12.
Author:
    Sarah Shen
Date:
    2022/8/12
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if root is None:
        return 0
    else:
        return max(max_depth(root.left), max_depth(root.right)) + 1



if __name__ == '__main__':
    r1 = TreeNode(3)
    r1.left = TreeNode(9)
    r1.right = TreeNode(20)
    r1.right.left = TreeNode(15)
    r1.right.right = TreeNode(7)

    r2 = TreeNode(1)
    r2.right = TreeNode(2)

    print(max_depth(r1))
    print(max_depth(r2))


