#!/usr/bin python
# -*- encoding: utf-8 -*-

import argparse
from conf.setting import VERSION

VERSION_INFO = 'Version: %s' % VERSION


def parse():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--target', dest='target',
                       help='The target PLC')
    group.add_argument('-p', '--port', dest='port',
                       help='The target PLC port.')
    group.add_argument('-m', '--model', dest='model',
                       help='The target PLC model.')
    group.add_argument('-thread', '--thread', dest='thread', type=int, default=1,
                       help='The max number of opreation (defautl 1)')
    group = parser.add_mutually_exclusive_group()
    # group.add_argument('-f', '--brute', dest='brute',
    #                    help='')
    group.add_argument('-o', '--output', dest='output', type=str,
                       help='File to output result(only *.txt)')
    group.add_argument('-lb', '--list block', dest='listblock',
                       help='PLC blocks operation -- List Blocks')
    group.add_argument('-lbt', '--list block type', dest='blocktype',
                       help='PLC blocks operation -- Get Blocks of Type.')
    group.add_argument('-gbi', '--get block info', dest='blockinfo',
                       help='PLC blocks operation -- Get Blocks info.')
    group.add_argument('-rs', '--read CPU', dest='szl',
                       help='PLC CPU operation -- Read SZL info.')
    group.add_argument('-rc', '--read clock', dest='clock',
                       help='PLC clock operation -- Get PLC clock info')
    group.add_argument('-b', '--brute', dest='brute',
                       help='')
    group.add_argument('-v', '--version', action='version', version=VERSION)
    args = parser.parse_args()
    return args
