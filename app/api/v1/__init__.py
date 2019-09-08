#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-25 16:14
# @Author : Spoon
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm
from flask import Blueprint

from app.api.v1 import tools


def create_blurprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    tools.api.register(bp_v1)
    return bp_v1