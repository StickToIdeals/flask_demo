#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-10 23:19
# @Author : Spoon
# @Site : 
# @File : forms.py
# @Software: PyCharm
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.libs.token_auth import User

from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, ValidationError, Email, Regexp

from app.models.t_user import User
from app.libs.enums import ClientTypeEnum
from app.vaildators.base import BaseForm


class ClientForm(BaseForm):
    account = StringField(validators=[DataRequired('必填'), length(
        min=5, max=32
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        # password can only include letters , numbers and "_"
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()
