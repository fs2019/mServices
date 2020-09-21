#!/usr/bin/python3
#coding:utf-8

import hashlib

def pwd(txt):
    md5_=hashlib.md5()
    md5_.update(txt.encode('utf-8'))

    # 增加加密复杂度,如果不使用下面，md5可解出000000
    # md5_.update('abc'.encode('utf-8'))

    return md5_.hexdigest()

if __name__ == '__main__':
    print(pwd('000000'))
