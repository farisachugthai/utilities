#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Automate profiling nvim."""
import argparse
import datetime
import logging
import os
from platform import system
from shutil import which
import subprocess
import sys
from typing import AnyStr

import pynvim

from pyutil.__about__ import __version__
from pyutil.env_checks import check_xdg_config_home

LOGGER = logging.getLogger(name=__name__)
LOG_LEVEL = "logging.WARNING"


def _parse_arguments():
    """Parse arguments given by the user."""
    parser = argparse.ArgumentParser(
        prog="Neovim Profiler", description="Automate profiling startuptime."
    )

    parser.add_argument(
        "-p",
        "--path",
        dest="path",
        help="Path to the location of the temporary buffer for Nvim.",
    )

    parser.add_argument(
        "-ll",
        "--log_level",
        dest="log_level",
        metavar="Log Level.",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level",
    )

    parser.add_argument(
        "-V", "--version", action="version", version="%(prog)s" + __version__
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        return parser.parse_args()


class Neovim:
    """Instantiate a connection to neovim if it's running, establish the path if not.

    Got to the point where I thought:

    *Let's just rewrite this module.*
    """

    def __init__(self, exe=None):
        if exe:
            self.exe = exe
        else:
            self.exe = self._get_instance()

    @property
    def running_instance(self):
        """Is neovim running?"""
        try:
            remote = os.environ.get("NVIM_LISTEN_ADDRESS")
        except OSError:
            return None
        else:
            return remote

    def _get_instance(self):
        """Determine if neovim is running."""
        if self.running_instance:
            vim = pynvim.attach("socket", path=self.running_instance)
            return vim
        else:
            return None

    @property
    def _exe_path(self):
        """Where is neovim located?"""
        return which("nvim")

    def __repr__(self) -> str:
        return f"<Nvim: {self.__class__.__name__}, {self.exe}>"


def output_results(output_dir):
    """Checks that an directory named profiling exists.

    IPython has a function in :mod:`IPython.utils` that I believe is called
    ensure_dir_exists. Do we provide anything that that implementation doesn't?

    Parameters
    ----------
    output_dir : str
        Directory to store profiling results in.

    Returns
    -------
    Bool

    """
    if os.path.isdir(os.path.join(output_dir, "profiling")) is False:
        try:
            os.mkdir(os.path.join(output_dir, "profiling"))
        except OSError as e:
            sys.exit(e)
        else:
            return True
    else:
        return True


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
        now = "profiling" + os.path.sep + str(now)

    profiling_log_file = os.path.join(nvim_root, "", now)

    subprocess.check_output(
        ["nvim", "--startuptime", profiling_log_file, "test.py", "-c", ":qall"]
    )


if __name__ == "__main__":
    user_args = _parse_arguments()

    try:
        LOG_LEVEL = user_args.log_level
    except Exception as e:
        LOGGER.error(e, exc_info=True)

    nvim_root = None  # Define it temporarily we need to refactor
    # main(nvim_root)
