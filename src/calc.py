#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 计算基金组合估值

from redis import Redis
from cache import Cache

cache = Cache(Redis(host='redis'))

def get_fund_value(fund_code):
    return cache.get_fund_now(fund_code)

def get_fund_name(fund_code):
    return cache.get_fund_name(fund_code)

def get_fund_nav(fund_code):
    return cache.get_fund_nav(fund_code)

def get_sum_value(funds):
    # 返回一个`今日预估净值(相比昨日涨跌)`格式的字符串
    yes = 0.0
    ret = 0.0
    for fund_code in funds:
        yes += float(funds[fund_code]) * cache.get_fund_value(fund_code)
    for fund_code in funds:
        ret += float(funds[fund_code]) * cache.get_fund_now(fund_code)
    return '{0:+.4f}'.format(ret - yes)

def main():
    _test = {
        '210004': '34.58',
        '000172': '26.25',
        '420003': 31.62,
        '040035': 18.02
    }

    __test = {
        '000311': 265.67
    }

    print(get_sum_value(_config))
    

if __name__ == "__main__": main()
