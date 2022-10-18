# -*- coding: utf-8 -*-

"""
@File: Code01_CoverMax.py
@Author: Sarah Shen
@Time: 18/10/2022 15:32
"""
import sys
from queue import PriorityQueue


def max_cover_1(lines: [list]):
    min_value = sys.maxsize
    max_value = -sys.maxsize - 1
    for i in range(len(lines)):
        # print(i, min_value, max_value)
        min_value = min(min_value, lines[i][0])
        max_value = max(max_value, lines[i][1])
    cover = 0
    for i in range(min_value, max_value):
        p = i + 0.5
        cur = 0
        for j in range(len(lines)):
            if lines[j][0] < p < lines[j][1]:
                cur += 1
        cover = max(cover, cur)
    return cover


class Line:
    def __init__(self, s: int, e: int):
        self.start = s
        self.end = e


def end_comparator(o1: Line, o2: Line):
    return o1.end - o2.end


def start_comparator(o1: list, o2: list):
    return o1[0] - o2[0]


def cmp_to_key(mycmp):
    """
    Convert a cmp= function into a key= function
    """

    class K:
        def __init__(self, obj):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


def max_cover_2(m: [list]):
    lines = [Line(0, 0)] * len(m)
    for i in range(len(m)):
        lines[i] = Line(m[i][0], m[i][1])
    lines.sort(key=cmp_to_key(end_comparator))
    # 小根堆，每一条线段的结尾数值，使用默认的
    heap = PriorityQueue()
    cover = 0
    for i in range(len(lines)):
        # lines[i] -> cur 在黑盒中，把 <= cur.start 的东西都弹出
        while not heap.empty() and heap.queue[0] <= lines[i].start:
            heap.get()
        heap.put(lines[i].end)
        cover = max(cover, heap.qsize())

    return cover


def max_cover_3(m: [list]):
    # m是二维数组，可以认为m内部是一个个的一维数组
    # 每一个一维数组就是一个对象，也就是线段
    # 如下的code，就是根据每一个线段的开始位置排序
    m.sort(key=cmp_to_key(start_comparator))
    # 准备好小根堆
    heap = PriorityQueue()
    cover = 0
    for line in m:
        while not heap.empty() and heap.queue[0] <= line[0]:
            heap.get()
        heap.put(line[1])
        cover = max(cover, heap.qsize())
    return cover


if __name__ == "__main__":
    ls = [[1, 3], [2, 4], [2, 6], [3, 7], [5, 7], [5, 8], [5, 9]]
    print(max_cover_1(ls))
    print(max_cover_2(ls))
    print(max_cover_3(ls))
