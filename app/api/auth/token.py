#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-10 22:57
# @Author : Spoon
# @Site : 
# @File : token.py
# @Software: PyCharm
from flasgger import swag_from
from flask import current_app, jsonify
from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.t_user import User
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from app.vaildators.forms import ClientForm

api = Redprint('token')


@swag_from('common.yml')
@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,
    }
    identity = promise[ClientTypeEnum(form.type.data)](
        form.account.data,
        form.secret.data
    )
    # Token
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identity['uid'],
                                form.type.data,
                                identity['scope'],
                                expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None,
                        expiration=7200):
    """生成令牌"""
    s = Serializer(current_app.config['SECRET_KEY'],
                   expires_in=expiration)
    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })
