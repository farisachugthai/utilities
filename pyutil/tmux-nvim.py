#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Neovim sessions with the help of tmux

Depends: tmux, nvim, libtmux

All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# imports: {{{
import argparse
import os
import sys
import subprocess

# TODO: This would probably do really well with some logging ya know
# Keeping an eye on the server for a lil.

try:
    import pynvim
except ImportError as e:
    sys.exit("Neovim isn't installed.")

try:
    import libtmux
except ImportError as e:
    sys.exit("libtmux isn't installed.")

from . import sys_checks
# }}}


class DefaultTmuxServer(libtmux.Server):
    """Helper for initializing tmux, nvim, ipython and anything else."""

    def __init__(self, **kwargs):
        libtmux.Server.__init__(self, colors='2', conf, **kwargs)

def check_if_virtualenv():
    if not os.environ.get('VIRTUAL_ENV') or \
    int(os.environ.get('CONDA_SHLVL')) = 1 or None:
        sys.exit("As a warning, you're not in a virtualenv. Pass -g to continue.")


def main():
    """Check the system for set environment variables."""
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
    conf = os.path.join(HOME, ".tmux.conf")
    if os.path.isfile(conf):
        has_config = 1

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
