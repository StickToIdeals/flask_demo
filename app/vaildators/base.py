#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-11 11:12
# @Author : Spoon
# @Site : 
# @File : base.py
# @Software: PyCharm

from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):

    def __init__(self):
        dara = request.json
        super(BaseForm, self).__init__(data=dara)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self