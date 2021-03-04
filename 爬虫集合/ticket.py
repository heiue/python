#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/1/25 3:28 下午
# @Author : weiyizheng
# @File : ticket.py
# @desc :
"""命令行的火车票查看器
Usage:
    12306 [-gdtkz] <from> <to> <date>

Options:
    -h,--help  显示帮助
    -g           高铁
    -d         动车
    -t         特快
    -k         快速
    -z         直达
"""

import re
import requests
import urllib.request
from pprint import pprint
import docopt
import json
import base64


class Ticket(object):
    stations_dict = dict()

    def __init__(self):
        self.stations_init()

    def stations_init(self):
        url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9183"
        result = requests.get(url)
        stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', result.text)
        self.stations_dict = dict(stations)

    def get_stations_code(self, station):
        if station in self.stations_dict:
            return self.stations_dict[station]
        else:
            return ''

    def get_ticket(self, from_station, to_station, date_station):
        s = requests.session()
        s.headers = {
            'Cookie': '_uab_collina=161155656074024912218616; JSESSIONID=E060105253877CADA5A87D73B693C2AA; BIGipServerpassport=904397066.50215.0000; RAIL_EXPIRATION=1611873038133; RAIL_DEVICEID=h4VqET2VOdR8urTZ92_iZtk7djPO7Om-TuienPsd4NRsec1w0aIjCYGnjemcLQ_yM7KF79KsrybgWSlo4a4n79bZUgz4WrTNezQelweZ0AGelH4-TnsqyKLlliHiwuIwAq3MNctMVofvi9CfOTkvMD_ksHZMi3k3; route=495c805987d0f5c8c84b14f60212447d; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u90AF%u90F8%2CHDP; BIGipServerpool_passport=65274378.50215.0000; _jc_save_toDate=2021-01-26; _jc_save_fromDate=2021-02-01; BIGipServerotn=2229797130.64545.0000'
        }

        url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={0}&leftTicketDTO.from_station={1}&leftTicketDTO.to_station={2}&purpose_codes=ADULT".format(date_station, from_station, to_station)
        # print(url)
        result = s.get(url)
        return result.json()['data']['result']

    def handler_data(self, data):
        for item in data:
            print(item)

if __name__ == '__main__':
    arg = docopt.docopt(__doc__)
    print(arg)
    tic = Ticket()
    from_station = tic.get_stations_code(arg.get('<from>'))
    to_station = tic.get_stations_code(arg.get('<to>'))
    date_station = arg.get('<date>')
    print(from_station, to_station, date_station)
    result = tic.get_ticket(from_station, to_station, date_station)
    tic.handler_data(result)
    ## 抓取的数据返回是加密的 不知道加密方式
    a = base64.b64decode("")
    print(a)

    # url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2021-02-01&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=HDP&purpose_codes=ADULT"
    # headers = {
    #     'Content-Type': 'application/json;charset=UTF-8',
    #     'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    #     'Cookie': '_uab_collina=161155656074024912218616; JSESSIONID=733D713484249DF93F4EF5B6CEE2CA90; BIGipServerpassport=904397066.50215.0000; RAIL_EXPIRATION=1611873038133; RAIL_DEVICEID=h4VqET2VOdR8urTZ92_iZtk7djPO7Om-TuienPsd4NRsec1w0aIjCYGnjemcLQ_yM7KF79KsrybgWSlo4a4n79bZUgz4WrTNezQelweZ0AGelH4-TnsqyKLlliHiwuIwAq3MNctMVofvi9CfOTkvMD_ksHZMi3k3; route=495c805987d0f5c8c84b14f60212447d; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u90AF%u90F8%2CHDP; BIGipServerpool_passport=65274378.50215.0000; _jc_save_toDate=2021-01-26; _jc_save_fromDate=2021-02-01; BIGipServerotn=787481098.24610.0000'
    # }
    # headers = {
    #     'Cookie': '_uab_collina=161155656074024912218616; JSESSIONID=E060105253877CADA5A87D73B693C2AA; BIGipServerpassport=904397066.50215.0000; RAIL_EXPIRATION=1611873038133; RAIL_DEVICEID=h4VqET2VOdR8urTZ92_iZtk7djPO7Om-TuienPsd4NRsec1w0aIjCYGnjemcLQ_yM7KF79KsrybgWSlo4a4n79bZUgz4WrTNezQelweZ0AGelH4-TnsqyKLlliHiwuIwAq3MNctMVofvi9CfOTkvMD_ksHZMi3k3; route=495c805987d0f5c8c84b14f60212447d; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u90AF%u90F8%2CHDP; BIGipServerpool_passport=65274378.50215.0000; _jc_save_toDate=2021-01-26; _jc_save_fromDate=2021-02-01; BIGipServerotn=2229797130.64545.0000'
    # }
    # rs = requests.get(url, headers=headers)
    # print(rs.json()['data']['result'])
