#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 天天基金网

import requests as rq
import re

def get_fund(fund_code):
    r = rq.get('http://fundgz.1234567.com.cn/js/{}.js'.format(fund_code))
    if r.status_code == 200:
        print r.encoding
        name = re.findall(r'"name":"(.*?)"', r.text)[0]
        value = re.findall(r'"dwjz":"(.*?)"', r.text)[0]
        now = re.findall(r'"gsz":"(.*?)"', r.text)[0]
        return {
            "name": name,
            "value": float(value),
            "now": float(now)
        }
    else:
        return None
