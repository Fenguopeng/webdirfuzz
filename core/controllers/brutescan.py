#!/usr/bin/env python
# coding=utf-8

import time
import string

from comm.request import Req

from conf.settings import DICT_PATH
from core.data import result
from core.data import fuzz_urls

class BruteScan(Req):
    """
    暴力字典扫描并对存在的URL再次进行fuzz
    """
    def __init__(self, site, timeout, delay, threads, ext):
        super(BruteScan, self).__init__(site, timeout, delay, threads)
        self.to_brute_urls = []
        self.bruted_urls = []
        self.ext = ext
        self.threads = threads

    def load_sen_dict(self):
        with open(DICT_PATH+'/brute.txt', 'r') as f:
            return f.readlines()

    def gen_dict(self):
        for path in self.load_sen_dict():
            path = string.strip(path)
            if path.find('[EXT]'):
                path = path.replace('[EXT]', self.ext)
            url = self.site_parse[0]+'://'+self.site_parse[1]+'/'+path
            self.to_brute_urls.append(url)

    def brute(self, url):
        if self.get_is_vul(url):
            self.bruted_urls.append(url)
            fuzz_urls.put(url)

    def start(self):
        self.gen_dict()
        print '[%s] Start Brute Scan ...' % time.strftime('%H:%M:%S')
        for url in self.to_brute_urls:
            self.pool.spawn(self.brute, url)
        self.pool.joinall()
        print '[%s] Stop Brute Scan!' % time.strftime('%H:%M:%S')
        print '[%s] %s Founded' % (time.strftime('%H:%M:%S'), len(self.bruted_urls))
        result.brute = self.bruted_urls