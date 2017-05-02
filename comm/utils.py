#!/usr/bin python
# -*- encoding: utf-8 -*-

import re


def is_ip(ip_str):
    ip_regx = '''
    ^
    (?:\d{1,2}|1\d\d|2[0-4]\d|25[0-5])
    \.
    (?:\d{1,2}|1\d\d|2[0-4]\d|25[0-5])
    \.
    (?:\d{1,2}|1\d\d|2[0-4]\d|25[0-5])
    \.
    (?:\d{1,2}|1\d\d|2[0-4]\d|25[0-5])
    $
    '''
    result = True if re.search(ip_regx, ip_str, re.X) else False
    return result


def get_domain_type(domain):
    if is_ip(domain):
        return 'ip'
    else:
        return False


def init_target(domain):
    ret = domain
    return ret
