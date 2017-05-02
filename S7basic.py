#!/usr/bin/python
# -*- coding: utf-8 -*-
from scapy.all import *
import random
import os
import socket

local_s7conn = "0300001611e00000001200c1020100c2020102c0010a"
local_s7set = "0300001902f08032010000000000080000f0000001000101e0"

src = "172.18.15.199"
dst = "172.18.15.163"
dport = 102
sport = random.randint(1024, 65535)
s = conf.L3socket(iface='eth1')


def str2byte(str_data):
    base = '0123456789ABCDEF'
    i = 0
    data = str_data.upper()
    result = ''
    while i < len(data):
        beg = data[i]
        end = data[i + 1]
        i += 2
        b1 = base.find(beg)
        b2 = base.find(end)
        if b1 == -1 or b2 == -1:
            return None
        result += chr((b1 << 4) + b2)
    return result

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
        try:
            port_scan = open("port_scan.log")
            port_scanRerult = port_scan.read()
            if "102/tcp" in port_scanRerult:
                dport = 102
                return dport
            else:
                return "The 102 is close"
        except:
            return "Nmap scan running error."

    def socket_detection(self, dst, dport):
        try:
            cli_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            cli_conn.connect((dst, dport))
            cli_conn.close()
        except:
            return "Socket connect error."

    def s7_connDetection(self, dst, dport):
        try:
            cli_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            cli_conn.connect((dst, dport))
            cli_conn.send(str2byte(local_s7conn))
            conn_recv = cli_conn.recvfrom(65565)
            packet = conn_recv[0]

        except:
            return "S7 Connect Error."

SiemensS7.ping_test(dst)
