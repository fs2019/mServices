#!/usr/bin/python3
# coding:utf-8
import os
from flask import Blueprint,jsonify
from flask import render_template,request,redirect
from models.user import User
from utils import crypt,cache
import uuid
from datetime import datetime,timedelta
import settings
from models import db

from werkzeug.datastructures import FileStorage

blue=Blueprint('userBlue',__name__)

@blue.route('/modify',methods=['GET','POST'])
def modify():
    token=request.cookies.get('token')
    user_id=cache.get_user_id(token)
    #登陆信息在redis中

    user=User.query.get(int(user_id))

    return render_template('user/info.html',user=user)

@blue.route('/logout')
def logout():
    token = request.cookies.get('token')
    cache.clear_token(token) #删除服务端redis

    resp = redirect('/user/login')
    resp.delete_cookie('token')  # 删除客户端

    return resp

@blue.route('/login',methods=['GET','POST'])
def login():
    message=''
    data={
        'cookies':request.cookies,
        'base_url':request.base_url
    }
    if request.method=='POST':
        phone=request.form.get('phone')
        passwd=request.form.get('passwd')

        login_user=User.query.filter(User.phone==phone,\
                                     User.auth_key==crypt.pwd(passwd)).one()
        if login_user:
            #登陆成功，生成token
            token=uuid.uuid4().hex
            resp=redirect('/')
            resp.set_cookie('token',token,\
                            expires=(datetime.now()+timedelta(days=3)))

            #将token添加redis,token-user_id
            cache.save_token(token,login_user.id)
            return resp
        else:
            message='not user'

    return render_template('user/login.html',**data,msg=message)

@blue.route('/upload')
def upload_photo():
    upload_file: FileStorage=request.files.get('photo')
    filename=uuid.uuid4().hex+os.path.splitext(upload_file.filename)[-1]
    filepath=os.path.join(settings.USER_DIR,filename)
    upload_file.save(filepath)
    user=User.query.get(cache.get_user_id(request.cookies.get('token')))
    user.photo='user/'+filename
    db.session.commit()
    return jsonify({
        'msg':'upload success',
        # 'path':'user/gyy6.jpg'
        'path':'user/'+filename
    })

