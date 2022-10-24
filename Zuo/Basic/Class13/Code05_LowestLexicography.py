# -*- coding: utf-8 -*-

"""
@File: Code05_LowestLexicography.py
@Author: Sarah Shen
@Time: 23/10/2022 00:24
"""


# 贪心算法
# 1. 最自然智慧的算法
# 2. 用一种局部最功利的标准，总是做出在当前看来是最好的选择
# 3. 难点在于证明局部最功利的标准可以得到全局最优解
# 4. 对于贪心算法的学习主要以增加阅历和经验为主

# 给定一个字符串组成的数组
# 必须把所有字符拼接起来
# 返回所有可能的拼接结果中，字典序最小的结果

# 字典序，字符串排序：
#

# 先提出贪心策略，不要去证明贪心策略的结果是否正确，直接用对数器判断对错
# 面试场上先提出用对数器的方式去验证，再说玩一玩证明


def lowest_string1(strs):
    if strs is None or len(strs) == 0:
        return ""
    ans = process(strs)
    ans.sort(key=cmp_to_key(my_comparator))
    return ans[0]


def process(strs):
    """ strs中所有字符串全排列，返回所有可能的结果 """
    ans = list()
    if len(strs) == 0:
        ans.append('')
        return ans
    for i in range(len(strs)):
        first = strs[i]
        nexts = remove_index_string(strs, i)
        next_strs = process(nexts)
        for cur in next_strs:
            ans.append(first + cur)
    return ans


def remove_index_string(arr, index: int):
    ans = [""] * (len(arr) - 1)
    ans_index = 0
    for i in range(len(arr)):
        if i != index:
            ans[ans_index] = arr[i]
            ans_index += 1
    return ans


def my_comparator(a: str, b: str):
    if (a + b) < (b + a):
        ans = -1
    elif (a + b) == (b + a):
        ans = 0
    else:
        ans = 1
    return ans


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


def lowest_string2(strs):
    if strs is None or len(strs) == 0:
        return ""
    strs.sort(key=cmp_to_key(my_comparator))
    res = ""
    for s in strs:
        res += s
    return res


if __name__ == '__main__':
    a_list = ['abc', 'cks', 'ft']
    b_list = ['b', 'ba']

    print(lowest_string2(a_list))
    print(lowest_string2(b_list))

    print()
    print(lowest_string1(a_list))
    print(lowest_string1(b_list))
