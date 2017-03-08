#!/usr/bin/env python
# coding=utf-8

import logging

def init_logger(name='webdirfuzz', log_file_path=None):
    """
    初始化日志文件
    """
    logger = logging.getLogger(name)
    log_handler = logging.FileHandler(log_file_path)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_handler.setFormatter(formatter)
    ll = (logging.CRITICAL,
          logging.ERROR,
          logging.WARNING,
          logging.INFO,
          logging.DEBUG)
    logger.setLevel(ll[4])
    log_handler.setLevel(ll[4])
    logger.addHandler(log_handler)
    return logger