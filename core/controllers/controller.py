#!/usr/bin python
# -*- encoding: utf-8 -*-

import os
import time
import logging
from conf import setting
from comm.utils import get_domain_type
from comm.utils import init_target
from comm.log import init_logger
# from core.controllers.autofuck import
from core.output.output_TXT import OutputTxt

logger = logging.getLogger('plcscan')


def init():
    if not os.path.exists(setting.LOG_PATH):
        os.makedirs(setting.LOG_PATH)


def complete(output_file):
    print '\n'
    print 'Ready to write result to %s' % output_file
    logger.info('output result to file ...')
    OutputTxt(output_file).save()
    logger.info('complete!')


def start(args):
    target = args.target
    port = args.port
    model = args.model
    thread_num = args.thread
    output = args.output

    target = init_target(target)
    domain_type = get_domain_type(target)
    if domain_type in setting.ALLOW_INPUTS:
        init()
        init_logger(log_file_path=setting.LOG_PATH + '/' + init_target(target) + '.log')
        autofuck = autofuck(target, model, port, thread_num)
        print '[%s] Scan Target: %s' % (time.strftime('%H:%M:%S:'), target)
        if output:
            complete(output)


