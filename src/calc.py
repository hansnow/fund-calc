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
    ret = 0.0
    for fund_code in funds:
        ret += float(funds[fund_code]) * cache.get_fund_value(fund_code)
    return ret

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
