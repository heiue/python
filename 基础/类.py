#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/12/18 6:11 下午
# @Author : weiyizheng
# @File : 类.py
# @desc :

class Eg(object):

    def __init__(self):
        self.attr1 = 1

        # 私有属性
        self.__title = '私有'

    def get_title(self):
        return self.__title

    @staticmethod
    def get_static_name():
        print(1)


if __name__ == '__main__':
    ob = Eg()
    print(ob.attr1)
    print(ob.get_title())
    print(ob.get_static_name())
