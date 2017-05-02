#!/usr/bin python
# -*- encoding: utf-8 -*-

import logging
from core.data import result


class OutputTxt(object):
    def __init__(self, output_file):
        self.logger = logging.getLogger('plcscan')
        self.result = result
        self.output_file = output_file

    def save(self):
        with open(self.output_file, 'w') as f:
            for key in self.result.keys():
                for res in self.result[key]:
                    f.write('%s\n' % res)
