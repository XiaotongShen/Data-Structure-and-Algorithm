# -*- coding: utf-8 -*-

"""
@File: Code01_Light.py
@Author: Sarah Shen
@Time: 23/10/2022 00:24
"""


def min_light2(road):
    road_list = list(road)
    i = 0
    light = 0
    while i < len(road_list):
        if road_list[i] == 'X':
            i += 1
        else:
            light += 1
            if i + 1 == len(road_list):
                break
            else:
                if road_list[i + 1] == 'X':
                    i += 2
                else:
                    i += 3
    return light


# 更简洁的解法
# 两个X之间，数一下.的数量，然后除以3，向上取整
# 把等数累加
def min_light3(road):
    road_list = list(road)
    cur = 0
    light = 0
    for r in road_list:
        if r == 'X':
            light += int((cur + 1) / 3)
            cur = 0
        else:
            cur += 1
    light += int((cur + 2) / 3)
    return light


if __name__ == '__main__':
    a = 'abc'
    b = list(a)
    print(b)
