#!/usr/bin/env python
# coding=utf-8

import httplib
import socket
import sys
import time
import logging

from comm.threadpool import ThreadPool
from urlparse import urlparse

logger = logging.getLogger('webdirfuzz')

class Req(object):
    def __init__(self, site, timeout, delay, cookie, threads):
        self.site = site if site.find('://') != -1 else 'http://%s' % site
        self.site_parse = urlparse(self.site)
        self.timeout = timeout
        self.delay = delay
        self.pool = ThreadPool(threads)
        self.headers = {
            'Accept': '*/*',
            'Referer': 'http://www.google.com',
            'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'Cache-Control': 'no-cache',
			'Cookie': cookie,
        }
        self._analysis_404()

    def send_http(self, url):
        o = urlparse(url)
        r = 0
        try:
            conn = httplib.HTTPConnection(o[1], timeout=self.timeout)
            if o[4]:
                conn.request('GET', o[2] + o[3] + '?' + o[4], headers=self.headers)
            else:
                conn.request('GET', o[2] + o[3], headers=self.headers)
            r = conn.getresponse()
            logger.info('%s %s' % (url, r.status))
            time.sleep(self.delay)
        except (httplib.HTTPException, socket.timeout, socket.gaierror, Exception), e:
            logger.error('url %s is unreachable, Exception %s %s' % (url, e.__class__.__name__, e))
            print 'url %s is unreachable, Exception %s %s' % (url.encode('utf-8'), e.__class__.__name__, e)
            pass
        return r

    def _analysis_404(self):
        """
        分析404页面特征并判断目标URL是否有效
        """
        try:
            conn1 = httplib.HTTPConnection(self.site_parse[1], timeout=self.timeout)
            conn1.request('GET', self.site_parse[2]+'/../g0ogle/go0g1e/l.php', headers=self.headers)
            response = conn1.getresponse()
            self.not_found_page_length = response.getheader('Content-Length')
        except (httplib.HTTPException, socket.timeout, socket.gaierror, Exception), e:
            logger.error('url %s is unreachable, Exception %s %s' % (self.site, e.__class__.__name__, e))
            print 'url %s is unreachable, Exception %s %s' % (self.site, e.__class__.__name__, e)
            sys.exit(1)

    def get_is_vul(self, url):
        r = self.send_http(url)
        if r != 0 and r.status == 200 and r.getheader('content-length') != self.not_found_page_length:
            self.pool.threadLock.acquire()
            print '[!] %s' % url.encode('utf-8')
            self.pool.threadLock.release()
            return True
        return False