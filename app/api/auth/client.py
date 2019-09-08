#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-10 23:11
# @Author : Spoon
# @Site : 
# @File : client.py
# @Software: PyCharm

from flasgger import swag_from

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.t_user import User
from app.vaildators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@swag_from('common.yml')
@api.route('/register', methods=['POST'])
def create_client():
    '''校验传入参数'''
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email()
    }
    '''执行注册函数'''
    promise[form.type.data]
    return Success()


def __register_user_by_email():
    '''校验传入参数'''
    form = UserEmailForm().validate_for_api()
    '''入库完成注册'''
    User.register_by_email(form.nickname.data, form.account.data, form.secret.data)
