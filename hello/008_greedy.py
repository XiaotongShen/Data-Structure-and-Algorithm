# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/3/31.
Author: 
    Sarah Shen
Date: 
    2022/3/31
"""

# 集合演示
fruits = set(["avocado", "tomato", "banana"])
vegetables = set(["beets", "carrots", "tomato"])
print(fruits | vegetables)
print(fruits & vegetables)
print(fruits - vegetables)
print(vegetables - fruits)

# 电台覆盖问题

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])       # 定义需要覆盖的州
print(states_needed)

# 定义广播电台清单
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
print(stations)
print('定义广播电台清单')

def find_station_list(states_needed, stations):
    final_stations = set()      # 初始化电台列表，空集合
    print(states_needed)
    while states_needed:
        best_station = None         # 初始化最大覆盖的电台， None
        states_covered = set()      # 初始化覆盖的州，空集合
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station # 电台所覆盖的未被覆盖的州
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        final_stations.add(best_station)
        states_needed -= states_covered
        print(best_station, states_covered, states_needed)

    print(final_stations)

find_station_list(states_needed, stations)





