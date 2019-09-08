#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-09-01 11:47
# @Author : Spoon
# @Site : 
# @File : common.py
# @Software: PyCharm
import base64
from io import BytesIO
from PIL import Image


##PIL转base64
def pil_base64(image):
    img_buffer = BytesIO()
    image.save(img_buffer, format='JPEG')
    byte_data = img_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str


##base64转PIL
def base64_pil(base64_str):
    image = base64.b64decode(base64_str)
    image = BytesIO(image)
    image = Image.open(image)
    return image
