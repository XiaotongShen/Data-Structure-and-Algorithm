# -*- coding: utf-8 -*-

"""
@File: Code02_DFS.py
@Author: Sarah Shen
@Time: 25/10/2022 17:12
"""


def dfs(node):
    if node is None:
        return
    stack = list()
    st = set()
    stack.append(node)
    st.add(node)
    # 压入的是就打印
    print(node.value)
    while len(stack) != 0:
        cur = stack.pop()
        for nxt in cur.nexts:
            if not st.__contains__(nxt):
                stack.append(cur)
                stack.append(nxt)
                st.add(nxt)
                print(nxt.value)
                break


if __name__ == '__main__':
    s = set()
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(2)
    print(s)
    print(s.__contains__(2))
    print(s.__contains__(5))
    s.remove(2)
    print(s.__contains__(2))
