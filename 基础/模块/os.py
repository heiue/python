#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/3/4 3:03 下午
# @Author : weiyizheng
# @File : os.py
# @desc :
import os, stat

path = '../ceshi.txt'

print(os.access(path, os.F_OK))
print(os.access(path, os.R_OK))
print(os.access(path, os.W_OK))
print(os.access(path, os.X_OK))

# retval = os.getcwd()
# print(retval)
#
# path = '../../'
# os.chdir(path)
# retval = os.getcwd()
# print(retval)

path = '../ceshi.txt'
flag = stat.UF_NOUNLINK
retval = os.chflags(path, flag)
print(retval)