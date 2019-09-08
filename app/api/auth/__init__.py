#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-25 17:03
# @Author : Spoon
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm

from flask import Blueprint
from app.api.auth import client, token, user


def create_blurprint_auth():
    bp_v1 = Blueprint('common', __name__)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    user.api.register(bp_v1)
    return bp_v1