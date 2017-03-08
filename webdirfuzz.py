#!/usr/bin/env python
# coding=utf-8

import sys

from conf.settings import START_STR

def main():
    print(START_STR)
    try:
        from core.parser import parse
        from core.controllers.controller import start

        args = parse()
        start(args)
    except Exception, e:
        print e
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()