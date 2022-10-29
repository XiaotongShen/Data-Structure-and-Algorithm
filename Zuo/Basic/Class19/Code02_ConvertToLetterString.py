# -*- coding: utf-8 -*-

"""
@File: Code02_ConvertToLetterString.py
@Author: Sarah Shen
@Time: 26/10/2022 10:05
"""
import random


# str只含有数字字符0~9，可以转化成字母，例如‘111’ 可以转化成三种字符串‘AAA’, 'AK', 'kA'
# 返回多少种转化方案
# 递归解法
def number(s: str):
    if s is None or len(s) == 0:
        return 0
    return process(list(s), 0)


def process(s_list: list, i: int):
    """ 将s_list从i位置开始转化，有多少种可能方案 """
    if i == len(s_list):
        return 1
        # i没有到最后，说明还有字符没有转换完成
    if s_list[i] == '0':
        # 之前的决定有问题
        return 0
    # s_list[i] != '0':
    # 可能性1，i单独转换成字母
    ways = process(s_list, i + 1)
    # 可能性2， i和i+1一起转换
    if i + 1 < len(s_list) and (str_to_int(s_list[i]) * 10 + str_to_int(s_list[i + 1])) < 27:
        ways += process(s_list, i + 2)
    return ways


# 从右往左的动态规划
# 就是上面方法的动态规划版本
# dp[i]表示，s_list[i]有多少种转化方式
def dp1(s: str):
    if s is None or len(s) == 0:
        return 0
    s_list = list(s)
    n = len(s_list)
    dp = [0] * (n + 1)
    dp[n] = 1
    for i in range(n - 1, -1, -1):
        if s_list[i] != '0':
            ways = dp[i + 1]
            if i + 1 < len(s_list) and str_to_int(s_list[i]) * 10 + str_to_int(s_list[i + 1]) < 27:
                ways += dp[i + 2]
            dp[i] = ways

    return dp[0]


# 从左往右的动态规划
# dp[i]表示：str[0,..., i]有多少种转化方式
# TODO
def dp2(s: str):
    if s is None or len(s) == 0:
        return 0
    s_list = list(s)
    n = len(s_list)
    if s_list[0] == '0':
        return 0
    dp = [0] * n
    dp[0] = 1
    for i in range(n):
        if s_list[i] == '0':
            # 如果s_list[i]==‘0’,那么他是一定要和前面一个字符一起拼的，
            # 那么就要求前一个字符不能也是‘0’，否则拼不了
            # 前面一个字符不是‘0’就够了吗，不够，还得要求拼完了要么是10， 要么是20，如果更大的话，拼不了
            # 这就够了吗？不够，拼完了，还得要求s_list[0, i-2]真的可以被费解
            # 如果[0,..., i-2]都不存在分解方案，那i和i-1拼成了也不行，因为之前的搞不定
            if s_list[i - 1] == '0' or s_list[i - 1] > '2' or (i - 2 >= 0 and dp[i - 2] == 0):
                return 0
            else:
                dp[i] = dp[i - 2] if i - 2 >= 0 else 1
        else:
            dp[i] = dp[i - 1]
            if s_list[i - 1] != '0' and str_to_int(s_list[i - 1]) * 10 + str_to_int(s_list[i]) <= 26:
                dp[i] += dp[i - 2] if i - 2 >= 0 else 1
    return dp[n - 1]


def random_string(length: int):
    s = ''
    for i in range(length):
        s = s + str(int(random.random() * 10))
    return s


def str_to_int(o: str):
    return ord(o) - ord('0')


if __name__ == '__main__':
    max_len = 30
    test_time = 10000
    print('测试开始')
    for i in range(test_time):
        str_len = int(random.random() * max_len)
        string = random_string(str_len)
        ans0 = number(string)
        ans1 = dp1(string)
        # ans2 = dp2(string)
        if ans0 != ans1: # or ans0 != ans2:
            print(string)
            print(ans0)
            print(ans1)
            # print(ans2)
            print('Oops!')
            break
    print('测试结束')
