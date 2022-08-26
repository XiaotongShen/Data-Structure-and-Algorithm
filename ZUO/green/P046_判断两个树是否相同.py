# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/8.
Author: 
    Sarah Shen
Date: 
    2022/8/8
"""
# 二叉树不能有环路
# 先序遍历：每一棵子树先打印头树，左树，右树
# 中序遍历：每一棵子树先打印左树，头树，右树
# 后序遍历：每一棵紫薯先打印左树，右树，头树


# 判断两棵树是否相同
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    else:
        return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == '__main__':
    n1 = TreeNode(1)
    n1.left = TreeNode(2)
    n1.right = TreeNode(3)

    n2 = TreeNode(1)
    n2.left = TreeNode(2)
    n2.right = TreeNode(3)

    n3 = TreeNode(1)
    n3.left = TreeNode(2)

    n4 = TreeNode(1)
    n4.right = TreeNode(2)

    print(is_same_tree(n1, n2))
    print(is_same_tree(n3, n4))



