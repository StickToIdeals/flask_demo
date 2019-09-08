#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-04 00:13
# @Author : Spoon
# @Site : 
# @File : setting.py
# @Software: PyCharm

from datetime import timedelta

import os


class Config:
    HOST = '0.0.0.0'
    PORT = '4567'

    BABEL_DEFAULT_LOCALE = 'zh_CN'
    SECRET_KEY = '26b9a014c1d24a8a9fdd8cf8674c21ed'

    TINIFY_KEY: str = 'E1jO7bHgYutzKjsbwZMuAHI9ikC3VXIo'

    CELERY_BROKER_URL = 'redis://localhost:6379/1'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/2'
    CELERY_IMPORTS = ('app.tasks',)

    # 发送定时任务 celery beat -A celery_app -l INFO
    CELERYBEAT_SCHEDULE = {
        'app.tasks': {
            'task': 'app.tasks.add_together',
            'schedule': timedelta(seconds=10),
            'args': (2, 8)
        }
    }

    SWAGGER = {'title': 'API', 'uiversion': 2}

    TOKEN_EXPIRATION = 30 * 24 * 3600

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # f-login 配置
    REMEMBER_COOKIE_NAME = 'remember_token'
    REMEMBER_COOKIE_DURATION = timedelta(days=7)

    # 邮件配置
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.163.com')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
                   ['true', 'on', '1']
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '25'))


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


setting = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

print(os.urandom(24))
