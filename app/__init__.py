#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-25 14:45
# @Author : Spoon
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm
from flasgger import Swagger
from flask import Flask
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_cors import CORS

from app.libs.extensions import celery
from app.libs.global_log import g_log
from app.libs.my_sql_alchemy import MySQLAlchemy, MyQuery
from app.pages.admin import NotAuthenticatedMenuLink, AuthenticatedMenuLink
from app.security import security
from app.setting import setting

db = MySQLAlchemy(query_class=MyQuery)
swagger = Swagger()
admin = Admin(name='Develop',template_mode='bootstrap3')


def init_plug(app):
    CORS(app, supports_credentials=True)  # 设置跨域
    db.init_app(app)
    swagger.init_app(app)
    admin.init_app(app)
    celery.init_app(app)
    app.celery = celery
    from flask_admin.contrib.sqla import ModelView
    from app.models.t_user import User
    admin.add_view(ModelView(User, db.session, name="用户管理"))
    admin.add_link(NotAuthenticatedMenuLink(name='Login', url='/auth/login/'))
    admin.add_link(AuthenticatedMenuLink(name='Logout', url='/auth/logout/'))
    admin.add_link(MenuLink(name='Back Home',url='/'))
    admin.add_link(MenuLink(name='Baidu', category='Links', url='http:www.baidu.com'))
    admin.add_link(MenuLink(name='GitHub', category='Links', url='https:www.github.com/ospoon'))


def init_blueprint(app):
    from app.pages.welcome import app as welcomeapp
    app.register_blueprint(welcomeapp)
    from app.pages.auth import auth
    app.register_blueprint(auth,url_prefix='/auth')
    from .api.v1 import create_blurprint_v1
    app.register_blueprint(create_blurprint_v1(), url_prefix='/api/v1')
    from .api.auth import create_blurprint_auth
    app.register_blueprint(create_blurprint_auth(), url_prefix='/api/auth')


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(security[config_name])
    app.config.from_object(setting[config_name])
    setting[config_name].init_app(app)

    init_plug(app)

    init_blueprint(app)

    g_log.info('create_app start')
    return app
