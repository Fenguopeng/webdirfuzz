#!/usr/bin/env python
# coding=utf-8

import os
VERSION = 'v1.1'

START_STR = r'''
                        _          _  _         __
                       | |        | |(_)       / _|
        __      __ ___ | |__    __| | _  _ __ | |_  _   _  ____ ____
        \ \ /\ / // _ \| '_ \  / _` || || '__||  _|| | | ||_  /|_  /
         \ V  V /|  __/| |_) || (_| || || |   | |  | |_| | / /  / /
          \_/\_/  \___||_.__/  \__,_||_||_|   |_|   \__,_|/___|/___|

                Web Dir Fuzz tool for vulnerability mining
                        By DROPS(www.dropsec.xyz)
'''

ALLOW_OUTPUT = ALLOW_INPUTS = ['domain', 'ip']

# 路径设置
dirname = os.path.dirname
abspath = os.path.abspath
join = os.path.join

ROOT_PATH = dirname(dirname(abspath(__file__)))

LOG_OPPOSITE_PATH = 'log'
LOG_PATH = join(ROOT_PATH, LOG_OPPOSITE_PATH)

DICT_OPPOSITE_PATH = 'dict'
DICT_PATH = join(ROOT_PATH, DICT_OPPOSITE_PATH)