#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-11 18:57
# @Author : Spoon
# @Site : 
# @File : user.py
# @Software: PyCharm


from flasgger import swag_from
from flask import jsonify, g

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.t_user import User

api = Redprint('user')


# @swag_from('common.yml')
@api.route('/get/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


# @swag_from('common.yml')
@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()
