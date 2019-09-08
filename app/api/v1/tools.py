#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-04 23:36
# @Author : Spoon
# @Site : 
# @File : tools.py
# @Software: PyCharm
import base64
import hashlib
import os

import qrcode
from flasgger import swag_from
from flask import jsonify, request
from werkzeug.utils import secure_filename

from app.libs import common
from app.libs.get_apk_info import get_apk_info
from app.libs.my_oss2 import upload
from app.libs.redprint import Redprint
import uuid

api = Redprint('tools')


@swag_from('tools.yml')
@api.route('/b64encode/<string:str>', methods=['GET'])
def get_base64(str):
    result = {
        'code': '200',
        'data': base64.b64encode(str.replace(' ', '').encode('utf-8')).decode()
    }
    return jsonify(result)


@swag_from('tools.yml')
@api.route('/md5/<string:str>', methods=['GET'])
def get_md5(str):
    result = {
        'code': '200',
        'data': hashlib.md5(str.encode(encoding='UTF-8')).hexdigest().upper()
    }
    return jsonify(result)


@swag_from('tools.yml')
@api.route('/makeqr/<string:str>', methods=['GET'])
def make_qr(str):
    img = qrcode.make(str)
    with open('qr.png', mode='wb') as wf:
        img.save(wf)
        image_base64 = common.pil_base64(img)
        result = upload('qr.png')
        os.remove(u'qr.png')
        result = {
            'code': '200',
            'data': {
                'base64': image_base64.decode(),
                'url': result
            }
        }
        return jsonify(result)


UPLOAD_FOLDER = '/Users/zhangxin/Documents/flask_demo/uploads'
ALLOWED_EXTENSIONS = set(['apk', 'zip'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@swag_from('tools.yml')
@api.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if len(request.files) == 0:
            result = {
                'code': '400',
                'error': '文件获取失败',
                'data': {}
            }
            return jsonify(result), 400
        file = request.files['file']
        if not allowed_file(file.filename):
            result = {
                'code': '400',
                'error': '文件格式非法',
                'data': {}
            }
            return jsonify(result), 400
        filename = secure_filename(file.filename)
        save_path = os.path.join(UPLOAD_FOLDER, str(uuid.uuid4()) + filename)
        file.save(save_path)
        # get_apk_info(save_path)
        result = {
            'code': '200',
            'error': '',
            'data': {
                'url': '',
                'msg': '文件上传成功'
            }
        }
        return jsonify(result), 200
    result = {
        'code': '405',
        'error': '请求方式非法',
        'data': {}
    }
    return jsonify(result), 405
