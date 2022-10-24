# -*- coding: utf-8 -*-

"""
@File: Code04_IPO.py
@Author: Sarah Shen
@Time: 23/10/2022 00:25
"""
from queue import PriorityQueue


class Program:

    def __init__(self, c: int, p: int):
        self.c = c
        self.p = p


def find_maximized_capital(k: int, w: int, profits: list, capital: list):
    min_cost_pq = PriorityQueue()
    max_profit_pq = PriorityQueue()
    # put every Program into the min_cost_pq (小根堆)
    for i in range(len(profits)):
        min_cost_pq.put((capital[i], Program(profits[i], capital[i])))
    for i in range(k):
        while not min_cost_pq.empty() and min_cost_pq.queue[0][0] <= w:
            top_program = min_cost_pq.get()[1]
            max_profit_pq.put((-top_program.p, top_program))
        if max_profit_pq.empty():
            return w
        w += max_profit_pq.get()[1].p
    return w


if __name__ == '__main__':
    cpt = [100, 2, 3, 300]
    ps = [20, 5, 7, 17]
    print(find_maximized_capital(4, 2, ps, cpt))
