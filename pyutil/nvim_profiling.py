#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Automate profiling nvim.

=============
Nvim Profiler
=============

.. highlight:: ipython

The below code displays how to attach to a remote neovim instance.

.. code-block:: python3

    >>> if not os.environ.get('NVIM_LISTEN_ADDRESS'):  # we have no running nvim
        >>> subprocess.run(['nvim&'])  # are we allowed to do this?
    >>> import pynvim
    >>> vim = pynvim.attach('socket', path=os.environ.get('NVIM_LISTEN_ADDRESS'))
    >>> vim.command('edit $MYVIMRC')
    >>> vim_root = vim.current.buffer


.. code-block:: vim

    stdpath({what})                 *stdpath()* *E6100*
    Returns |standard-path| locations of various default files and directories.

    {what}       Type    Description ~
    cache        String  Cache directory. Arbitrary temporary
                         storage for plugins, etc.
    config       String  User configuration directory. The
                         |init.vim| is stored here.
    config_dirs  List    Additional configuration directories.
    data         String  User data directory. The |shada-file|
                         is stored here.
    data_dirs    List    Additional data directories.

    Example:
        :echo stdpath("config")

Outputs <~/.config/nvim>. So that should work.

In the future this module is going to move towards implementing a command
that will behave similarly to the following command run in the shell:

.. code-block:: shell-session

    nvim --startuptime test.txt test.py test.txt -c"bn"
    # Also we could make the base command
    nvim --clean --startuptime foo.log example_module.py foo.log -c'bn'


"""
import argparse
import datetime
import logging
import os
from platform import system
import subprocess
import sys

from pyutil.__about__ import __version__
from pyutil.env_checks import check_xdg_config_home

LOGGER = logging.getLogger(name=__name__)
LOG_LEVEL = "logging.WARNING"


def _parse_arguments():
    """Parse arguments given by the user."""
    parser = argparse.ArgumentParser(
        prog='Neovim Profiler', description='Automate profiling startuptime.')

    parser.add_argument(
        "-p",
        "--path",
        dest="path",
        metavar="path",
        help="Path to the location of the temporary buffer for Nvim.")

    parser.add_argument(
        '-ll',
        '--log_level',
        dest='log_level',
        metavar='Log Level.',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Set the logging level')

    parser.add_argument('-V',
                        '--version',
                        action='version',
                        version='%(prog)s' + __version__)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        return parser.parse_args()


def output_results(output_dir):
    """Checks that an directory named profiling exists.

    IPython has a function in :ref:`IPython.utils` that I believe is called
    ensure_dir_exists. Do we provide anything that doesn't?

    Parameters
    ----------
    output_dir : str
        Directory to store profiling results in.

    Returns
    -------
    Bool

    """
    if os.path.isdir(os.path.join(output_dir, 'profiling')) is False:
        try:
            os.mkdir(os.path.join(output_dir, 'profiling'))
        except OSError:
            raise SystemExit  # is this how we do this?
        else:
            return True
    else:
        return True


def find_init_files():
    """Locate the initialization files used for nvim.

    Should theoretically work on both Windows and Unix systems.

    Returns
    --------
    nvim_root : str
        The directory where nvim's configuration files are found

    """
    global OS
    OS = system()
    if check_xdg_config_home():
        nvim_root = os.path.join(os.environ.get('XDG_CONFIG_HOME'), '', 'nvim')
        if not os.path.isdir(nvim_root):
            LOGGER.error(
                "XDG_CONFIG_HOME set but $XDG_CONFIG_HOME/nvim doesn't exist.")
        else:
            return nvim_root
    else:
        userConfFile = os.path.join(os.path.expanduser('~'), '.config', 'nvim',
                                    'init.vim')

        # Handle windows
        if not os.path.isfile(userConfFile):
            appdata_dir = os.getenv('appdata')

        if userConf is None:
            userConf = []

        return userConf


def temporary_buffer(buffer=None, path=None):
    """TODO: Docstring for temporary_buffer.

    Parameters
    ----------
    buffer : TODO, optional
    path : TODO, optional

    Returns
    -------
    TODO

    """
    if path is None:
        path = os.path.join(os.environ.get('PREFIX'), '', 'tmp')
    os.environ.putenv('NVIM_LISTEN_ADDRESS', path)


def main(nvim_root):
    """Profile nvim.

    Parameters
    -----------
    nvim_root : str
        The directory where nvim's configuration files are found.

    Returns
    --------
    profiling_log_file : str
        Creates file based on the current time in ISO format profiling nvim.


    .. todo:: Allow the ``test.py`` file that we use for startup to be configured.

    """
    now = datetime.date.isoformat(datetime.datetime.now())

    if output_results(nvim_root):
        now = 'profiling' + os.path.sep + str(now)

    profiling_log_file = os.path.join(nvim_root, '', now)

    subprocess.check_output([
        'nvim', '--startuptime', profiling_log_file, 'test.py', '-c', ':qall'
    ])


if __name__ == "__main__":
    user_args = _parse_arguments()

    try:
        LOG_LEVEL = user_args.log_level
    except Exception as e:
        LOGGER.error(e, exc_info=True)

    nvim_root = find_init_files()

    main(nvim_root)
