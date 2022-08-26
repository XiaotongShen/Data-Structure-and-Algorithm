# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/7/1.
Author: 
    Sarah Shen
Date: 
    2022/7/1
"""


import random

# lib里的，不能改！有一个1-5等概率返回一个的函数
def f1():
    """
    1-5 等P的随机
    :return:
    """
    return int(random.random()*5) +1

# 随机机制，智能用f1
# 等概率返回0和1
def f2():
    """
    0,1 等P发生器
    :return:
    """
    ans = f1()
    while ans == 3:
        ans = f1()
    if ans < 3:
        r = 0
    else:
        r = 1
    return r
# 验证f2()
# testTimes = 100000
# count = 0
# for i in range(testTimes):
#     if f2() == 0:
#         count += 1
# print(count/testTimes)


# 1-7 的随机
# 0-6 的随机
# 需要3个二进制位
def f3():
    ans = (f2() << 2) + (f2() << 1) + (f2() << 0)
    return ans

# 验证f3()
# testTimes = 100000
# counts = [0,0,0,0,0,0,0,0]
# for i in range(testTimes):
#     num = f3()
#     counts[num] += 1
# n = len(counts)
# for i in range(n):
#     print(str(i)+"这个数，出现了 "+str(counts[i])+" 次")


def f4():
    ans = f3()
    while ans == 0:
        ans = f3()
    return ans

# 验证f3()
testTimes = 100000
counts = [0,0,0,0,0,0,0,0]
for i in range(testTimes):
    num = f4()
    counts[num] += 1
n = len(counts)
for i in range(n):
    print(str(i)+"这个数，出现了 "+str(counts[i])+" 次")

# a = 1
# b = 0
# print(a)
# print(a << 2)
# print(a << 1)
# print(a << 0)
# print(b)
# print(b << 2)
# print(b << 1)
# print(b << 0)
# print((b << 2) + (b << 1) + (b << 0))
# print((b << 2) + (b << 1) + (a << 0))
# print((b << 2) + (a << 1) + (b << 0))
# print((b << 2) + (a << 1) + (a << 0))
# print((a << 2) + (b << 1) + (b << 0))
# print((a << 2) + (b << 1) + (a << 0))
# print((a << 2) + (a << 1) + (b << 0))
# print((a << 2) + (a << 1) + (a << 0))




