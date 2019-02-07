#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Neovim sessions with the help of tmux.

.. module:: tmux_nvim

Depends: tmux, nvim, libtmux

"""
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
        libtmux.Server.__init__(self, colors='2', conf, **kwargs)


def check_if_virtualenv():
    """Check if we're in a virtualenv or conda env.

    .. todo::

        Do this in a better way. They'll get the warning if they use
        the builtin venv, pipenv or the other 1000 ways to isolate python.
    """
    if not os.environ.get('VIRTUAL_ENV') or \
    int(os.environ.get('CONDA_SHLVL')) = 1 or None :
        print("As a warning, you're not in a virtualenv. Pass -g to continue."
        sys.exit()


def main():
    """Check env vars and programatically ijteract with tmux and nvim."""
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
