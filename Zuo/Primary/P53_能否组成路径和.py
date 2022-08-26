# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/16.
Author: 
    Sarah Shen
Date: 
    2022/8/16
"""

# 根节点到也节点的任何一条路径和是否非指定值
# 方法1 用pre_sum and sum 的方式实现，process判断是否有和为指定值的时刻发生。
# 清理现场



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, x, targetSum):
        if x is None:
            return False
        else:
            if x.left is None and x.right is None:
                return x.val == targetSum
            else:
                return self.hasPathSum(x.left, targetSum - x.val) | self.hasPathSum(x.right, targetSum - x.val)


if __name__ == '__main__':
    r1 = TreeNode(5)
    r1.left = TreeNode(4)
    r1.right = TreeNode(8)
    r1.left.left = TreeNode(11)
    r1.left.left.left = TreeNode(7)
    r1.left.left.right = TreeNode(2)
    r1.right.left = TreeNode(13)
    r1.right.right = TreeNode(4)
    r1.right.right.right = TreeNode(1)

    r2 = TreeNode(1)
    r2.left = TreeNode(2)
    r2.righg = TreeNode(3)

    r3 = None

    s = Solution()
    print(s.hasPathSum(r1, 22))
    print(s.hasPathSum(r2, 5))
    print(s.hasPathSum(r3, 0))




