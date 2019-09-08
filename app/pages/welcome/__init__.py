#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-25 14:04
# @Author : Spoon
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

app = Blueprint('app', __name__)

from . import views