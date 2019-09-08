#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-25 14:05
# @Author : Spoon
# @Site : 
# @File : views.py
# @Software: PyCharm
from flask import render_template

from . import auth



@auth.route('/')
def index():
    return 'auth'


@auth.route('/login/')
def login_view():
    return 'auth'


@auth.route('/logout/')
def logout_view():
    return 'auth'
