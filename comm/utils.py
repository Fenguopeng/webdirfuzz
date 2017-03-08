#!/usr/bin/env python
# coding=utf-8

import re
import urlparse

def is_ip(ip_str):
    ip_regx = """
            ^
            (?:\d{1,2}|1\d\d|2[0-4]\d|25[0-5])
            \.
            (?:\d{1,2}|1\d\d|2[0-4]\d|25[0-5])
            \.
            (?:\d{1,2}|1\d\d|2[0-4]\d|25[0-5])
            \.
            (?:\d{1,2}|1\d\d|2[0-4]\d|25[0-5])
            $
        """
    result = True if re.search(ip_regx, ip_str, re.X) else False
    return result

def is_url(url_str):
    url_regx = """
            ^
           (?:http(?:s)?://)? #protocol
           (?:[\w]+(?::[\w]+)?@)? #user@password
           ([-\w]+\.)+[\w-]+(?:.)? #domain
           (?::\d{2,5})? #port
           (/?[-:\w;\./?%&=#]*)? #params
            $
        """
    result = True if re.search(url_regx, url_str, re.X) else False
    return result

def get_domain_type(domain):
    if is_ip(domain):
        return 'ip'
    elif is_url(domain):
        return 'domain'
    else:
        return False

def get_host(domain):
    o = urlparse.urlparse(domain)
    return o[1]

def init_target(domain):
    ret = domain if domain.find('://') != -1 else 'http://%s' % domain
    return ret