# -*- coding: utf-8 -*-

"""
@File: Code03_StickersToSpellWord.py
@Author: Sarah Shen
@Time: 26/10/2022 10:05
"""
import sys


# 本题测试链接：https://leetcode.com/problems/stickers-to-spell-word
class Solution1:
    # def minStickers(self, stickers: List[str], target: str) -> int:
    def min_stickers1(self, stickers: list, target: str):
        ans = self.process1(stickers, target)
        return -1 if ans == sys.maxsize else ans

    # 所有贴纸stickers，每一种贴纸都有无穷张
    # target 目标字符串
    # 最少张数
    def process1(self, stickers: list, target: str):
        if len(target) == 0:
            return 0
        min_num = sys.maxsize
        for first in stickers:
            rest = self.minus(target, first)
            if len(rest) != len(target):
                min_num = min(min_num, self.process1(stickers, rest))
        return min_num + (0 if min_num == sys.maxsize else 1)

    def minus(self, s1: str, s2: str):
        str1 = list(s1)
        str2 = list(s2)
        count = [0] * 26
        for cha in str1:
            count[self.cha_to_int(cha)] += 1
        for cha in str2:
            count[self.cha_to_int(cha)] -= 1
        builder = ''
        for i in range(26):
            if count[i] > 0:
                for j in range(count[i]):
                    builder += self.int_to_cha(i)
        return builder

    @staticmethod
    def cha_to_int(cha: str):
        return ord(cha) - ord('a')

    @staticmethod
    def int_to_cha(d: int):
        return chr(d + ord('a'))


class Solution2:
    # def minStickers(self, stickers: List[str], target: str) -> int:
    def min_stickers2(self, stickers: list, target: str):
        n = len(stickers)
        # 关键优化，用词频表替代贴纸数组
        counts = [[0] * 26 for i in range(n)]
        for i in range(n):
            string = list(stickers[i])
            for cha in string:
                counts[i][self.cha_to_int(cha)] += 1
        ans = self.process2(counts, target)
        return -1 if ans == sys.maxsize else ans

    def process2(self, stickers: list, t: str):
        if len(t) == 0:
            return 0
        # target做出词频统计
        target = list(t)
        t_counts = self.str_to_counts(t)
        n = len(stickers)
        min_num = sys.maxsize
        for i in range(n):
            # 尝试第一张贴纸是谁
            sticker = stickers[i]
            # 最关键的优化（重要的剪枝！ 这一步也是贪心！）
            if sticker[self.cha_to_int(target[0])] > 0:
                rest = ''
                for j in range(26):
                    if t_counts[j] > 0:
                        nums = t_counts[j] - sticker[j]
                        for k in range(nums):
                            rest += self.int_to_cha(j)
                min_num = min(min_num, self.process2(stickers, rest))
        return min_num + (0 if min_num == sys.maxsize else 1)

    @staticmethod
    def cha_to_int(cha: str):
        return ord(cha) - ord('a')

    @staticmethod
    def int_to_cha(d: int):
        return chr(d + ord('a'))

    def str_to_counts(self, string: str):
        counts = [0] * 26
        for cha in string:
            counts[self.cha_to_int(cha)] += 1
        return counts


class Solution3:
    # def minStickers(self, stickers: List[str], target: str) -> int:
    def min_stickers3(self, stickers: list, target: str):
        n = len(stickers)
        counts = [[0] * 26 for i in range(n)]
        for i in range(n):
            string = list(stickers[i])
            for cha in string:
                counts[i][self.cha_to_int(cha)] += 1
        dp = dict()
        dp[''] = 0
        ans = self.process3(counts, target, dp)
        return -1 if ans == sys.maxsize else ans

    def process3(self, stickers: [list], t: str, dp: dict):
        if dp.keys().__contains__(t):
            return dp.get(t)
        target = list(t)
        t_counts = self.str_to_counts(t)
        n = len(stickers)
        min_num = sys.maxsize
        for i in range(n):
            sticker = stickers[i]
            if sticker[self.cha_to_int(target[0])] > 0:
                rest = ''
                for j in range(26):
                    if t_counts[j] > 0:
                        nums = t_counts[j] - sticker[j]
                        for k in range(nums):
                            rest += self.int_to_cha(j)
                min_num = min(min_num, self.process3(stickers, rest, dp))
        ans = min_num + (0 if min_num == sys.maxsize else 1)
        dp[t] = ans
        return ans

    @staticmethod
    def cha_to_int(cha: str):
        return ord(cha) - ord('a')

    @staticmethod
    def int_to_cha(d: int):
        return chr(d + ord('a'))

    def str_to_counts(self, string: str):
        counts = [0] * 26
        for cha in string:
            counts[self.cha_to_int(cha)] += 1
        return counts
