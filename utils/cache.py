#!/usr/bin/python3
# coding:utf-8

from utils import rd

def save_token(token,user_id):
    #数据类型为字符串，兼容时间
    rd.set('tokens',token,user_id)
    rd.expire(token,3*24*3600)

def get_user_id(token):
    return rd.get(token)

def clear_token(token):
    rd.delete(token)
