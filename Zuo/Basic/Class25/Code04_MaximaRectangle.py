# -*- coding: utf-8 -*-

"""
@File: Code04_MaximaRectangle.py
@Author: Sarah Shen
@Time: 31/10/2022 22:47
"""


# 测试链接：https://leetcode.com/problems/maximal-rectangle/
class Solution:

    # def maximalRectangle(self, matrix: List[List[str]]) -> int:
    def maximal_rectangle(self, matrix: [[str]]):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        max_area = 0
        height = [0] * (len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                height[j] = 0 if matrix[i][j] == '0' else height[j] + 1
            max_area = max(self.max_rec_from_bottom(height), max_area)
        return max_area

    @staticmethod
    def max_rec_from_bottom(height: [int]):
        if height is None or len(height) == 0:
            return
        max_area = 0
        s = list()
        for i in range(len(height)):
            while len(s) != 0 and height[s[-1]] >= height[i]:
                j = s.pop()
                k = -1 if len(s) == 0 else s[-1]
                cur_area = (i - k - 1) * height[j]
                max_area = max(max_area, cur_area)
            s.append(i)
        while len(s) != 0:
            j = s.pop()
            k = -1 if len(s) == 0 else s[-1]
            cur_area = (len(height) - k - 1) * height[j]
            max_area = max(max_area, cur_area)
        return max_area
