# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/8/9.
Author: 
    Sarah Shen
Date: 
    2022/8/9
"""

# 比较器，重载比较运算符
# 对于任意比较器， 首先要制指定两个数o1, o2
# 比较器的返回规范：
# 1. 返回负数时，认为o1应该排在o2的前面
# 2. 返回正数时，认为o2应该排在o1的前面
# 3. 返回0时，认为谁排在前面都可以

import functools


def my_comparator_num(o1, o2):
    return o2 - o1


class Student:

    def __init__(self, name, age, class_id):
        self.name = name
        self.age = age
        self.class_id = class_id

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.class_id, self.age)


def my_comparator_id(o1, o2):
    """ 按class_id从小到大排序 """
    return o1.class_id - o2.class_id


def my_comparator_age(o1, o2):
    """ 按age从小到大排序 """
    return o1.age - o2.age


if __name__ == '__main__':
    # 例子1：官方给的是从小到大的排序
    a = [4, 5, 6, 9, 8, 2, 4, 6, 3, 8, 4]
    print("排序前：")
    print(a)
    b = sorted(a)
    a.sort()
    print("==========")
    print("从小到大排序：")
    print(a)
    print(b)

    # 例子2：比较器实现从大到小排序
    print("==========")
    print("从大到小排序：")
    a.sort(key=functools.cmp_to_key(my_comparator_num))
    c = sorted(a, key=functools.cmp_to_key(my_comparator_num))
    print(a)
    print(c)

    # 例子3 对学生类排序
    s1 = Student('张三', 18, 1)
    s2 = Student('李四', 27, 3)
    s3 = Student('王五', 19, 2)
    s4 = Student('赵六', 22, 1)
    s5 = Student('左七', 34, 2)
    students = [s1, s2, s3, s4, s5]
    print("==========")
    print("按照课程age从小到大排序：")
    d = sorted(students, key=functools.cmp_to_key(my_comparator_age))
    for s in d:
        print(s)
    print("==========")
    print("按照课程id从小到大排序：")
    e = sorted(students, key=functools.cmp_to_key(my_comparator_id))
    for s in e:
        print(s)

