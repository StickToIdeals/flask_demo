#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-25 15:38
# @Author : Spoon
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views