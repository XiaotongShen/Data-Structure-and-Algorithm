# -*- coding: utf-8 -*-

"""
@File: Code03_Coffee.py
@Author: Sarah Shen
@Time: 29/10/2022 13:23
"""
from queue import PriorityQueue
import random


# 题目
# 数组arr代表每一个咖啡机冲一杯咖啡的时间，每个咖啡机只能串行的制造咖啡
# 现在有那个人需要和咖啡，只能用咖啡机来制造咖啡
# 认为每个人喝咖啡的时间非常短，冲好的时间即喝完的时间
# 每个人喝完之后咖啡杯可以选择洗或者自然挥发干净，只有一台洗咖啡杯的机器，只能串行的洗咖啡杯
# 洗杯子的机器洗完一个杯子时间为a，任何一个杯子自然挥发干净的时间为b
# 四个参数：arr, n, a, b
# 假设时间点从0开始，返回所有人喝完咖啡并洗完咖啡杯的全部过程结束后，至少来到什么时间点


# 贪心，暴力递归
def min_time1(arr: list, n: int, a: int, b: int):
    heap = PriorityQueue()
    for i in range(len(arr)):
        # 将三个值的tuple放入小根堆:(当前做完一杯咖啡到达的时间点，当前可以开始做咖啡的时间点，做一杯咖啡需要的时间)
        # 以做完咖啡的时间排序做小根堆
        heap.put((0 + arr[i], 0, arr[i]))
    drinks = [0] * n  # n个人喝完咖啡的时间,初始化
    for i in range(n):
        cur = heap.get()  # 堆顶弹出一个最快做出咖啡的咖啡机
        drinks[i] = cur[0]  # 将咖啡完成的时间计入i号客人喝完咖啡的时间
        cur_updated = (cur[0] + cur[2], cur[1] + cur[2], cur[2])  # 咖啡机当前完成的时间 ++; 咖啡机当前可用的时间 ++
        heap.put(cur_updated)  # 将更新后的咖啡机重新压入小根堆，依次直到所有客人服务完
    # 以上获得了每个客人喝完咖啡的时间
    return best_time(drinks, a, b, 0, 0)


def best_time(drinks: list, wash: int, air: int, idx: int, free: int):
    """
    drinks: 所有杯子可以开始洗的时间
    wash: 单杯洗干净的时间（串行）
    air：挥发干净的时间（并行）
    free: 洗的机器什么时候可以用
    drinks[index...]都变干净，最早结束的时间（返回值）
    """
    if idx == len(drinks):
        # 如果当前已经超过了最后一个index（len(drinks）-1)
        return 0
    # idx号杯子决定洗
    self_clean1 = max(drinks[idx], free) + wash
    rest_clean1 = best_time(drinks, wash, air, idx + 1, self_clean1)
    p1 = max(self_clean1, rest_clean1)
    # idx号杯子决定挥发
    self_clean2 = drinks[idx] + air  # 咖啡喝完即可挥发，需要时间air
    rest_clean2 = best_time(drinks, wash, air, idx + 1, free)
    p2 = max(self_clean2, rest_clean2)
    return min(p1, p2)


# 贪心 + 优良尝试改成动态规划
def min_time2(arr: list, n: int, a: int, b: int):
    """
    arr: 咖啡机做出一杯咖啡所用的时间
    n: 排队的人数
    a: 洗咖啡杯的用时(串行）
    b: 自然烘干咖啡杯的用时（并行）
    """
    heap = PriorityQueue()
    for i in range(len(arr)):
        heap.put((0 + arr[i], 0, arr[i]))
    drinks = [0] * n
    for i in range(n):
        cur = heap.get()
        drinks[i] = cur[0]
        cur_updated = (cur[0] + cur[2], cur[1] + cur[2], cur[2])
        heap.put(cur_updated)
    return best_time_dp(drinks, a, b)


def best_time_dp(drinks: list, wash: int, air: int):
    n = len(drinks)
    max_free = 0
    # 杯子的个数有限，但是可用的时间无限，以下首先用最差的情况限定free的边界
    for i in range(len(drinks)):
        # 对于机器的空闲时间free，最差的情况是所有的杯子都洗，要同时满足咖啡喝完和机器空闲两个条件，
        # 所以是咖啡喝完drinks[i] 与机器空闲时间max_free的最大值，再加上洗杯子的时间
        max_free = max(max_free, drinks[i]) + wash
    dp = [[0] * (max_free + 1) for i in range(n + 1)]  # 定义表
    # 依赖关系是idx 依赖idx +1， 所以从n-1开始填表
    for idx in range(n - 1, -1, -1):
        for free in range(max_free):
            # idx号杯子决定洗
            self_clean1 = max(drinks[idx], free) + wash
            if self_clean1 > max_free:
                break
            rest_clean1 = dp[idx + 1][self_clean1]
            p1 = max(rest_clean1, self_clean1)
            # idx号杯子决定挥发
            self_clean2 = drinks[idx] + air
            rest_clean2 = dp[idx + 1][free]
            p2 = max(self_clean2, rest_clean2)
            dp[idx][free] = min(p1, p2)

    return dp[0][0]


def random_array(arr_l: int, max_v: int):
    a = [0] * arr_l
    for i in range(arr_l):
        a[i] = int(random.random() * max_v) + 1
    return a


if __name__ == '__main__':
    arr_len = 10
    max_value = 10
    test_time = 10
    print('测试开始')
    for i in range(test_time):
        arr = random_array(arr_len, max_value)
        n = int(random.random() * 7) + 1
        a = int(random.random() * 7) + 1
        b = int(random.random() * 10) + 1
        ans1 = min_time1(arr, n, a, b)
        ans2 = min_time2(arr, n, a, b)
        if ans1 != ans2:
            print(arr)
            print("n : %s" % n)
            print("a : %s" % a)
            print("b : %s" % b)
            print(str(ans1) + ' , ' + str(ans2))
            print('==================')
            break
    print('测试结束')
