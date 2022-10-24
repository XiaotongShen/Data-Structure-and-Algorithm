# -*- coding: utf-8 -*-

"""
@File: Code03_BestArrange.py
@Author: Sarah Shen
@Time: 23/10/2022 00:25
"""
# 一个会议室，安排最多的会议
# 有效的贪心策略，先安排结束时间最早的


class Program:

    def __init__(self, s: int, e: int):
        self.start = s
        self.end = e


def best_arrange1(programs):
    if programs is None or len(programs) == 0:
        return 0
    return process(programs, 0, 0)


def process(programs, done: int, time_line: int):
    """
    还剩下的会议都放在programs里
    done：之前已经安排了多少会议
    timeline：目前来到的时间点是什么
    返回能安排的最多会议数量
    """
    if len(programs) == 0:
        return done
        # 检查还剩下的会议
    max_pros = done
    # 当前安排的会议是什么会，每一个枚举
    for i in range(len(programs)):
        if programs[i].start >= time_line:
            nxt = copy_but_except(programs, i)
            max_pros = max(max_pros, process(nxt, done + 1, programs[i].end))
    return max_pros


def copy_but_except(programs, i: int):
    ans = [None] * (len(programs) - 1)
    index = 0
    for k in range(len(programs)):
        if k != i:
            ans[index] = programs[k]
            index += 1
    return ans


def my_comparator(p1, p2):
    return p1.end - p2.end


def cmp_to_key(mycmp):
    """
    Convert a cmp= function into a key= function
    """

    class K:
        def __init__(self, obj):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0

    return K


def best_arrange2(programs):
    """ 会议的开始时间和结束时间都是数值，不小于0 """
    programs.sort(key=cmp_to_key(my_comparator))
    time_line = 0
    result = 0
    for i in range(len(programs)):
        if time_line <= programs[i].start:
            result += 1
            time_line = programs[i].end
    return result


if __name__ == '__main__':
    p = list()
    p.append(Program(1, 2))
    p.append(Program(2, 9))
    p.append(Program(1, 4))
    p.append(Program(9, 12))
    p.append(Program(3, 10))
    print(best_arrange2(p))
    print()
    print(best_arrange1(p))
