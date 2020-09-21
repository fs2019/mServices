#!/usr/bin/python3
#coding:utf-8


import logging


logger=logging.getLogger('')

from flask import Blueprint,request,jsonify
from flask.logging import default_handler


blue=Blueprint('loggerBlue',__name__)

@blue.route('/log',methods=['POST'])
def upload_log():
    print(request.form)
    return jsonify({
        'msg':'ok'
    })


