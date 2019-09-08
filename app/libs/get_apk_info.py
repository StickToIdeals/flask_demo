#!/usr/bin/env python
# encoding: utf-8
'''
@author: Spoon
@contact: zxin088@gmail.com
@file: get_apk_info.py
@time: 2019/5/22 9:12
@desc:
    aapt d badging filepath/..apk
    https://blog.csdn.net/tabactivity/article/details/76992994
'''


import functools
from app.libs.read_apk.common.aapt import aapt_tools
import os
import re


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('call')
def get_apk_info(apk_path):
    if apk_path:
        output = aapt_tools().badging(os.path.join(os.getcwd(), apk_path))
        print('应用名称: %s' % re.findall(r"application-label:'(.*?)'", output)[0])
        print('应用包名: %s' % re.findall(r"package: name='(.*?)' ", output)[0])
        print('应用版本: %s' % re.findall(r"versionName='(.*?)' ", output)[0])
    else:
        print('请按套路出牌!!!')
    os.system('pause')


if __name__ == '__main__':
    get_apk_info(apk_path = input('请输入APK文件路径!!!\n'))