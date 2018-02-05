#!/usr/bin/env python
"""
Pumps the version number in setup.py by 1 if possible.
"""
import sys
import os
loc = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
if len(sys.argv) > 1:
    loc = sys.argv[1]
with open(os.path.join(loc, 'setup.py'), 'r') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    l2 = l.replace(' ','')
    if 'version=' in l2:
        location = l.find('version')
        before = l[:location]
        version = l.replace(' ', '').replace("'",'').replace(',', '').split('version=')[-1]
        version = version.split('.')
        version[-1] = str(int(version[-1])+1)
        version = '.'.join(version)
        lines[i] = before + 'version=\'{}\',\n'.format(version)
with open(os.path.join(loc, 'setup.py'), 'w') as f:
    f.writelines(lines)