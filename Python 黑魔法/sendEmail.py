#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/4/14 2:18 下午
# @Author : weiyizheng
# @File : sendEmail.py
# @desc :
import smtplib
from email.mime.text import MIMEText
from email.header import Header


class email(object):
    from_host = "mr_heiue@163.com"
    license = "JIVDTGLGUZHCCIXD"
    to_host = []
    cc_host = []
    messages = {}

    def __init__(self):
        self.smtp = smtplib.SMTP()
        self.smtp.connect("smtp.163.com", 25)
        self.smtp.login(self.from_host, self.license)

    def toHost(self, host):
        self.to_host = host
        return self

    def ccHost(self, host):
        self.cc_host = host
        return self

    def message(self, title, content):
        self.messages = MIMEText(content, 'plain', 'utf-8')
        self.messages['From'] = self.from_host
        self.messages['To'] = ','.join(self.to_host)
        self.messages['Cc'] = ';'.join(self.cc_host)
        self.messages['Subject'] = title
        return self

    def send(self):
        try:
            print(self.from_host, self.to_host, self.messages)
            self.smtp.sendmail(self.from_host, self.to_host, self.messages.as_string())
            print('成功')
        except smtplib.SMTPException:
            print('失败')
        self.smtp.close()


em = email()
em.toHost(["907662506@qq.com"]).ccHost(["1295101456@qq.com"]).message('这是个标题', '收到一份邮件').send()
