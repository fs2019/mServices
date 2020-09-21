#!/usr/bin/python3
#coding:utf-8

import logging
from logging.handlers import HTTPHandler,TimedRotatingFileHandler
from logging import StreamHandler,FileHandler,Formatter

logger=logging.getLogger('edu_api')

def config_log():
    fmt=Formatter(fmt='%(asctime)s %(name)s %(levelname)s: %(message)s',\
                  datefmt='%Y-%m-%d %H:%M:%S')

    iohandler=StreamHandler()
    iohandler.setLevel(logging.DEBUG)
    iohandler.setFormatter(fmt)

    file_handler=FileHandler('edu.log')
    file_handler.setLevel(logging.WARN)
    file_handler.setFormatter(fmt)

    http_handler=HTTPHandler(host='localhost:5000',
                             url='/log',
                             method='POST')
    http_handler.setLevel(logging.ERROR)
    http_handler.setFormatter(fmt) #上传的不需要格式

    logger.setLevel(logging.DEBUG)
    logger.addHandler(iohandler)
    logger.addHandler(file_handler)
    logger.addHandler(http_handler)

config_log()
logger.info('hello logger')
logger.warning('test logging warn')
logger.error('server error')
logger.critical('port8000 check bad')

