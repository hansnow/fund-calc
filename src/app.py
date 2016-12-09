#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from flask import Flask, request
from provider.sina import get_fund, get_fund_nav
from calc import get_sum_value, get_fund_name, get_fund_nav
import json
import sys
app = Flask(__name__)

@app.route("/api", methods=['POST'])
def calc():
    funds = request.get_json()['funds']
    try:
        return str(get_sum_value(funds))
    except:
        return 'error'

@app.route("/api/get_fund_name", methods=['POST'])
def get_name():
    fund = request.get_json()['fund']
    return get_fund_name(fund)

@app.route("/api/get_fund_nav", methods=['POST'])
def get_nav():
    fund = request.get_json()['fund']
    value = get_fund(fund)['value']
    nav = get_fund_nav(fund)
    return json.dumps({"value": value, "chartData": nav})

