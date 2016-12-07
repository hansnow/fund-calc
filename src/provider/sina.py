#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 新浪财经
# 
# 实时数据获取API
# http://app.xincai.com/fund/api/jsonp.json/<jsonp 变量名>/XinCaiFundService.getFundYuCeNav?symbol=<基金代码>

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
    data = re.findall(r'"(.*?)"', r.text)[0].split(',')
    if data:
        return {
            "name": data[0],
            "value": float(data[3]),
            "now": float(data[2])
        }
    else:
        return None

def get_sum_value(funds):
    ret = 0.0
    for fund_code in funds:
        ret += float(funds[fund_code]) * get_fund(fund_code)['now']
    return ret

def main():
    print(get_sum_value(_config))
    

if __name__ == "__main__": main()
