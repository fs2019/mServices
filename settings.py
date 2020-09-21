#!/usr/bin/python3
# coding: utf-8

class Dev():
    ENV='development'
    DEBUG=True


    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:''@localhost/edu?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_COMMIT_ON_TEAPDOWN=True
    SQLALCHEMY_ECHO=True