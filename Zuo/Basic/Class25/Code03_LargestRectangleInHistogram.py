# -*- coding: utf-8 -*-

"""
@File: Code03_LargestRectangleInHistogram.py
@Author: Sarah Shen
@Time: 31/10/2022 22:47
"""


# 测试链接：https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:

    # def largestRectangleArea(self, heights: List[int]) -> int:
    @staticmethod
    def largest_rectangle_area1(heights: [int]):
        if heights is None or len(heights) == 0:
            return 0
        max_area = 0
        s = list()
        for i in range(len(heights)):
            while len(s) != 0 and heights[s[-1]] >= heights[i]:
                j = s.pop()
                k = -1 if len(s) == 0 else s[-1]
                cur_area = (i - k - 1) * heights[j]
                max_area = max(max_area, cur_area)
            s.append(i)
        while len(s) != 0:
            j = s.pop()
            k = -1 if len(s) == 0 else s[-1]
            cur_area = (len(heights) - k - 1) * heights[j]
            max_area = max(max_area, cur_area)
        return max_area


