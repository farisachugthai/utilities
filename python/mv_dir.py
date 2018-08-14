#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maintainer: Faris Chugthai

"""No-op

For the time being this is primarily going to be a really simple no-op so
I can practice using argparse in different contexts.

https://github.com/farisachugthai

All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = 'Faris Chugthai'
__copyright__ = 'Copyright (C) 2018 Faris Chugthai'
__license__ = 'MIT'
__email__ = 'farischugthai@gmail.com'

# imports: {{{
import argparse
import os
import shutil
import sys
# }}}

# jeez what was i doing? this is potentially dangerous code....dressed up
# a rm -rf in sheeps clothing....
#  for f in os.listdir(src):
#      try:
#          shutil.rmtree(dest)
#      except NotADirectoryError:
#          try:
#              os.unlink(dest)
#          except FileNotFoundError:
#              pass
#      shutil.move(src, dest)


if __name__ = '__main__':
# lines we wanna improve on
#  src = input("What is the path of the directory you would like to move?")
#  # Should create an error if not given a string.
#  dest = input("What is the path of the directory you want to move to?")
    pass
