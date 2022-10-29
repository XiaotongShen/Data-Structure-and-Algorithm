# -*- coding: utf-8 -*-

"""
@File: Code04_LongestCommonSubsequence.py
@Author: Sarah Shen
@Time: 26/10/2022 10:05
"""


# 这个问题leetcode上可以直接测
# 链接：https://leetcode.com/problems/longest-common-subsequence/
class Solution1:

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    def longest_common_subsequence1(self, text1: str, text2: str) -> int:
        if text1 is None or text2 is None or len(text1) == 0 or len(text2) == 0:
            return 0
        str1 = list(text1)
        str2 = list(text2)
        return self.process1(str1, str2, len(str1) - 1, len(str2) - 1)

    def process1(self, str1: list, str2: list, i: int, j: int):
        if i == 0 and j == 0:
            return 1 if str1[i] == str2[j] else 0
        elif i == 0:
            if str1[i] == str2[j]:
                return 1
            else:
                return self.process1(str1, str2, i, j - 1)
        elif j == 0:
            if str1[i] == str2[j]:
                return 1
            else:
                return self.process1(str1, str2, i - 1, j)
        else:
            p1 = self.process1(str1, str2, i - 1, j)
            p2 = self.process1(str1, str2, i, j - 1)
            p3 = (1 + self.process1(str1, str2, i - 1, j - 1)) if str1[i] == str2[j] else 0
            return max(p1, max(p2, p3))


class Solution2:

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    @staticmethod
    def longest_common_subsequence2(text1: str, text2: str) -> int:
        if text1 is None or text2 is None or len(text1) == 0 or len(text2) == 0:
            return 0
        str1 = list(text1)
        str2 = list(text2)
        n = len(str1)
        m = len(str2)
        dp = [[0] * m for i in range(n)]
        dp[0][0] = 1 if str1[0] == str2[0] else 0
        for j in range(1, m):
            dp[0][j] = 1 if str1[0] == str2[j] else dp[0][j - 1]
        for i in range(1, n):
            dp[i][0] = 1 if str1[i] == str2[0] else dp[i - 1][0]
        for i in range(1, n):
            for j in range(1, m):
                p1 = dp[i - 1][j]
                p2 = dp[i][j - 1]
                p3 = (1 + dp[i - 1][j - 1]) if str1[i] == str2[j] else 0
                dp[i][j] = max(p1, max(p2, p3))
        return dp[n - 1][m - 1]
