# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/16.
Author: 
    Sarah Shen
Date: 
    2022/8/16
"""

# 原来的节点 linked-list，之前的累加和，达标和的值，达标路径的list
# basecase是到达叶节点的时候


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum(self, root, targetSum):
        ans = []
        if root is None:
            return ans
        path = []
        self.process(root, path, 0, targetSum, ans)
        return ans

    def process(self, x:TreeNode, path:list, pre_sum:int, sum:int, ans:list[list]):
        if x.left is None and x.right is None:
            if pre_sum + x.val == sum:
                path.append(x.val)
                ans.append(path.copy())
                path.pop()
            return
        path.append(x.val)
        pre_sum += x.val
        if x.left is not None:
            self.process(x.left, path, pre_sum, sum, ans)
        if x.right is not None:
            self.process(x.right, path, pre_sum, sum, ans)
        path.pop()


if __name__ == '__main__':

    r1 = TreeNode(5)
    r1.left = TreeNode(4)
    r1.right = TreeNode(8)
    r1.left.left = TreeNode(11)
    r1.left.left.left = TreeNode(7)
    r1.left.left.right = TreeNode(2)
    r1.right.left = TreeNode(13)
    r1.right.right = TreeNode(4)
    r1.right.right.left = TreeNode(5)
    r1.right.right.right = TreeNode(1)

    r2 = TreeNode(1)
    r2.left = TreeNode(2)
    r2.right = TreeNode(3)

    r3 = None

    r = TreeNode(3)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.left.left = TreeNode(1)
    r.left.right = TreeNode(1)
    r.left.right.left = TreeNode(0)
    r.left.right.right = TreeNode(0)

    a = [3,8,6,7,4]
    b = a.copy()
    print(a)
    print(b)
    print(id(a))
    print(id(b))
    print(a.pop())
    print(a)

    s = Solution()
    print(s.pathSum(r1, 22))
    print(s.pathSum(r2, 5))
    print(s.pathSum(r, 6))


