# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/16.
Author: 
    Sarah Shen
Date: 
    2022/8/16
"""
# array list 首尾交换就逆序了
# linked list 逆序的时间要快很多
# 对比array list 和 linked list的时间
# 对比不同的栈实现方式的计算速度：
## 语言本身的栈 比较慢
## 链表实现的栈 最慢
## 数组实现的栈 有利可图


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# step1 拿出此时队列的size，size有多少，step2 就进行多少回
# step2 弹出节点，有左先加左，有右再加右


class MyQueue:
    def __init__(self):
        self.arr = []
        # self.size = 0

    # def size(self):
    #     return len(self.arr)

    def add(self, ele):
        self.arr.append(ele)
        # self.size += 1

    def pop(self):
        if len(self.arr) == 0:
            print('This is an Empty Queue!')
        else:
            ele = self.arr[0]
            self.arr = self.arr[1:]
            # self.size -= 1
            return ele


def level_order(root):
    mq = MyQueue()
    level_list = []
    if root is None:
        pass
    else:
        mq.add(root)
        level_size = len(mq.arr)
        while level_size != 0:
            vals = []
            for i in range(level_size):
                node = mq.pop()
                if node is not None:
                    vals.append(node.val)
                    if node.left is not None:
                        mq.add(node.left)
                    else:
                        pass
                    if node.right is not None:
                        mq.add(node.right)
                    else:
                        pass
            level_list.append(vals)
            level_size = len(mq.arr)
    return level_list





if __name__ == '__main__':
    r1 = TreeNode(3)
    r1.left = TreeNode(9)
    r1.right = TreeNode(20)
    r1.right.left = TreeNode(15)
    r1.right.right = TreeNode(7)

    r2 = TreeNode(1)

    r3 = None

    print(level_order(r1))
    print(level_order(r2))
    print(level_order(r3))