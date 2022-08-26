# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/5/6.
Author: 
    Sarah Shen
Date: 
    2022/5/6
"""

class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        """
        :param cost:
        :return:
        """
        n = len(cost)
        for i in range(2,n+1):
            print(i)
        # cost_list = []
        # for j in range(2):
        #     costs = cost[j]
        #     stairs = [j]
        #     for i in range(j, len(cost)-1):
        #         if i in stairs:
        #             c1 = cost[i+1]
        #             c2 = cost[i+2]
        #             if c1 >= c2:
        #                 costs += c2
        #                 stairs.append(i+2)
        #             else:
        #                 costs += c1
        #                 stairs.append(i+1)
        #         else:
        #             pass
        #     cost_list.append(costs)
        # return min(cost_list[0], cost_list[1])

# cost = [10, 15, 20]
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# cost = [0, 1, 2, 2]
print(cost)
print(type(cost))

s = Solution()
# min_cost =
s.minCostClimbingStairs(cost)

print(min_cost)