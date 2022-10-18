# -*- coding: utf-8 -*-

"""
@File: Code01_Comparator.py
@Author: Sarah Shen
@Time: 15/10/2022 16:55
"""


# 我定义的学生类
class Student:
    def __init__(self, name=None, sid=None, age=None):
        self.name = name
        self.sid = sid
        self.age = age


# 任何比较器
# compare方法里，遵循一个统一的规范：
# 返回负数的时候，认为第一个参数应该排在前面
# 返回正数的时候，认为第二个参数应该排在前面
# 返回0的时候，认为无所谓谁排在前面

# 我定义的比较器们
def id_asc_age_desc_comparator(o1: Student, o2: Student):
    # 根据id从小到大，但是如果id一样，按照年龄从大到小
    return (o1.sid - o2.sid) if o1.sid != o2.sid else (o2.age - o1.age)


def id_asc_comparator(o1: Student, o2: Student):
    # 根据id从小到大
    return o1.sid - o2.sid


def id_desc_comparator(o1: Student, o2: Student):
    # 根据id从大到小
    return o2.sid - o1.sid


def int_desc_comparator(arg0: int, arg1: int):
    # 根据整数值降序
    return arg1 - arg0


def int_asc_comparator(arg0: int, arg1: int):
    # 根据整数值降序
    return arg0 - arg1


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


def print_student(students: list):
    for student in students:
        print("Name: %s, Id: %i, Age: %i" % (student.name, student.sid, student.age))


if __name__ == '__main__':
    a = [5, 4, 3, 2, 7, 9, 1, 0]
    print("第1次打印")
    print(a)
    a.sort()
    print("第2次打印")
    print(a)
    # a.sort(reverse=True)
    a.sort(key=cmp_to_key(int_desc_comparator))
    print("第3次打印")
    print(a)
    a.sort(key=cmp_to_key(int_asc_comparator))
    print("第4次打印")
    print(a)

    student1 = Student("A", 4, 40)
    student2 = Student("B", 4, 21)
    student3 = Student("C", 3, 12)
    student4 = Student("D", 3, 62)
    student5 = Student("E", 3, 42)
    students_list = list()
    students_list.append(student1)
    students_list.append(student2)
    students_list.append(student3)
    students_list.append(student4)
    students_list.append(student5)

    print("第1次打印")
    print_student(students_list)

    students_list.sort(key=cmp_to_key(id_asc_comparator))
    print("第2次打印")
    print_student(students_list)

    students_list.sort(key=cmp_to_key(id_desc_comparator))
    print("第3次打印")
    print_student(students_list)

    students_list.sort(key=cmp_to_key(id_asc_age_desc_comparator))
    print("第4次打印")
    print_student(students_list)
