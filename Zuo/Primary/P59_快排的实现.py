# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/17.
Author: 
    Sarah Shen
Date: 
    2022/8/17
"""


# 快排在做的事情，在一个数组中，拿出最后一个数last，<= last 放在左边，> last的放在右边，last要放在 <= last 的最后一个数；
# solution 1
# 一个小于等于last的区域
# 从0开始遍历，判断当前数是否小于等于last， 是当前数加入从当前数和小于等于last做交换

# solution 2
# 分 <=last 区 & >last区 （分 < = > 三区）


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if nums is None or len(nums) <= 1:
            return nums
        else:
            # print(nums)
            last_num = nums[-1]
            lt = []
            et = []
            gt = []
            for i in range(len(nums)):
                cur = nums[i]
                if cur < last_num:
                    lt.append(cur)
                elif cur == last_num:
                    et.append(cur)
                else:
                    gt.append(cur)
                # print(cur, last_num, lt, et, gt)

            lt = self.sortArray(lt)
            gt = self.sortArray(gt)
            ans = lt + et + gt
            # print(ans)
            return ans






if __name__ == '__main__':
    a = [4, 3, 1, 0, 2, 5, 6, 0, 1, 2]
    b = [5, 2, 3, 1]

    s = Solution()
    # s.sortArray(a)
    print(a)
    print(s.sortArray(a))

    print(b)
    print(s.sortArray(b))
