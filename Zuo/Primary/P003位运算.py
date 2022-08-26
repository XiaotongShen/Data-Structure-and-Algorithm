# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/6/30.
Author: 
    Sarah Shen
Date: 
    2022/6/30
"""


# 位运算符
# & 与
# | 或
# ^ 异或
# ~ 取反
# >> 右移
# << 左移

def to_bin(int):
    bin = ""
    for i in range(32):
        check = int & (1 << i)
        if check == 0:
            bin = "0" + bin
        else:
            bin = "1" + bin

    return bin

a = 60
b = 13
print("=================================")
print(to_bin(a), "(a)")
print(to_bin(b), "(b)")
print(to_bin(a&b), "(a & b)")
print(to_bin(a|b), "(a | b)")
print(to_bin(a^b), "(a ^ b)")
print(to_bin(~a), "(~a)")
print(to_bin(a<<2), "(a << 2)")
print(to_bin(a>>2), "(a >> 2)")

print("\n=================================")
print(to_bin(1024), "(1024)")
print(to_bin(1024 >> 1),"(1024 >> 1)")

print("\n=================================")
c = 5
print(c,"(c)")
print(-c,"(-c)")
print(~c+1,"(~c+1)")
print(~(-c)+1,"(~(-c)+1)")

print("\n=================================")
d = 0
print(d, "(d)")
print(-d,"(-d)")
print(~d+1, "(~d+1)")











