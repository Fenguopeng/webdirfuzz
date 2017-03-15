#!/usr/bin/env python
# coding=utf-8

import argparse

from conf.settings import VERSION

VERSION_INFO = 'Version: %s' % VERSION
def parse():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--target', dest='target',
                        help='The target site to be scanned')
    group.add_argument('-update', '--update', dest='update', action='store_true', default=False,
                        help='update from github automaticly')
    parser.add_argument('-thread', '--thread', dest='thread', type=int, default=1,
                        help='Max number of concurrent HTTP requests (default 1)')
    parser.add_argument('-d', '--depth', dest='depth', type=int, default=1,
                        help='depth for spider(default 3)')
    parser.add_argument('-b', dest='brute', action='store_true', default=False,
                        help='just brute scan, others ignored')
    parser.add_argument('-e', '--ext', dest='ext', type=str, default='php',
                        help='brute scan path extention(default php)')
    parser.add_argument('-o', '--output', dest='output', type=str,
                        help='File to output result(only TXT)')
    parser.add_argument('--delay', dest='delay', type=int, default=0,
                        help='Delay in seconds between each HTTP request(default 0)')
    parser.add_argument('--cookie', dest='cookie', type=str, default='',
                        help='Add Cookie with HTTP request ')
    parser.add_argument('--timeout', dest='timeout', type=int, default=5,
                        help='HTTP request timeout(default 5)')
    parser.add_argument('-V', '--version', action='version', version=VERSION_INFO)
    args = parser.parse_args()
    return args