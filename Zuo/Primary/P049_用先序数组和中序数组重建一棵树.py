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

def build_tree(preorder, inorder):
    if preorder is None or inorder is None or len(preorder) != len(inorder):
        return None
    else:
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        else:
            value_index_map = {}
            for i in range(len(inorder)):
                value_index_map[inorder[i]] = i
            find = value_index_map[preorder[0]]

            if find == 0:
                preorder_left = None
                inorder_left = None
            else:
                preorder_left = preorder[1:find+1]
                inorder_left = inorder[0:find]

            preorder_right = preorder[find+1:]
            inorder_right = inorder[find+1:]
            root.left = build_tree(preorder_left, inorder_left)
            root.right = build_tree(preorder_right, inorder_right)
            return root


# ---------- LeetCode Solution ----------- #
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def array_to_tree(left, right):
            nonlocal preorder_index
            # if there are no elements to construct the tree
            if left > right: return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index]
            root = TreeNode(root_value)


            preorder_index += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)

if __name__ == '__main__':
    preorder = [3, 9, 4, 5, 20, 15, 7]
    inorder = [4, 9, 5, 3, 15, 20, 7]
    L1 = 0
    R1 = len(preorder) - 1
    L2 = 0
    R2 = len(inorder) - 1
    # print(preorder, L1, R1)
    # print(inorder, L2, R2)
    root = build_tree(preorder, inorder)
    print(root.val)
    print(root.left.val)
    print(root.left.left.val)
    print(root.left.right.val)
    print(root.right.val)
    print(root.right.left.val)
    print(root.right.right.val)

    # 将中序列表定义成哈希表
    # my_dict = {}
    # for i in range(len(inorder)):
    #     my_dict[inorder[i]] = i
    # print(my_dict)
    # 取出先序列表的第一个值，创建树的根几点
    # root = TreeNode(preorder[L1])
    #
    # root_val = preorder[L1]
    #
    # # 找到根节点值在中序列表中的index
    # find = my_dict[root_val]
    # print(find)
    # # 该index的左侧为左树的中序列表
    # # 该index的右侧为右树的中序列表
    # # 先序列表中，L1+1 位置开始，长度为find-L2的列表为左树的先序列表
    # # 先序列表中，L1+1 位置开始，长度为find-L2的列表为左树的先序列表
    # print("\n")
    # inorder_left = inorder[L2:find]
    # L2_left = L2
    # R2_left = find-1
    # preorder_left = preorder[L1+1: L1+find-L2+1]
    # L1_left = L1+1
    # R1_left = L1+find-L2
    # print(preorder_left, L1_left, R1_left)
    # print(inorder_left, L2_left, R2_left)
    # print(preorder_left[2])

    # root.left = f(preorder[L1+1: L1+find-L2+1], L1+1, L1+find-L2, inorder[L2:find], L2, find-1, my_dict)

    # print("\n")
    # inorder_right = inorder[find+1:R2+1]
    # L2_right = find+1
    # R2_right = R2
    # preorder_right = preorder[L1+find-L2+1: R1+1]
    # L1_right= L1+find-L2+1
    # R1_right = R1
    # print(preorder_right, L1_right, R1_right)
    # print(inorder_right, L2_right, R2_right)
    # root.right = f(preorder[L1+find-L2+1: R1+1], L1+find-L2+1, R1, inorder[find+1:R2+1], find+1, R2, my_dict)









