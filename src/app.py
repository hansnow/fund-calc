#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from flask import Flask, request
from calc import get_sum_value
import sys
app = Flask(__name__)

@app.route("/api", methods=['POST'])
def calc():
    funds = request.get_json()['funds']
    try:
        return str(get_sum_value(funds))
    except:
        return 'error'