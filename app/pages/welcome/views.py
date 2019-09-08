#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-25 14:05
# @Author : Spoon
# @Site : 
# @File : views.py
# @Software: PyCharm
from flask import render_template, jsonify, url_for

from . import app



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/task/<int:v1>/<int:v2>')
def task(v1, v2):
    from app.tasks import add_together
    task = add_together.delay(v1, v2)
    print(task)
    return '完成'

@app.route('/longtask', methods=['POST'])
def longtask():
    from app.tasks import long_task
    task = long_task.apply_async()
    print(task.id)
    return jsonify({}), 202, {'Location': url_for('app.taskstatus',task_id=task.id)}


@app.route('/status/<string:task_id>')
def taskstatus(task_id):
    from app.tasks import long_task
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        # job did not start yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)
