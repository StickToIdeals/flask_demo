#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-13 23:52
# @Author : Spoon
# @Site : 
# @File : global_log.py
# @Software: PyCharm

import logging
import logging.config
import os


def get_logger(name='root'):
    conf_log = os.path.abspath(os.getcwd() + "/logger_config.ini")
    logging.config.fileConfig(conf_log)
    return logging.getLogger(name)


g_log = get_logger(__name__)