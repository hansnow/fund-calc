#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 新浪财经
# 
# 实时数据获取API
# http://app.xincai.com/fund/api/jsonp.json/<jsonp 变量名>/XinCaiFundService.getFundYuCeNav?symbol=<基金代码>
from __future__ import print_function
import sys
import requests as rq
import re

_config = {
    '210004': '34.58',
    '000172': '26.25',
    '420003': 31.62,
    '040035': 18.02
}

__config = {
    '000311': 265.67
}

def get_fund(fund_code):
    r = rq.get('http://hq.sinajs.cn/list=fu_{}'.format(fund_code))
    data = re.findall(r'"(.*?)"', r.text)
    if data[0] != '':
        # print(data, file=sys.stderr)
        data = data[0].split(',')
        return {
            "name": data[0],
            "value": float(data[3]),
            "now": float(data[2])
        }
    else:
        return None

def get_fund_nav(fund_code):
    r = rq.get('http://app.xincai.com/fund/api/jsonp.json//XinCaiFundService.getFundYuCeNav?symbol={}'.format(fund_code))
    try:
        raw_text = re.findall(r'detail:"(.*?)"', r.text)[0]
        data = re.findall(r'\d\.\d{4}', raw_text)
        return map(lambda x: float(x), data)
    except:
        return []

def get_sum_value(funds):
    ret = 0.0
    for fund_code in funds:
        ret += float(funds[fund_code]) * get_fund(fund_code)['now']
    return ret

def main():
    print(get_sum_value(_config))
    

if __name__ == "__main__": main()
