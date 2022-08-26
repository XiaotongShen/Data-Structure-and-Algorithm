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
# x以固定不等概率，返回0和1
def x():
    if random.random() < 0.84:
       return 0
    else:
        return 1

# 验证x()
# testTimes = 1000000
# count = 0
#
# for i in range(testTimes):
#     if h() == 0:
#         count += 1
# print(count/testTimes)


# 构建y，以等概率返回0和1：
def y():
    a = x()
    while a == x():
        a = x()
    return a

# 验证y()
testTimes = 1000000
count = 0

for i in range(testTimes):
    if y() == 0:
        count += 1
print(count/testTimes)

# 本质上，所有数字都是二进制拼的，要练习