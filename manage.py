#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019-08-25 14:45
# @Author : Spoon
# @Site : 
# @File : manage.py
# @Software: PyCharm
from http.client import HTTPException

import click
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import create_app, db, g_log
from app.libs.error import APIException
from app.libs.error_code import ServerError
from app.models.t_user import User

app = create_app('default')
# Use `celery worker -A manage.celery -l INFO` to start celery worker
celery = app.celery
manager = Manager(app)
migrate = Migrate(app, db)


@app.errorhandler(Exception)
def framework_error(e):
    g_log.error("error:")
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


'''
通过命令创建数据库
'''
@manager.command
def db_create_all():
    print(db.create_all())


@manager.command
def clean():
    click.echo('clean data start...')
    db.drop_all()
    db.create_all()
    click.echo('clean data finish...')


#执行命令 python manage.py forge -t 0001 -c 30
@manager.option('-t', '--task', dest='task', help='Quantity of messages, default is 1.', default='1')
@manager.option('-c', '--count', dest='count', help='Quantity of messages, default is 20.', default=20)
def forge(task, count):
    click.echo('create data start...')
    click.echo('Task参数 ：' + task)
    click.echo('Count参数 ：' + count)
    from faker import Faker
    fake = Faker(locale='zh_CN')
    for i in range(int(count)):
        with db.auto_commit():
            user = User()
            user.nickname = fake.name()
            user.email = fake.company_email()
            user.password = '123456789'
            db.session.add(user)
    click.echo('Created %s fake messages.' % count)
    click.echo('create data finish...')



def make_shell_context():
  return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()