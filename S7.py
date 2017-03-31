#!/usr/bin/python
# -*- coding: utf-8 -*-
from scapy.layers.inet import IP, ICMP
from scapy.all import *
import random
import os

src = "172.18.15.199"
dst = "172.18.15.163"
dport = 102
sport = random.randint(1024, 65535)
s = conf.L3socket(iface='eth1')



class SiemensS7(object):

    # def __init__(self):
    #     pass

    # Ping Detection
    @staticmethod
    def ping_test(dstip):
        ping_result = os.system("ping -c 1 %s" % dstip)
        return ping_result

a = SiemensS7.ping_test(dst)
