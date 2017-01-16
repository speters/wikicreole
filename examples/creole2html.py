#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from creole import Parser
from creole.html_emitter import HtmlEmitter

if __name__=="__main__":
    try:
        document = Parser(unicode(sys.stdin.read(), 'utf-8', 'ignore')).parse()
    except NameError:
        document = Parser(sys.stdin.read()).parse()

    try:
        sys.stdout.write(HtmlEmitter(document).emit().encode('utf-8', 'ignore'))
    except TypeError:
        sys.stdout.write(HtmlEmitter(document).emit())

