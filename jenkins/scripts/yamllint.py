#!/usr/bin/env python

import sys
import yaml
import string
<<<<<<< HEAD
from yamllint.linter import Lintproblem
=======
from yamllint.linter import LintProblem

>>>>>>> 7e82a31... trailing-space
if len(sys.argv) < 2:
    print 'Missing file to lint'
    sys.exit(1)
ID = 'trailing-spaces'
TYPE = 'line'
<<<<<<< HEAD


def check(conf, line):
    if line.end == 0:
        return

    pos = line.end
=======
def check(conf, line):
    if line.end == 0:
        return
pos = line.end
>>>>>>> 7e82a31... trailing-space
    while line.buffer[pos - 1] in string.whitespace and pos > line.start:
        pos -= 1

    if pos != line.end and line.buffer[pos] in ' \t':
        yield LintProblem(line.line_no, pos - line.start + 1,
                          'trailing spaces')
i = 1
while i < len(sys.argv):
    try:
	yaml.load( open(sys.argv[i], 'r'), Loader=yaml.CLoader)
	print 'YAML: Syntax OK in file: '+ sys.argv[i]
    except:
	print "YAML: Invalid FAIL in file " + sys.argv[i]
    i+=1
