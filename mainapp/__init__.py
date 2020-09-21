#!/usr/bin/python3
# coding: utf-8

from flask import Flask
import settings
from flask.logging import default_handler
from logging import FileHandler,Formatter
import logging

app=Flask(__name__)
app.config.from_object(settings.Dev)
app.logger.setLevel(logging.INFO)

app.logger.removeHandler(default_handler)

fmt = Formatter(fmt='%(asctime)s %(name)s %(levelname)s: %(message)s', \
                datefmt='%Y-%m-%d %H:%M:%S')

file_handler = FileHandler('edu.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(fmt)

app.logger.addHandler(file_handler)