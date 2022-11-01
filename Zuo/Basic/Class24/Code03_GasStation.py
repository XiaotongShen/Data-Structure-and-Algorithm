# -*- coding: utf-8 -*-

"""
@File: Code03_GasStation.py
@Author: Sarah Shen
@Time: 31/10/2022 22:46
"""


# 测试链接：https://leetcode.com/problems/gas-station
class Solution:

    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    def can_complete_circuit(self, gas: [int], cost: [int]):
        good = self.good_array(gas, cost)
        for i in range(len(gas)):
            if good[i]:
                return i
        return -1

    @staticmethod
    def good_array(g: [int], c: [int]):
        n = len(g)
        m = n * 2
        arr = [0] * m
        for i in range(n):
            arr[i] = g[i] - c[i]
            arr[i + n] = g[i] - c[i]
        for i in range(1, m):
            arr[i] += arr[i - 1]
        w = list()
        for i in range(n):
            while len(w) != 0 and arr[w[-1]] >= arr[i]:
                w.pop()
            w.append(i)
        ans = [False] * n
        i = 0
        offset = 0
        j = n
        while j < m:
            if arr[w[0]] - offset >= 0:
                ans[i] = True
            if w[0] == i:
                w.remove(w[0])
            while len(w) != 0 and arr[w[-1]] >= arr[j]:
                w.pop()
            w.append(j)
            offset = arr[i]
            i += 1
            j += 1
        return ans
