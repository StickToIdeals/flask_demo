#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-09-01 12:47
# @Author : Spoon
# @Site : 
# @File : my_oss2.py
# @Software: PyCharm

import oss2
import uuid
import logging


def upload(name):
    # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
    auth = oss2.Auth('LTAIUm2QVQBPA64c', 'IDgldVXROjVgB2pibcwInEivnHe5nc')
    # 开启日志
    # oss2.set_file_logger('oss_log.log', 'oss2', logging.INFO)
    # Endpoint以杭州为例，其它Region请按实际情况填写。
    bucket = oss2.Bucket(auth, 'http://oss-cn-hangzhou.aliyuncs.com', '10atech')
    filename = str(uuid.uuid4()) + '.png'
    result = bucket.put_object_from_file(filename, name)
    print('http status: {0}'.format(result.status))
    if result.status == 200:
        return bucket.sign_url('GET', filename, 60 * 60 * 24 * 30)
