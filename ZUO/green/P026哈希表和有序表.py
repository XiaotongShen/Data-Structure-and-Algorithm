# -*- coding: utf-8 -*-

"""
Description:
    Created by Sarah Shen at 2022/7/26.
Author: 
    Sarah Shen
Date: 
    2022/7/26
"""
dict = { 'sarah': '我是沈晓彤'}
print(dict['sarah'])

dict['sarah'] = '她是沈晓彤'

print(dict['sarah'])

# dict.pop('sarah')
print(dict.get('sarah'))


test1 = 'sarah'
test2 = 'sarah'

dict2 = {1234567:"我是1234567"}
print(dict2[1234567])

dict3 = {}
dict3[3] = "我是3"
dict3[0] = "我是0"
dict3[7] = "我是7"
dict3[2] = "我是2"
dict3[5] = "我是5"
dict3[9] = "我是9"


from collections import OrderedDict

od = OrderedDict()

od[3] = "我是3"
od[0] = "我是0"
od[7] = "我是7"
od[2] = "我是2"
od[5] = "我是5"
od[9] = "我是9"

od
