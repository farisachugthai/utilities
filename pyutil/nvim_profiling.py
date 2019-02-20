#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Automate profiling nvim.

This module currently assumes a lot but there could and should be a lot of
ways to do this.

However we haven't implemented the important part nor have we began
utilizing argparse.

Then as we keep going we can import pynvim, attach and possibly run
this inside of nvim? Idk.

"""
import datetime
import logging
import os
from platform import system
import subprocess

# Does this need to get moved back so we can initialize a logger or are we
# cool because we have one in the init file?
try:
    import pynvim
except ImportError as e:
    logging.debug(e)

from pyutil.env_checks import env_check, check_xdg_config_home


def output_results(output_dir):
    if os.path.isdir(os.path.join(output_dir, 'profiling')) is False:
        os.mkdir(os.path.join(output_dir, 'profiling'))


def main(nvim_root):
    """Profile nvim.

    Parameters
    -----------
    nvim_root : path-like object
        The directory where nvim's configuration files are found.

    Returns
    --------
    profiling_log_file : file
        Creates file based on the current time in ISO format profiling nvim.

    .. todo::

        Allow the ``test.py`` file that we use for startup to be configured.
    """
    now = datetime.date.isoformat(datetime.datetime.now())

    profiling_log_file = os.path.join(nvim_root, '', now)

    subprocess.check_output([
        'nvim', '--startuptime', profiling_log_file, 'test.py', '-c', ':qall'
    ])


def find_init_files():
    """Discover the initialization files used for nvim.

    Should theoretically work on both Windows and Unix systems.

    Returns
    --------
    nvim_root : path-like object
        The directory where nvim's configuration files are found.

    .. todo::

        Alright so if ``XDG_CONFIG_HOME`` isn't set we need
        to check ~/.config/nvim and check whether we're on windows or not

    """
    global OS
    OS = system()
    if check_xdg_config_home():
        nvim_root = os.path.join(os.environ.get('XDG_CONFIG_HOME'), '', 'nvim')
        if not os.path.isdir(nvim_root):
            logging.ERROR(
                "XDG_CONFIG_HOME set but $XDG_CONFIG_HOME/nvim doesn't exist.")
        else:
            return nvim_root
    else:
        pass


if __name__ == "__main__":
    find_init_files()

    main()
