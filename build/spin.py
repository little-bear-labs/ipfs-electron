#!/usr/bin/env python3

from os      import chdir
from os.path import dirname, isdir, isfile, join

spin_dir = join(dirname(__file__), '..', '..', 'electron-spin')

if isdir(spin_dir):
  chdir(spin_dir)
else:
  exit(0)

if not isfile('BUILD.gn'):
  print('error: electron-spin directory present, but electron-spin/BUILD.gn absent. It is expected to define the target electron-spin')
  exit(1)

if isfile('builtin_schemes.h'):
  print('ADDITIONAL_BUILTIN_SCHEMES')
