#!/usr/bin/python3
#coding:utf-8

from mainapp import app
from models.user import User,Role,QX,user_role

if __name__ == '__main__':
    app.app_context().push()
    