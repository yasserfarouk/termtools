#!/usr/bin/env python
"""
A script to insert requirements from pipfile to setup.py.

The script assumes that both Pipfile and setup.py are in the same folder which is '..'. This can be changed by passing
one argument with the location of setup.py file
"""
import sys
import os
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip
loc = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
if len(sys.argv) > 1:
    loc = sys.argv[1]
pfile = Project(chdir=False).parsed_pipfile
requirements = convert_deps_to_pip(pfile['packages'], r=False)
test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)
with open(os.path.join(loc, 'setup.py'), 'r') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'install_requires' in l:
        location = l.find('install_requires')
        before = l[:location]
        lines[i] = before + 'install_requires={},\n'.format(requirements)
with open(os.path.join(loc, 'setup.py'), 'w') as f:
    f.writelines(lines)