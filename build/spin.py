#!/usr/bin/env python3

from os      import chdir
from os.path import dirname, isdir, isfile, join
from sys     import stderr

spin_dir = join(dirname(__file__), '..', '..', 'electron-spin')

if isdir(spin_dir):
  chdir(spin_dir)
else:
  exit(0)

if not isfile('BUILD.gn'):
  print('error: electron-spin directory present, but electron-spin/BUILD.gn absent. It is expected to define the target electron-spin', file=stderr)
  exit(1)

for header in ['additional_schemes',
               'interceptors',
               'preferences',
               'pre_main_message_loop_run',
               'scheme_url_loader',
               ]:
  if isfile(header + '.h'):
    print('ELECTRON_SPIN_' + header.upper())
