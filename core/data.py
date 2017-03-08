#!/usr/bin/env python
# coding=utf-8

from attrdict import AttrDict
from Queue import Queue

fuzz_urls = Queue()

# 结果存储
result = AttrDict()
result.spider = []
result.fuzz = []
result.brute = []