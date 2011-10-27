#!/usr/bin/python

import sys

f = open(sys.argv[1], 'r')

print '<string-array name="">'

for line in f:
    print "<item>" + line.strip() + "</item>"


print '</string-array>'