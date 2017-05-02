#!/usr/bin python
# -*- encoding: utf-8 -*-

import logging


def init_logger(name='plcscan', log_file_path=None):
    # init log file
    logger = logging.getLogger(name)
    log_hancler = logging.FileHandler(log_file_path)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s -%(message)s'
    )
    log_hancler.setFormatter(formatter)
    ll = (
        logging.CRITICAL,
        logging.ERROR,
        logging.WARNING,
        logging.INFO,
        logging.DEBUG
    )
    logger.setLevel(ll[4])
    log_hancler.setLevel(ll[4])
    logger.addHandler(log_hancler)
    return logger
