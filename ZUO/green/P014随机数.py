# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/6/30.
Author: 
    Sarah Shen
Date: 
    2022/6/30
"""

import random

# ans = random.random()
# print(ans)

# testTimes = 10000000
# count = 0
# for i in range(testTimes):
#     if random.random() < 0.75:
#         count += 1
#     else:
#         pass
# print(count/testTimes)



# testTimes = 10000000
# count = 0
# for i in range(testTimes):
#     if random.random() * 8 < 5:
#         count += 1
#     else:
#         pass
# print(count/testTimes)
# print(5/8)

#
# K = 9
# # [0, K) -> [0,8]
# counts = [0,0,0,0,0,0,0,0,0]
#
# testTimes = 1000000
# for i in range(testTimes):
#     ans = int(random.random() * K)
#     counts[ans] += + 1
#
# n = len(counts)
# for i in range(n):
#     print(str(i)+"这个数，出现了 "+str(counts[i])+" 次")


# import math
#
# def xToXPower2():
#     return max(random.random(), random.random())
#
# def xToXPower3():
#     return max(random.random(), random.random(), random.random())
#
# x = 0.7
# testTimes = 1000000
# count = 0
# for i in range(testTimes):
#     if xToXPower2() < x:
#         count += 1
#     else:
#         pass
# print(count/testTimes)
# print(math.pow(x, 2))
#
# count = 0
# for i in range(testTimes):
#     if xToXPower3() < x:
#         count += 1
#     else:
#         pass
# print(count/testTimes)
# print(math.pow(x, 3))


import math

def xToXPower2():
    return min(random.random(), random.random())

x = 0.7
testTimes = 1000000
count = 0
for i in range(testTimes):
    if xToXPower2() < x:
        count += 1
    else:
        pass
print(count/testTimes)
print(1-math.pow((1-x), 2))




