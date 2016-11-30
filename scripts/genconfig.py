#!/usr/bin/env python

import os
import re
import sys

comment = re.compile('^\s*#')
assign = re.compile('^\s*([a-zA-Z_]+)\s*(\?)?=\s*([^#]*)')

args = os.environ.copy()
for arg in sys.argv:
    m = assign.match(arg)
    if m:
        var = m.group(1).strip()
        val = m.group(3).strip()
        args[var] = val

with open('CONFIG') as f:
    for line in f:
        line = line.strip()
        if not comment.match(line):
            m = assign.match(line)
            if m:
                var = m.group(1).strip()
                default = m.group(3).strip()
                val = default
                if var in args:
                    val = args[var]
                if default.lower() == 'y' or default.lower() == 'n':
                    if val.lower() == 'y':
                        print "#define SPDK_{} 1".format(var)
                    else:
                        print "#undef SPDK_{}".format(var)
                else:
                    strval = val.replace('"', '\"')
                    print "#define SPDK_{} \"{}\"".format(var, strval)
