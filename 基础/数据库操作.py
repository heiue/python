#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/2/19 2:41 下午
# @Author : weiyizheng
# @File : 数据库操作.py
# @desc :
import mysql.connector
import pymysql
import sys

# db = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='root'
# )

try:
    db = pymysql.connect(host='localhost', user='root', passwd='root', database='saas')
    cursor = db.cursor()
    print(db)

    cursor.execute('select * from saas_sc_poster where id = 1')

    data = cursor.fetchone()

    print(data)

    db.close()

except:
    print('Unexpected error:', sys.exc_info()[0])
