#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 缓存相关

from redis import Redis
import json
from provider.sina import get_fund, get_fund_nav

class Cache(object):
    def __init__(self, redis):
        self.cache = redis

    def set(self, prefix, key, value, expire=None):
        data = json.dumps(value)
        return self.cache.set('{}_{}'.format(prefix, key), data, ex=expire)

    def get(self, prefix, key):
        data = self.cache.get('{}_{}'.format(prefix, key))
        return json.loads(data)

    def exists(self, prefix, key):
        return self.cache.exists('{}_{}'.format(prefix, key))

    def get_fund_name(self, code):
        if self.exists('fund_name', code):
            return self.get('fund_name', code)
        else:
            data = get_fund(code)
            if data:
                name = data['name']
                self.set('fund_name', code, name)
                return name
            else:
                self.set('fund_name', code, '')
                return ''

    def get_fund_now(self, code):
        if self.exists('fund_now', code):
            return self.get('fund_now', code)
        else:
            now = get_fund(code)['now']
            self.set('fund_now', code, now, expire=60)
            return now

    def get_fund_value(self, code):
        if self.exists('fund_value', code):
            return self.get('fund_value', code)
        else:
            value = get_fund(code)['value']
            self.set('fund_value', code, value, expire=60)
            return value

    def get_fund_nav(self, code):
        if self.exists('fund_nav', code):
            return self.get('fund_nav', code)
        else:
            nav = get_fund_nav(code)
            value = self.get_fund_value(code)
            data = {'value': value, 'chartData': nav}
            self.set('fund_nav', code, data, expire=60)
            return data
