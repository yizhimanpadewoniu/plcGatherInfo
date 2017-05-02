#!/usr/bin python
# -*- encoding: utf-8 -*-

import os
import commands
import socket
import sys
import time
import logging
from comm import errorMsg
from comm.threadpool import ThreadPool

logger = logging.getLogger('plcscan')


class Request(object):
    def __init__(self, target, model, port, threads):
        self.target = target
        self.model = model
        self.port = port
        self.pool = ThreadPool(threads)
        self._analysis_s7()

    def _ping_s7(self, target):
        try:
            ping_result = commands.getstatusoutput("ping -c 1 -W 5 %s > ping_result" % target)
            # os.system("ping -c 1 -W 1 %s > ping_result" % target)
            ping_status = ping_result[0]
            ping_output = ping_result[1]
            if ping_status == 256:
                logger.error('host %s is unreachable.' % self.target)
            elif ping_status == 0:
                try:
                    ping_ttl = ping_output.find('ttl=')
                    ping_time = ping_output.find('time=')
                    if ping_ttl is True & ping_time is True:
                        # r = ping_ttl, ping_time
                        logger.info('%s %s %s' % (self.target, ping_ttl, ping_time))
                        # return ping_ttl, ping_time
                except errorMsg.PingException, e:
                    logger.error('Host %s %s.' % (self.target, e))
        except errorMsg.NetException, e:
            logger.error('%s %s' % (self.target, e))
            sys.exit(1)


    def _analysis_s7(self):

