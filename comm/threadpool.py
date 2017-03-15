#!/usr/bin/env python
# coding=utf-8

import threading
from Queue import Queue
from Queue import Empty

class ThreadPoolSlot(threading.Thread):
    def __init__(self, tasks):
        threading.Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.idle = True
        self.start()

    def run(self):
        while True:
            try:
                func, args, kwargs = self.tasks.get(True, timeout=60)
            except Empty, e:
                break
            self.idle = False
            func(*args, **kwargs)
            self.idle = True
            self.tasks.task_done()

class ThreadPool(object):
    def __init__(self, thread_num):
        self.tasks = Queue()
        self.pool = []
        self.threadLock = threading.Lock()
        self.__init__thread_pool(thread_num)

    def __init__thread_pool(self, thread_num):
        for i in range(thread_num):
            self.pool.append(ThreadPoolSlot(self.tasks))

    def spawn(self, func, *args, **kwargs):
        """
        向队列中添加任务
        """
        self.tasks.put((func, args, kwargs))

    def joinall(self):
        self.tasks.join()
        for thread in self.pool:
            thread.join(5)

    def undone_tasks(self):
        r = 0
        for thread in self.pool:
            if not thread.idle:
                r += 1
        if r:
            r += self.tasks.qsize()
        return r