# -*- coding: utf-8 -*-

"""
@File: Code01_SegmentTree.py
@Author: Sarah Shen
@Time: 08/11/2022 18:22
"""
# TODO
import random


class SegmentTree:
    """
    arr: 为原序列的信息，从0开始，但在arr里是从1开始的
    sum: 模拟先对数维护区间
    lazy: 为累加和的懒惰标记
    change: 为更新的值
    update: 为更新懒惰标记
    """

    def __init__(self, origin: [int]):
        self.max_n = len(origin) + 1
        self.arr = [0] * self.max_n  # arr[0]不用，从1开始使用
        for i in range(1, self.max_n):
            self.arr[i] = origin[i - 1]
        self.sum = [0] * (self.max_n << 2)  # 用来支持脑补概念中，某一个范围的累加和信息
        self.lazy = [0] * (self.max_n << 2)  # 用来支持脑补概念中，某一个范围没有往下传递的累加任务
        self.change = [0] * (self.max_n << 2)  # 用来支持脑补概念中，某一个范围有没有更新操作的任务
        self.update = [None] * (self.max_n << 2)  # 用来支持脑补概念中，某一个范围更的更新任务，更新成了什么

    def push_up(self, rt: int):
        self.sum[rt] = self.sum[rt << 1] + self.sum[rt << 1 | 1]  # 父节点的值等于左右节点值相加

    def push_down(self, rt: int, ln: int, rn: int):
        """
        之前的，所有懒增加和懒更新，从父范围，发给左右两个子范围
        分发策略是什么
        ln表示左子树元素节点个数，rn表示右子树节点个数
        """
        if self.update[rt]:
            self.update[rt << 1] = True
            self.update[rt << 1 | 1] = True
            self.change[rt << 1] = self.change[rt]
            self.change[rt << 1] = self.change[rt]
            self.lazy[rt << 1] = 0
            self.lazy[rt << 1 | 1] = 0
            self.sum[rt << 1] = self.change[rt] * ln
            self.sum[rt << 1 | 1] = self.change[rt] * rn
            self.update[rt] = False
        if self.lazy[rt] != 0:
            self.lazy[rt << 1] += self.lazy[rt]
            self.sum[rt << 1] += self.lazy[rt] * ln
            self.lazy[rt << 1 | 1] += self.lazy[rt]
            self.sum[rt << 1 | 1] += self.lazy[rt] * rn
            self.lazy[rt] = 0

    def build(self, l: int, r: int, rt: int):
        if l == r:
            self.sum[rt] = self.arr[l]
            return
        mid = (l + r) >> 1
        self.build(l, mid, rt << 1)
        self.build(mid + 1, r, rt << 1 | 1)
        self.push_up(rt)

    def tree_update(self, big_l: int, big_r: int, c: int, l: int, r: int, rt: int):
        """
        big_l ~ big_r 所有的值变成c
        l~r rt
        """
        # 可以懒更新的情况
        if big_l <= l and r <= big_r:
            self.update[rt] = True
            self.change[rt] = c
            self.sum[rt] = c * (r - l + 1)
            self.lazy[rt] = 0
            return
            # 当前任务躲不掉，无法兰更新，要往下发
        mid = (l + r) >> 1
        self.push_down(rt, mid - l + 1, r - mid)
        if big_l <= mid:
            self.tree_update(big_l, big_r, c, l, mid, rt << 1)
        if big_r > mid:
            self.tree_update(big_l, big_r, c, mid + 1, r, rt << 1 | 1)
        self.push_up(rt)

    def add(self, big_l: int, big_r: int, c: int, l: int, r: int, rt: int):
        # 懒更新的情况
        if big_l <= l and r <= big_r:
            self.sum[rt] += c * (r - l + 1)
            self.lazy[rt] += c
            return
        # 不能懒更新的情况
        mid = (l + r) >> 1
        self.push_down(rt, mid - l + 1, r - mid)
        if big_l <= mid:
            self.add(big_l, big_r, c, l, mid, rt << 1)
        if big_r > mid:
            self.add(big_l, big_r, c, mid + 1, r, rt << 1 | 1)
        self.push_up(rt)

    def query(self, big_l: int, big_r: int, l: int, r: int, rt: int):
        if big_l <= l and r <= big_r:
            return self.sum[rt]
        mid = (l + r) >> 1
        self.push_down(rt, mid - l + 1, r - mid)
        ans = 0
        if big_l <= mid:
            ans += self.query(big_l, big_r, l, mid, rt << 1)
        if big_r > mid:
            ans += self.query(big_l, big_r, mid + 1, r, rt << 1 | 1)
        return ans


class Right:
    """
    用来和线段树作比较的算法过程
    """

    def __init__(self, origin: [int]):
        self.arr = [0] * (len(origin) + 1)
        for i in range(len(origin)):
            self.arr[i + 1] = origin[i]

    def update(self, big_l: int, big_r: int, c: int):
        for i in range(big_l, big_r + 1):
            self.arr[i] = c

    def add(self, big_l: int, big_r: int, c: int):
        for i in range(big_l, big_r + 1):
            self.arr[i] += c

    def query(self, big_l: int, big_r: int):
        ans = 0
        for i in range(big_l, big_r + 1):
            ans += self.arr[i]
        return ans


def generate_random_array(max_len: int, max_value: int):
    size = int(random.random() * max_len) + 1
    origin = [0] * size
    for i in range(size):
        origin[i] = int(random.random() * max_value) + 1
    return origin


def test():
    max_l = 100
    max_v = 1000
    test_times = 1
    add_or_update_times = 100
    query_times = 50
    for i in range(test_times):
        origin = generate_random_array(max_l, max_v)
        seg = SegmentTree(origin)
        big_s = 1
        big_n = len(origin)
        root = 1
        seg.build(big_s, big_n, root)
        rig = Right(origin)

        # num1 = int(random.random() * big_n) + 1
        # num2 = int(random.random() * big_n) + 1
        # big_l = min(num1, num2)
        # big_r = max(num1, num2)
        # c = int(random.random() * max_v) + 1
        # seg.tree_update(big_l, big_r, c, big_s, big_n, root)
        # rig.update(big_l, big_r, c)
        # print(origin)
        # print((big_l, big_r), c)
        # print(seg.arr)
        # print(rig.arr)

        for j in range(add_or_update_times):
            num1 = int(random.random() * big_n) + 1
            num2 = int(random.random() * big_n) + 1
            big_l = min(num1, num2)
            big_r = max(num1, num2)
            c = int(random.random() * max_v) + 1
            # if random.random() < 0.5:
            # seg.add(big_l, big_r, c, big_s, big_n, root)
            # rig.add(big_l, big_r, c)
            # else:
            seg.tree_update(big_l, big_r, c, big_s, big_n, root)
            rig.update(big_l, big_r, c)
        for k in range(query_times):
            num1 = int(random.random() * big_n) + 1
            num2 = int(random.random() * big_n) + 1
            big_l = min(num1, num2)
            big_r = max(num1, num2)
            ans1 = seg.query(big_l, big_r, big_s, big_n, root)
            ans2 = rig.query(big_l, big_r)
            if ans1 != ans2:
                print(ans1)
                print(ans2)
                return False
    return True


if __name__ == '__main__':
    # origin = [2, 1, 1, 2, 3, 4, 5]
    # seg = SegmentTree(origin)
    # big_s = 1  # 整个区间的开始位置，规定从1开始，不从0开始 -> 固定
    # big_n = len(origin)  # 整个去见的结束位置，规定能到N， 不是 N-1 -> 固定
    # root = 1  # 整棵树的头节点位置，规定是1，不是0  -> 固定
    # big_l = 2  # 操作区间的开始位置 -> 可变
    # big_r = 5  # 操作区间的结束位置 -> 可变
    # c = 4  # 要加或者要更新的数字 -> 可变
    # # 区间生成，必须在【big_s, big_n]整个范围上build
    # seg.build(big_s, big_n, root)
    # # 区间修改，可以改变big_l, big_r和c的值， 其他值不可改变
    # seg.add(big_l, big_r, c, big_s, big_n, root)
    # # 区间更新，可以改变big_l, big_r和c的值， 其他值不可改变
    # seg.tree_update(big_l, big_r, c, big_s, big_n, root)
    # # 区间查询，可以改变big_l和big_r值， 其他值不可改变
    # ans = seg.query(big_l, big_r, big_s, big_n, root)
    # print(ans)

    print("对数器测试开始 ... ")
    # test()
    print("测试结果 ：" + ("通过" if test() else "未通过"))
    a = [None] * 8
    print(a)
    a[2] = True
    print(a)