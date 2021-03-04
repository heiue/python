#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/27 11:24 上午
# @Author : weiyizheng
# @File : dict.py
# @desc :
some_dict = {}
some_dict[5.5] = "Ruby"
some_dict[5.0] = "JavaScript"
some_dict[5] = "Python"
print(some_dict[5.5])
#输出 Ruby
print(some_dict[5.0])
#输出 Python
print(some_dict[5])
#输出 Python

print(hash(5.0) == hash(5))