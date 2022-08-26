# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/3/11.
Author: 
    Sarah Shen
Date: 
    2022/3/11
"""


def countdown(i):
    print(i)
    # 基线条件
    if i <= 0:
        return
    # 递归条件
    else:
        countdown(i-1)



# countdown(10)


# 数据结构：调用栈，call stack

def greet2(name):
    print("how are you, ", name, "?")
def bye():
    print("ok bye!")
def greet(name):
    print("FirstTouch, ", name, "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

# greet('Jobs')

# 递归调用栈
def fact(x):
    # 基线条件
    if x == 1:
        return 1
    # 递归条件
    else:
        return x * fact(x-1)

print(fact(3))

