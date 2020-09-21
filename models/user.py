#!/usr/bin/python3
# coding:utf-8

from sqlalchemy import Column,Integer,String,ForeignKey
from models import db

#用户和角色，多对多，1个用户多个角色，1个角色多个用户
#角色与权限，多对多，1个角色包含多个权限，1个权限多个角色使用

#抽象类，不会去创建表，减少重复代码
class BaseMode(db.Model):
    __abstract__=True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True, nullable=False)

#继承抽象类
class Role(BaseMode):
    __tablename__='role'

#继承抽象类
class QX(BaseMode):
    __tablename__='qx'

#模型之间关系不需要创建第三个模型类实现
#用户角色表
user_role=db.Table('user_role',Column('user_id',Integer,ForeignKey('user.id',\
                                                        name='user_role_fk')),
                                Column('role_id',Integer,ForeignKey('role.id',\
                                                        name='user_role_pk')))


class User(db.Model):
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(20),unique=True,nullable=False)
    auth_key=Column(String(100),nullable=False)
    nick_name=Column(String(20))
    photo=Column(String(100))

    # role_id=Column(ForeignKey('role.id'))
    # many-to-many,多对多关系，指定secondary
    roles=db.relationship(Role,secondary=user_role)



