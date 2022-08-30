# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/29.
Author: 
    Sarah Shen
Date: 
    2022/8/29
"""
import random
# 生成符合要求的数组 1 <= K < M
# 生成用于比较的算法过程
# 大量随机生成数组，以进行算法过程检验


class Test:
    """ 算法的对数器，随机生成数组，比较两个不同的算法过程结果是否一致 """

    def main(self, times: int, max_kinds: int, max_val: int, func):
        succeed = True
        ma = 9
        for i in range(times):
            a = int(random.random() * ma) + 1
            b = int(random.random() * ma) + 1
            k = min(a, b)
            m = max(a, b)
            while k == m:
                m += 1
            arr = self.generate_random_array(max_kinds=max_kinds, max_val=max_val, k=k, m=m)
            ans1 = func(arr, k, m)
            ans2 = self.comparator(arr, k, m)

            if ans1 != ans2:
                succeed = False
                print(arr)
                print(ans1, ans2)
                break
        print("Nice!" if succeed else "Oops, Something is Wrong!")

    @staticmethod
    def generate_random_array(max_kinds: int, max_val: int, k: int, m: int):
        # 随机生成的种类个数，最少2类
        num_kinds = int(random.random() * max_kinds) + 2
        # 定义符合条件的数组
        arr = [0] * (k + (num_kinds - 1) * m)

        # 任务初始化
        index = 0   # 初始化arr的index
        ast = []    # 初始化辅助数组，用于保存所有已生成的数字类

        # 生成真命天子
        k_times_num = int(random.random() * max_val)
        # 保存真命天子到辅助数组
        ast.append(k_times_num)
        # 填充k次真命天子
        for i in range(k):
            arr[index] = k_times_num
            index += 1
        num_kinds -= 1
        # print(ast)
        # print(arr)

        # 填充所有的非真命天子，每个值m次
        while num_kinds != 0:
            # 生成其他数类
            m_times_num = int(random.random() * max_val)
            # 如果已存在，重新生成
            while m_times_num in ast:
                m_times_num = int(random.random() * max_val)
            # 保存新数类到辅助数组
            ast.append(m_times_num)
            # 填充m次其他数类
            for i in range(m):
                arr[index] = m_times_num
                index += 1
            num_kinds -= 1
            # print(ast)
            # print(arr)

        # 将数组内容随机排序
        for i in range(len(arr)):
            j = int(random.random() * len(arr))
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
        # print(arr)
        return arr

    @staticmethod
    def comparator(arr: list, k: int, m: int):
        """ 使用哈希表实现的查找出现k次的数 """
        ast = {}
        for num in arr:
            if num in ast.keys():
                ast[num] += 1
            else:
                ast[num] = 1
        for key in ast.keys():
            if ast[key] == k:
                return key


# 一个更简洁的Solution
def km(arr: list, k: int, m: int):
    """ 数组中只有一种数出现了k次，其他所有数均出现了m次，请找出出现了k次的数(精简版) """
    ast = [0] * 32
    for num in arr:
        for i in range(32):
            ast[i] += (num >> i) & 1
    ans = 0
    for i in range(32):
        ast[i] %= m
        if ast[i] != 0:
            ans |= 1 << i
    return ans


# 此处用于理解简洁算法的位运算过程
# def km(arr: list, k: int, m: int):
#     """ 数组中只有一种数出现了k次，其他所有数均出现了m次，请找出出现了k次的数 """
#     ast = [0] * 32  # 定义一个长度为32的数组（位图）
#     for num in arr:
#         # print(num)
#         # print_bin_32(num)
#         for i in range(32):
#             ast[i] += (num >> i) & 1    # 判断num的第i位是否为1，若为1，则在ast的第i位加上1
#         # print(ast)
#         # print('\n')
#     ans = 0
#     print(ast)
#     print(m)
#     for i in range(32):
#         ast[i] %= m  # ast按位整除m, 若整除余数不为0，则表示代表出现了k次的数在余数不为0的位上是1
#         if ast[i] != 0:
#             ans |= 1 << i   # 将余数不为零的位置上填上1，返回值
#             print('i: %i' % i)
#             print_bin_32(ans)
#     print(ast)
#     return ans
#
# def print_bin_32(x: int):
#     """  打印整数的32位二进制表示 """
#     print(x, format(x, '032b'))


if __name__ == '__main__':
    # 单一样本检验算法过程
    arr = [55, 799, 8, 19, 72, 799, 8, 19, 72, 799, 8, 19, 72, 799, 8, 19, 72, 55, 55]
    k = 3
    m = 4
    # print(km(arr=arr, k=3, m=4))

    # 对数器检验算法过程
    test = Test()
    test.main(times=100000, max_kinds=5, max_val=100, func=km)
