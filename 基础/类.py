#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/12/18 6:11 下午
# @Author : weiyizheng
# @File : 类.py
# @desc :

class Eg(object):
    listEx = [1, 2, 3, 4, 5]

    def __init__(self):
        self.attr1 = 1

        # 私有属性
        self.__title = '私有'

    def get_title(self):
        return self.__title

    @staticmethod
    def get_static_name():
        print(1)

    def __getitem__(self, item):
        print(item)
        print(self.listEx[item])

    def __add__(self, other):
        print(other)
        return self.attr1 + other


class Base(object):
    name = ''

    def __init__(self):
        self.name = 'heiue'

    def nowClass(self):
        print('base')

class User(Base):
    type = 0

    def __init__(self):
        Base.__init__(self)
        self.type = 1

    """重写"""
    def nowClass(self):
        print('user')

    def f(self):
        print(1)

class Tool1(object):

    def __init__(self):
        pass

    def f(self):
        print('tool1')

class Tool2(object):

    def __init__(self):
        pass

    def f(self):
        print('tool2')

class Son(Tool2, Tool1):

    def __init__(self):
        pass

if __name__ == '__main__':
    ob = Eg()
    print(ob.attr1)
    print(ob.get_title())
    print(ob.get_static_name())
    ob[1:]
    print(ob + 5)

    user = User()
    print(user.type)
    print(user.name)
    user.nowClass()
    super(User, user).nowClass()

    son = Son()
    son.f()