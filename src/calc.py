#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 计算基金组合估值

import requests as rq
import re
from provider.sina import get_fund

_config = {
    '210004': '34.58',
    '000172': '26.25',
    '420003': 31.62,
    '040035': 18.02
}

__config = {
    '000311': 265.67
}


def get_sum_value(funds):
    ret = 0.0
    for fund_code in funds:
        ret += float(funds[fund_code]) * get_fund(fund_code)['now']
    return ret

def main():
    print(get_sum_value(_config))
    

if __name__ == "__main__": main()
