#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-04 00:13
# @Author : Spoon
# @Site : 
# @File : security.py
# @Software: PyCharm

import os

class Security:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql+pymysql://root:12345678@localhost:3306/flaskdb'

    @staticmethod
    def init_app(app):
        pass

class Development(Security):
    # 数据库链接地址
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql+cymysql://root:12345678@localhost:3306/flaskdb'

    # 发信服务器用户名和密码
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'spoondev@163.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'zx123456'
    MAIL_DEFAULT_SENDER = (u'张鑫', MAIL_USERNAME)
    pass


class Testing(Security):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql+pymysql://root:12345678@localhost:3306/flaskdb'
    pass


class Production(Security):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql+pymysql://root:12345678@localhost:3306/flaskdb'
    pass


security = {
    'development': Development,
    'testing': Testing,
    'production': Production,
    'default': Development
}
