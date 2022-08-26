# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/16.
Author: 
    Sarah Shen
Date: 
    2022/8/16
"""

# 判断一棵树是否是平衡二叉树
# 平衡树：每一颗子树，左树的高度和右树高度差不超过1，则为平衡树
# X为root的二叉树， 左树为平衡树，右树也为平衡树，如果左树和右树的高度差不超过1，则以X为root的树为平衡二叉树
# 递归的方式

# 判断一棵树是否是搜索二叉树
# 搜索二叉树，每一颗子树，左树节点都比我小，右树节点都比我大
# 方法1，搜索二叉树的中序遍历一定是递增的
# 方法2，构造递归函数，X为root的二叉树，满足：左树是搜索二叉树，右树是搜索二叉树，左树的最大值小于 X， 右树的最大值大于X，则以X为根的二叉树为搜说二叉树


# 对于每个几点，获取其最全的信息：是否是搜索二叉树，你的最大值是多少，你的最小值是多少；
# 获取到信息后，先判断信息是否为空：
#     如果info不为空，继续对子树获取Info，直到获取到其整棵树的最大的最大值，或最小的最小值
# 一旦左树或者右树不为空，且不是搜索二叉树，则返回False，如果左树右树都是搜说二叉树，且左树的最大值 不小于X，右树最小值是否大于X，

# 判断一颗二叉树是否是搜索二叉树

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 3 个条件：左树是搜索二叉树， 右树是搜索二叉树， 左树的最大值 小于node右树 小于右树最小值
class Solution:

    def isValidBST(self, root):
        return self.process(root).is_bst

    class Info:
        def __init__(self, is_bst=True, mx=None, mi=None):
            self.is_bst = is_bst
            self.max = mx
            self.min = mi

    def process(self, x):
        if x is None:
            return None
        else:
            # 获取x的左树和右树的全部信息
            left_info = self.process(x.left)
            right_info = self.process(x.right)
            # 获取以x为root的树的最大值和最小值
            ma = x.val
            mi = x.val
            if left_info is not None:
                ma = max(left_info.max, ma)
                mi = min(left_info.min, mi)
            if right_info is not None:
                ma = max(right_info.max, ma)
                mi = min(right_info.min, mi)
            # 判断当前树是否为搜索二叉树
            is_bst = True
            # 左树和右树是否为搜索二叉树
            if left_info is not None and not left_info.is_bst:
                is_bst = False
            if right_info is not None and not right_info.is_bst:
                is_bst = False
            # 左树最大值是否小于x，x是否小于右树最小值
            left_max_lt_x = (left_info is None) | (left_info is not None and left_info.max < x.val)
            right_min_gt_x = (right_info is None) | (right_info is not None and x.val < right_info.min)
            if not left_max_lt_x or not right_min_gt_x:
                is_bst = False

        return self.Info(is_bst, ma, mi)


if __name__ == '__main__':
    r1 = TreeNode(2)
    r1.left = TreeNode(1)
    r1.right = TreeNode(3)

    r2 = TreeNode(5)
    r2.left = TreeNode(1)
    r2.right = TreeNode(4)
    r2.right.left = TreeNode(3)
    r2.right.right = TreeNode(6)

    s = Solution()
    print(s.isValidBST(r1))
    print(s.isValidBST(r2))

    r3 = TreeNode(32)
    r3.left = TreeNode(26)
    r3.right = TreeNode(47)
    r3.left.left = TreeNode(19)
    r3.right.right = TreeNode(56)
    r3.left.left.right = TreeNode(27)

    print(s.isValidBST(r3))








