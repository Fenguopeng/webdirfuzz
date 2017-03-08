#!/usr/bin/env python
# coding=utf-8

import re
import random
import time
import logging

from urlparse import urlparse
from urlparse import urljoin
from comm.request import Req

from Queue import PriorityQueue
from Queue import Empty
from bs4 import BeautifulSoup

from core.data import result
from core.data import fuzz_urls

logger = logging.getLogger('webdirfuzz')

class Spider(Req):
    def __init__(self, site, timeout, delay, depth, threads):
        super(Spider, self).__init__(site, timeout, delay, threads)
        self.depth = depth
        self.visited = []
        self.tasks_queue = PriorityQueue()

    def get_page_content(self, url):
        r = 0
        r = self.send_http(url)
        if r != 0 and r.status == 200 and r.getheader('content-length') != self.not_found_page_length:
            print '[!]' + url.encode('utf-8')
            if r.getheader('content-type') or r.getheader('content-type').find('html') != 1:
                return r.read()
            elif r.getheader('content-length') and int(r.getheader('content-length') < 102400):
                return r.read()
            else:
                logger.info('%s content-length %s is too long' % (url, r.getheader('content-length')))

    def get_all_links(self, content):
        a_tag = self.get_a_links(content)
        all_links = a_tag
        return all_links

    def get_a_links(self, content):
        """
        获取href属性中的url
        """
        links = []
        soup = BeautifulSoup(content, 'html.parser')
        a = soup.find_all('a', attrs={'href': re.compile('.*')})
        for link in a:
            links.append(link['href'])
        return links

    def filter_links(self, url, links):
        """
        过滤链接包括非本域下、相对路径、非http
        :param url: 当前访问url
        :param links: 页面中全部链接
        :return: 过滤后有效链接
        """
        filtered_links = []
        for link in links:
            o = urlparse(link)
            if (self.site_parse[1].find(o[1]) > 0 or (o[0] == '' and o[1] == '' and o[2] != '')):
                ret = urljoin(url, link)
                filtered_links.append(ret)
        return filtered_links

    def crawl_page(self, url, depth):
        """
        爬取页面，获取链接
        :param url: 爬取目标url
        :param depth: 深度
        :return: 有效链接
        """
        if depth < 1:
            print '[-]%s' % url.encode('utf-8')
            return
        result = self.get_page_content(url)
        if not result:
            return
        links = self.get_all_links(result)
        links = self.filter_links(url, links)
        for link in links:
            self.tasks_queue.put((random.randint(1, 500), (link, depth-1)), True, 5)

    def get_visited(self):
        return self.visited

    def start(self):
        print '[%s] Start Spider...' % (time.strftime('%H:%M:%S'))
        self.tasks_queue.put((1, (self.site, self.depth)))
        while True:
            try:
                p, (url, depth) = self.tasks_queue.get(True, 1)
            except Empty, e:
                if self.pool.undone_tasks():
                    continue
                else:
                    break
            if url not in self.visited:
                self.pool.spawn(self.crawl_page, *(url, depth))
                self.visited.append(url)
                fuzz_urls.put(url)
        print '[%s] Stop Spider' % time.strftime('%H:%M:%S')
        print '[%s] %s Founded' % (time.strftime('%H:%M:%S'), len(self.visited))
        result.spider = self.visited