#!/usr/bin/python
# -*- coding: utf-8 -*-
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
        os.system("ping -c 1 -W 1 %s > ping_result" % dstip)
        ping_result = open("ping_result")
        lines = ping_result.readlines()
        ttl = "ttl="
        times = "time="
        try:
            if lines.index(ttl) and lines.index(times):
                ping_ttl = lines[lines.index(ttl)+4: lines.index(ttl)+7]
                ping_time = lines[lines.index(times)+5: lines.index(times)+13]
                return ping_ttl, ping_time
        except:
            return "The Target Can't Unreachable."

    # Running Nmap to scan open ports
    def port_scan(dstip):
        os.system("nmap -O -p 1-65535 -sS %s -oN port_scan.log" % dstip)
        port_scan = open("port_scan.log")
        try:
            port_scanRerult = port_scan.readlines()
            for i in port_scanRerult:
                if "open" in i or "MAC" in i:
                    print i
        except:
            return "Nmap scan running error."

    # TCP connect
    # def s7_tcp_connect(self):

SiemensS7.ping_test(dst)
