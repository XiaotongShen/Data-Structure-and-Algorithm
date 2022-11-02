# -*- coding: utf-8 -*-

"""
@File: Code05_CountSubmatricesWithAllOnes.py
@Author: Sarah Shen
@Time: 31/10/2022 22:47
"""


# 测试链接：https://leetcode.com/problems/count-submatrices-with-all-ones
class Solution:

    # def numSubmat(self, mat: List[List[int]]) -> int:
    def num_sum_mat(self, mat: [[int]]):
        if mat is None or len(mat) == 0 or len(mat[0]) == 0:
            return 0
        nums = 0
        height = [0] * len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                height[j] = 0 if mat[i][j] == 0 else height[j] + 1
            nums += self.count_from_bottom(height)
        return nums

    def count_from_bottom(self, height: [int]):
        if height is None or len(height) == 0:
            return 0
        nums = 0
        s = list()
        for i in range(len(height)):
            while len(s) != 0 and height[s[-1]] >= height[i]:
                j = s.pop()
                if height[j] > height[i]:
                    left = -1 if len(s) == 0 else s[-1]
                    n = i - left - 1
                    down = max(height[i], 0 if left == -1 else height[left])
                    nums += (height[j] - down) * self.num(n)
            s.append(i)
        while len(s) != 0:
            j = s.pop()
            left = -1 if len(s) == 0 else s[-1]
            n = len(height) - left - 1
            down = 0 if left == -1 else height[left]
            nums += (height[j] - down) * self.num(n)
        return nums

    @staticmethod
    def num(n: int):
        return (n * (1 + n)) >> 1
