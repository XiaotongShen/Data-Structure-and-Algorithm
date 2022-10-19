# -*- coding: utf-8 -*-

"""
@File: HeapGreater.py
@Author: Sarah Shen
@Time: 18/10/2022 15:33
"""


# T一定要是非基础类型，有基础类型需求包一层
class HeapGreater:
    """ 定义一个加强堆类，类中有更多方法可供使用 """

    def __init__(self):
        # 定义堆属性
        # heap用来保存堆元素的数组
        # index_map用来保存元素及其对应index的字典（哈希表）
        # hsize用来表示元素个数，堆的长度
        # comp定义的比较器 - 这个暂时不使用
        self.heap = []
        self.index_map = dict()
        self.hsize = 0

    def is_empty(self):
        """ 判断堆是否是为空 """
        return self.hsize == 0

    def size(self):
        """ 检查堆的长度 """
        return self.hsize

    def contains(self, obj):
        """ 检查堆中是否有元素obj """
        return self.index_map.keys().__contains__(obj)

    def peek(self):
        """ 查看堆顶的元素 """
        return self.heap[0]

    def push(self, obj):
        """ 向堆中压入一个元素obj """
        # 向数组heap结尾增加元素obj
        # 向字典index_map中增加元素：index pair (obj: hsize)
        # 使用定义的heap_insert将hsize位置(增加的最新的index位置)作插入动作，
        # 该动作会自动调整hsize位置的元素，使heap有效
        # 最后hsize增加1
        self.heap.append(obj)
        self.index_map[obj] = self.hsize
        self.heap_insert(self.hsize)
        self.hsize += 1

    def pop(self):
        """ 从堆顶弹出元素 """
        # 首先获取从堆顶第一个位置获取ans
        # 在返回ans之前，要调整剩余元素组成的堆的有效性
        # 将堆中0位置的元素和最后一个元素做交换
        # index_map中第一个元素极其对应的index删除
        # 将heap中最后一个元素移除，此时最后一个元素的值是拿到的堆顶的ans
        # hsize - 1
        # 将0位置上换上来的数向下调整，使堆有效
        # 返回答案
        ans = self.heap[0]
        self.swap(0, self.hsize - 1)
        self.index_map.pop(ans)
        self.heap.pop()
        self.hsize -= 1
        self.heapify(0)
        return ans

    def remove(self, obj):
        """  """
        # 找到heap中最后一个位置的元素
        # 在index_map中找到要remove的节点的index
        # 从index_map中移除要remove的节点对应的key value pair
        # 移除heap中最后一个index的值
        # hsize - 1
        # 如果要remove的元素和heap中最后一个index的值不一样，
        # 将原最后一个位置的数赋值给要移除节点对应的index
        # 在index_map中增加key - value pair：replace：index
        # 调整值replace，使heap有效
        replace = self.heap[self.hsize - 1]
        index = self.index_map.get(obj)
        self.index_map.pop(obj)
        self.heap.pop()
        self.hsize -= 1
        if replace != obj:
            self.heap[index] = replace
            self.index_map[replace] = index
            self.resign(replace)

    def resign(self, obj):
        # 获取heap中obj所对应的index
        # 对该index做一次insert，做一次heapify
        index = self.index_map.get(obj)
        self.heap_insert(index)
        self.heapify(index)

    def get_all_elements(self):
        # 遍历heap中的每一个元素，添加到辅助数组ans中，返回ans
        ans = []
        for ele in self.heap:
            ans.append(ele)
        return ans

    def heap_insert(self, index):
        # 当前出入的节点位置为index，获取起父节点位置(index - 1) / 2
        # 如果index位置元素小于其父节点位置元素，则交换父子节点，当前节点移动到父节点
        # 如此循环至结束
        while self.heap[index] < self.heap[int((index - 1) / 2)]:
            self.swap(index, int((index - 1) / 2))
            index = int((index - 1) / 2)

    def heapify(self, index):
        # 当前位置为index， 找到其左侧子节点的位置index*2+1
        # 当左侧子节点存在，即其位置小于hsize，则获取左右节点最小节点的位置，保存在best中（右侧子节点可能存在也可能不存在）
        # 对比所有存在子节点中最大的元素与父节点的值，讲较小节点的index放入best
        # 如果best = index说明当前节点比任何子节点值小，堆有效，无需调增，直接退出
        # 否则，交换best 和index位置的元素，当前节点来到best位置
        # 找到新的子节点位置继续，循环至结束
        left = index * 2 + 1
        while left < self.hsize:
            best = left + 1 if left + 1 < self.hsize and self.heap[left + 1] < self.heap[left] else left
            best = best if self.heap[best] < self.heap[index] else index
            if best == index:
                break
            self.swap(best, index)
            index = best
            left = index * 2 + 1

    def swap(self, i: int, j: int):
        o1 = self.heap[i]
        o2 = self.heap[j]
        self.heap[i] = o2
        self.heap[j] = o1
        self.index_map[o2] = i
        self.index_map[o1] = j


if __name__ == "__main__":
    # Test
    h = HeapGreater()
    print(h.is_empty())
    h.push(4)
    h.push(3)
    h.push(2)
    h.push(0)
    h.push(7)
    print(h.heap)
    print(h.index_map)
    print(h.contains(2))
    print(h.is_empty())
    print(h.peek())
    print(h.size())

    print(h.pop())
    print(h.heap)
    print(h.index_map)
    print(h.contains(2))
    print(h.is_empty())
    print(h.peek())
    print(h.size())

    h.remove(4)
    print(h.heap)

    # 检查list与dict的methods
    # a = [1, 2, 3, 4]
    # b = {1: 0, 2: 1, 3: 2, 4: 3}
    # print("List Operations")
    # print(a)
    # print(a[0])
    # print(a.pop())
    # print(a)
    #
    # print("Dict Operations")
    # print(b)
    # print(b.keys().__contains__(1))
    # print(b.pop(1))
    # print(b)
    # print(b.get(2))
    # b[1] = 0
    # print(b)
