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


def is_mirror(l, r):
    if l is None and r is None:
        return True
    elif l is None or r is None:
        return False
    else:
        return l.val == r.val and is_mirror(l.left, r.right) and is_mirror(l.right, r.left)


def is_symmetric(root):
    return is_mirror(root, root)


if __name__ == '__main__':
    r1 = TreeNode(1)
    r1.left = TreeNode(2)
    r1.right = TreeNode(2)
    r1.left.left = TreeNode(3)
    r1.right.right = TreeNode(3)
    r1.left.right = TreeNode(4)
    r1.right.left = TreeNode(4)

    r2 = TreeNode(1)
    r2.left = TreeNode(2)
    r2.right = TreeNode(2)
    r2.left.right = TreeNode(3)
    r2.right.right = TreeNode(3)

    print(is_symmetric(r1))
    print(is_symmetric(r2))
