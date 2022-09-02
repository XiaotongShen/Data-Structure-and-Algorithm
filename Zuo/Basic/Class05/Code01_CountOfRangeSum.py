# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/9/1.
Author: 
    Sarah Shen
Date: 
    2022/9/1
"""


# LC题目： https://leetcode.com/problems/count-of-range-sum/

class CountOfRangeSum:

    def count_range_sum(self, nums: list, lower: int, upper: int):
        if nums is None or len(nums) == 0:
            return 0
        else:
            sums = [0] * len(nums)
            sums[0] = nums[0]
            for i in range(1, len(nums)):
                sums[i] = sums[i - 1] + nums[i]
            return self.process(sums, 0, len(sums) - 1, lower, upper)

    def process(self, sums: list, left: int, right: int, lower: int, upper: int):
        if left == right:
            return 1 if lower <= sums[left] <= upper else 0
        else:
            mid = left + ((right - left) >> 1)
            return \
                self.process(sums, left, mid, lower, upper) + \
                self.process(sums, mid + 1, right, lower, upper) + \
                self.merge(sums, left, mid, right, lower, upper)

        # @staticmethod
        # def merge(arr: list, left: int, mid: int, right: int, lower: int, upper: int):
        #     # cal part of merge
        #     ans = 0
        #     window_left = left
        #     window_right = left
        #     for i in range(mid + 1, right + 1):
        #         lower_new = arr[i] - upper
        #         upper_new = arr[i] - lower
        #         while window_right <= mid and arr[window_right] <= upper_new:
        #             window_right += 1
        #         while window_left <= mid and arr[window_left] < lower_new:
        #             window_left += 1
        #         ans += window_right - window_left
        #     # sort part of merge
        #     ast = []
        #     p1 = left
        #     p2 = mid + 1
        #     while p1 <= mid and p2 <= right:
        #         if arr[p1] <= arr[p2]:
        #             ast.append(arr[p1])
        #             p1 += 1
        #         else:
        #             ast.append(arr[p2])
        #             p2 += 1
        #     while p1 <= mid:
        #         ast.append(arr[p1])
        #         p1 += 1
        #     while p2 <= right:
        #         ast.append(arr[p2])
        #         p2 += 1
        #     for i in range(len(ast)):
        #         arr[left + i] = ast[i]
        #     return ans

    @staticmethod
    def merge(arr: list, left: int, mid: int, right: int, lower: int, upper: int):
        # cal part of merge
        ans = 0
        window_left = left
        window_right = left
        for i in range(mid + 1, right + 1):
            lower_new = arr[i] - upper
            upper_new = arr[i] - lower
            while window_right <= mid and arr[window_right] <= upper_new:
                window_right += 1
            while window_left <= mid and arr[window_left] < lower_new:
                window_left += 1
            ans += window_right - window_left
        # sort part of merge
        ast = [0] * (right - left + 1)
        i = 0
        p1 = left
        p2 = mid + 1
        while p1 <= mid and p2 <= right:
            if arr[p1] <= arr[p2]:
                ast[i] = (arr[p1])
                p1 += 1
            else:
                ast[i] = (arr[p2])
                p2 += 1
            i += 1
        while p1 <= mid:
            ast[i] = (arr[p1])
            p1 += 1
            i += 1
        while p2 <= right:
            ast[i] = (arr[p2])
            p2 += 1
            i += 1
        for j in range(len(ast)):
            arr[left + j] = ast[j]
        return ans


if __name__ == '__main__':
    # a = [10, 20, 30, 40, 50, 60, 70, 80]
    a = [10] * 8
    c = CountOfRangeSum()
    print(c.count_range_sum(a, 40, 60))
