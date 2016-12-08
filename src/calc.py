#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 计算基金组合估值

import requests as rq
import re
from redis import Redis
from provider.sina import get_fund as _get_fund

cache = Redis(host='redis')

def get_fund_value(fund_code):
    if cache.exists(fund_code):
        return float(cache.get(fund_code))
    else:
        now = _get_fund(fund_code)['now']
        cache.set(fund_code, now, ex=60)
        return now

def get_fund_name(fund_code):
    data = _get_fund(fund_code)
    if data:
        return data['name']
    else:
        return ''

def get_sum_value(funds):
    ret = 0.0
    for fund_code in funds:
        ret += float(funds[fund_code]) * get_fund_value(fund_code)
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
