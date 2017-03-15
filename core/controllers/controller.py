#!/usr/bin/env python
# coding=utf-8
import time
import logging

from conf import settings
from comm.utils import get_domain_type
from comm.utils import get_host
from comm.utils import init_target
from core.controllers.spider import Spider
from core.controllers.fuzzfilescan import FuzzFileScan
from core.controllers.brutescan import BruteScan
from core.output.output_txt import OutputTxt
from comm.log import init_logger
from core.controllers import update

import os

logger = logging.getLogger('webdirfuzz')

def complate(output_file):
    print '\n'
    print 'Ready to write result to %s' % output_file
    logger.info('output result to file ...')
    OutputTxt(output_file).save()
    logger.info('complete!')

def init():
    if not os.path.exists(settings.LOG_PATH):
        os.makedirs(settings.LOG_PATH)

def start(args):
    target = args.target
    timeout = args.timeout
    delay = args.delay
    depth = args.depth
    thread_num = args.thread
    is_brute = args.brute
    ext = args.ext
    output = args.output
    cookie = args.cookie
    is_update = args.update

    update.update(is_update)
    target = init_target(target)
    domain_type = get_domain_type(target)
    if domain_type in settings.ALLOW_INPUTS:
        # 初始化
        init()
        init_logger(log_file_path=settings.LOG_PATH + '/' + get_host(target) + '.log')
        spider = Spider(target, timeout, delay, cookie, depth, thread_num)
        fuzz = FuzzFileScan(target, timeout, delay, cookie, thread_num)
        brute = BruteScan(target, timeout, delay, cookie, thread_num, ext)
        print '[%s] Scan Tartget: %s' % (time.strftime('%H:%M:%S'), target)
        if not is_brute:
            spider.start()
        brute.start()
        fuzz.start()
        if output:
            complate(output)