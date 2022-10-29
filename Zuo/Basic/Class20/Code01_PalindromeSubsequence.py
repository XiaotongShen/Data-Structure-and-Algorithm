# -*- coding: utf-8 -*-

"""
@File: Code01_PalindromeSubsequence.py
@Author: Sarah Shen
@Time: 29/10/2022 13:23
"""


# 测试链接：https://leetcode.com/problems/longest-palindromic-subsequence/
class Solution1:

    # def longestPalindromeSubseq(self, s: str) -> int:
    def longest_palindrome_subseq1(self, s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        ss = list(s)
        return self.f(ss, 0, len(ss) - 1)

    def f(self, ss: list, left: int, right: int):
        if left == right:
            return 1
        if left == right - 1:
            return 2 if ss[left] == ss[right] else 1
        p1 = self.f(ss, left + 1, right - 1)
        p2 = self.f(ss, left + 1, right)
        p3 = self.f(ss, left, right - 1)
        p4 = 0 if ss[left] != ss[right] else 2 + self.f(ss, left + 1, right - 1)
        return max(max(p1, p2), max(p3, p4))


class Solution:

    # def longestPalindromeSubseq(self, s: str) -> int:
    @ staticmethod
    def longest_palindrome_subseq2(s: str) -> int:
        if s is None or len(s) == 0:
            return 0
        ss = list(s)
        n = len(ss)
        # 定义动态规划表
        dp = [[0] * n for i in range(n)]
        # 初始化动态规划表
        # 当L小于R时，不考虑，所以表左下角均不考虑
        # 当L==R时，最长回文子序列长度为1，
        # 当L==R-1时，最长回文子序列长度为1或2（当L和R位置上的字符一样的时候）
        dp[n - 1][n - 1] = 1
        for i in range(n - 1):
            dp[i][i] = 1
            dp[i][i + 1] = 2 if ss[i] == ss[i + 1] else 1
        # 此时对角线上的值，与独角线右上一条对角线的值已经填完了
        # 接下来填其他位置
        for l in range(n - 3, -1, -1):
            for r in range(l + 2, n):
                dp[l][r] = max(dp[l][r - 1], dp[l + 1][r])
                if ss[l] == ss[r]:
                    dp[l][r] = max(dp[l][r], 2 + dp[l + 1][r - 1])
        return dp[0][n - 1]
