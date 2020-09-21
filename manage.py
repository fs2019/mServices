#!/usr/bin/python3
# coding: utf-8

from flask import render_template,request,redirect,url_for
from mainapp import app
from mainapp.views import user_v,logger_v
from flask_script import Manager
from models import db,User
from utils import cache

@app.before_request
def check_login():
    app.logger.info(request.path+'access ')
    # print(request.cookies.get('token'))
    # if request.path != '/user/login':
    if request.path not in ['/user/login','/log']:
        #验证token是否有效,token存储与redis中
        token=request.cookies.get('token')
        if not token:
            return redirect(url_for('userBlue.login'))
        else:
            user_id=cache.get_user_id(token)
            if not user_id:
                return redirect(url_for('userBlue.login'))

@app.route('/')
def index():
    token=request.cookies.get('token')
    user_id=cache.get_user_id(token)
    user=User.query.get(int(user_id))
    return render_template('index.html',user=user)

#需要勾子函数@app.before_request验证权限才能创建表
@app.route('/create_dbtables')
def create_dbtables():
    try:
        db.create_all()
        return '模型中创建数据库表成功'
    except Exception as e:
        print(e)

#需要勾子函数@app.before_request验证权限才能删除表
@app.route('/drop_dbtables')
def drop_dbtables():
    db.drop_all()
    return '模型中删除数据库所有表成功'


if __name__ == '__main__':
    #注册blueprint
    app.register_blueprint(user_v.blue,url_prefix='/user')
    app.register_blueprint(logger_v.blue)
    #初始化db
    db.init_app(app)
    manage=Manager(app)
    manage.run()


#python manage.py runserver -d
