#!/usr/bin/env python
# coding=utf-8

import re
import time
import string

from urlparse import urlparse
from comm.request import Req
from conf.settings import DICT_PATH
from core.data import result
from core.data import fuzz_urls
from Queue import Empty

class FuzzFileScan(Req):
    def __init__(self, site, timeout, delay, cookie, threads):
        super(FuzzFileScan, self).__init__(site, timeout, delay, cookie, threads)
        self.fuzzed_urls = []
        self.test_urls = []

    def load_suffix_dict(self):
        with open(DICT_PATH+'/fuzz.txt', 'r') as f:
            return f.readlines()

    def filter_links(self, url):
        """
        静态文件类型不测试
        """
        pattern = re.compile(r'/.*\.(?!html|htm|js|css|jpg|png|jpeg|gif|svg|pdf|avi|mp4|mp3)')
        ret = re.match(pattern, url)
        return ret

    def gen_dict(self, url):
        o = urlparse(url)
        ret = []
        if self.filter_links(o[2]):
            for stuffix in self.load_suffix_dict():
                to_fuzz_url = o[0] + '://' + o[1] + o[2] + string.strip(stuffix)
                ret.append(to_fuzz_url)
            return ret
        return []

    def fuzz(self, urls):
        for url in urls:
            if self.get_is_vul(url):
                self.fuzzed_urls.append(url)

    def start(self):
        print '[%s] Start Fuzz File Scan ...' % time.strftime('%H:%M:%S')
        while True:
            try:
                url = fuzz_urls.get(True, 1)
                to_fuzz_url_list = self.gen_dict(url)
            except Empty, e:
                if self.pool.undone_tasks():
                    continue
                else:
                    break
            self.pool.spawn(self.fuzz, to_fuzz_url_list)
        print '[%s] Stop Fuzz File Scan!' % time.strftime('%H:%M:%S')
        print '[%s] %s Founded' % (time.strftime('%H:%M:%S'), len(self.fuzzed_urls))
        result.fuzz = self.fuzzed_urls