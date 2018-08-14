#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Neovim sessions with the help of tmux

Depends: tmux, nvim, libtmux

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
import sys
import subprocess

# TODO: This would probably do really well with some logging ya know
# Keeping an eye on the server for a lil.

try:
    import neovim
except ImportError as e:
    print(e)
    sys.exit("Neovim isn't installed.")

try:
    import libtmux
except ImportError as e:
    print(e)
    sys.exit("libtmux isn't installed.")

from . import sys_checks
# }}}


class DefaultTmuxServer(libtmux.Server):
    """Helper for initializing tmux, nvim, ipython and anything else."""

# so now we gotta figure out if this is the correct way to make a child class
# probs not tho
    def __init__(self, **kwargs):
        libtmux.Server.__init__(self, colors='2', conf,


def check_if_virtualenv():
    # TODO: Do this in a better way. They'll get the warning if they
    # use the builtin venv, pipenv or the other 1000 ways to isolate python.
    if not os.environ.get('VIRTUAL_ENV') or \
    int(os.environ.get('CONDA_SHLVL')) = 1 or None :
        print("As a warning, you're not in a virtualenv. Pass -g to continue."
        sys.exit()


def main():

    EDITOR_FLAGS = sys.argv[1:]
    if os.environ.get('EDITOR') is not None:
        EDITOR = os.environ.get('EDITOR')

    if os.environ.get('NVIM_SOCKET_PATH') is not None and len(os.environ.get('NVIM_SOCKET_PATH')) > 0:
        NVIM_SOCKET_PATH = os.environ.get('NVIM_SOCKET_PATH')
    else:
        NVIM_SOCKET_PATH = home + '.cache'


if __name__ == '__main__':

    # checks correct python version and linux os
    sys_checks.main()

    # check if tmux version 1.8< is installed
    libtmux.common.has_minimum_version()

    HOME = os.path.join(os.path.expanduser("~"), "")
    conf = os.path.join(HOME + ".tmux.conf")
    if os.path.isfile(conf):
        has_config = 1


    # because of libtmux we might not need all the stuff below
#    args = argparse.ArgumentParser("usage, description, argument_default, add_help and allow_abbrev are already true")
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-s", "--session", "foo")
    #  parser.add_argument('project_id', help='Your Google Cloud project ID.')
    #  parser.add_argument(
    #      'bucket_name', help='Your Google Cloud Storage bucket name.')
    #  parser.add_argument(
    #      '--zone',
    #      default='us-central1-f',
    #      help='Compute Engine zone to deploy to.')
    #  parser.add_argument(
    #      '--name', default='demo-instance', help='New instance name.')

    args = parser.parse_args()
