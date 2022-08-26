# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/17.
Author:
    Sarah Shen
Date:
    2022/8/17
"""


## 非递归版本的并归排序
# playaroud 步长
# step = 1 merge
# step = 2 merge
# step = 4 merge
# ...
# step = 8
# 只有当步长 < 总长度的时候需要merge
# 步长>=总长度，说明全部排好序了，就结束
# 要考虑内存溢出的问题：如果我的步长比数组长度的一半大，提前退出

# 左组L ... M：在处理M的时候，为了避免 L+Step-1这个值溢出，不要取min(L+step-1, N-1),要先判断N-1-L与step的大小
# 右组M+1 ... R：同理，为了避免越界的问题，(N-1)-(M+1)+1 = N-1-M-1+1 = N-1-M >= step 的大小:M+1 ... M+1+step-1 = M +step, < : M+1 ... R = N-1
# merge ...
# step > N / 2: break -- int(N/2)是向下取整的
# step <= N / 2: step *2
# 下一个组：
# L = R+1 避免越界：R < N


class Solution:

    def sortArray(self, nums: list[int]) -> list[int]:
        if nums is None or len(nums) <= 1:
            return nums
        else:
            n = len(nums)
            step = 1
            while step < n:
                step *= 2
                # print("step is %i" % step)
                for j in range(0, n, step):
                    l = j
                    r = min(l + step, n)
                    m = l + (step >> 1)
                    # print(l, m, r)
                    left = nums[l:m]
                    right = nums[m:r]
                    # print(left, right)
                    nums[l:r] = self.merge(left, right)
                    # print(nums)
            return nums


    def merge(self, left: list, right: list):
        assist = []
        p1 = 0
        p2 = 0
        left_n = len(left) - 1
        right_n = len(right) - 1

        while p1 <= left_n and p2 <= right_n:
            if left[p1] <= right[p2]:
                assist.append(left[p1])
                p1 += 1
            else:
                assist.append(right[p2])
                p2 += 1
        while p1 <= left_n:
            assist.append(left[p1])
            p1 += 1
        while p2 <= right_n:
            assist.append(right[p2])
            p2 += 1
        return assist



if __name__ == '__main__':
    a = [4, 3, 1, 0, 2, 5, 6, 0, 1, 2]
    b = [5, 2, 3, 1]

    s = Solution()

    print(a)
    print(s.sortArray(a))

    print(b)
    print(s.sortArray(b))

