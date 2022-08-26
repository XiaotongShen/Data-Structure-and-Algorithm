# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/3/15.
Author: 
    Sarah Shen
Date: 
    2022/3/15
"""

# 散列表，字典的应用
# 001 商品价格表
book = dict()

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

print(book)
print(book["avocado"])

# 电话簿
phone_book = {}

phone_book["jenny"] = 8675309
phone_book["emergency"] = 911

print(phone_book["jenny"])

# 投票箱
voted = {}
value = voted.get('tom')

voted = {}

def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")

check_voter('tom')
check_voter('mike')
check_voter('mike')

# facebook缓存
cache = {}

def get_page(url):
    if cache.get(url):
        return cache(url)
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
"""
散列表适合用于：
1. 模拟映射管事
2. 防止重复
3. 缓存/记住数据，以免服务器再通过处理来生成他们
"""

# 冲突（collision）：给两个键分配相同的位置，
# 好的散列函数很少导致冲突
# 散列表中查找所花费的时间是常量时间O（1）

