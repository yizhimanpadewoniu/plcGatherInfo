#!/usr/bin python
# -*- encoding: utf-8 -*-

import os

VERSION = 'v0.1'

START_STR = r"""
 _______  __       ______     ________                  __       ______           ______
|       \|  \     /      \   |        \                |  \     |      \         /      \
| $$$$$$$| $$    |  $$$$$$\  | $$$$$$$__    __ _______ | $$   __ \$$$$$$_______ |  $$$$$$\______
| $$__/ $| $$    | $$   \$$  | $$__  |  \  |  |       \| $$  /  \ | $$ |       \| $$_  \$/      \
| $$    $| $$    | $$        | $$  \ | $$  | $| $$$$$$$| $$_/  $$ | $$ | $$$$$$$| $$ \  |  $$$$$$\
| $$$$$$$| $$    | $$   __   | $$$$$ | $$  | $| $$  | $| $$   $$  | $$ | $$  | $| $$$$  | $$  | $$
| $$     | $$____| $$__/  \  | $$    | $$__/ $| $$  | $| $$$$$$\ _| $$_| $$  | $| $$    | $$__/ $$
| $$     | $$     \$$    $$  | $$     \$$    $| $$  | $| $$  \$$|   $$ | $$  | $| $$     \$$    $$
 \$$      \$$$$$$$$\$$$$$$    \$$      \$$$$$$ \$$   \$$\$$   \$$\$$$$$$\$$   \$$\$$      \$$$$$$

                                Information Gather tool for PLC

                                   By DROPS(www.dropsec.xyz)
"""

ALLOW_INPUTS = ALLOW_OUTPUTS = ['ip']

# Path configure
dirname = os.path.dirname
abspath = os.path.abspath
join = os.path.join

ROOT_PATH = dirname(dirname(abspath(__file__)))

LOG_OPPOSITE_PATH = 'log'
LOG_PATH = join(ROOT_PATH, LOG_OPPOSITE_PATH)

