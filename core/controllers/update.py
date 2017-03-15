#!/usr/bin/env python
# coding=utf-8

import os

UPDATE_CMD = 'git pull --rebase --stat origin master'

def update(is_update):
    if is_update:
        print 'Start update from github'
        print os.system(UPDATE_CMD)
        exit(1)