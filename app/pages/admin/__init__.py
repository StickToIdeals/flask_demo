#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-25 15:36
# @Author : Spoon
# @Site : 
# @File : __init__.py.py
# @Software: PyCharm

from flask_admin.menu import MenuLink
from sqlalchemy.sql.functions import current_user


class AuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return True


class NotAuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return False