#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Automate profiling nvim."""
import argparse
import datetime
import logging
import os
import subprocess
import sys
from pathlib import Path
# from platform import system
# from profile import run
from shutil import which
# from timeit import Timer
from typing import Optional, Union

import pynvim
# from pynvim.api.nvim import Nvim
from pynvim.plugin import script_host

from pyutil.__about__ import __version__
# from pyutil.env_checks import check_xdg_config_home


def _parse_arguments():
    """Parse arguments given by the user."""
    parser = argparse.ArgumentParser(
        prog="Neovim Profiler", description="Automate profiling startuptime."
    )

    parser.add_argument(
        "-p",
        "--path",
        default="test.py",
        help="Path to the location of the temporary buffer for Nvim.",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="nvim.log",
        help="File to write profiling results to.",
    )

    parser.add_argument(
        "-r",
        "--reruns",
        type=int,
        default=1,
        help="Number of times to rerun neovim startup",
    )

    parser.add_argument(
        "-ll",
        "--log_level",
        dest="log_level",
        default=29,
        choices=[0, 10, 20, 30, 40],
        help="Set the logging level",
    )

    __version__ = "1"
    parser.add_argument(
        "-V", "--version", action="version", version="%(prog)s" + __version__
    )

    # sys.argv by default when invoking python from inside of neovim.
    # if len(sys.argv) == 1 or sys.argv == ['-c', 'script_host.py']:
    #     # print help so we dont raise systemexit.
    #     sys.exit(parser.print_help())
    # else:
    return parser


class Neovim:
    """Instantiate a connection to neovim if it's running, establish the path if not.

    .. todo::

        Utilize __new__ to establish a Global Object.

    """

    def __init__(
        self,
        file_to_open: str,
        output_file: Optional[Union[str, Path]] = "nvim.log",
    ):
        """Initialize the instance.

        Parameters
        ----------
        profiling_log_file : str or Path
            The directory to put the output.
        """
        # self.instance = pynvim.Nvim.from_nvim(script_host.vim) if self._get_instance() is None else self._get_instance()
        # self._buffer = Buffer()
        self.log = output_file
        self.path = file_to_open

    @property
    def listen_address(self) -> Optional[Union[str, bool]]:
        """Is neovim running?

        Returns
        -------
        str or bool
            str if running False if not.
        """
        try:
            return os.environ.get("NVIM_LISTEN_ADDRESS")
        except OSError:
            return False

    def attach_to_process(self):
        # This probably isnt gonna work. We need an already running
        # instance and this is more used for controlling the already
        # running nvim process
        child_argv = os.environ.get('NVIM_CHILD_ARGV')
        if child_argv is None and self.listen_address is None:
            child_argv = f'["nvim", "--startuptime", "{self.log}", "{self.path}", "-c", ":qall"]'

        if child_argv is not None:
            import json
            editor = pynvim.attach('child', argv=json.loads(child_argv))
        else:
            assert self.listen_address is None or self.listen_address != ''
            editor = pynvim.attach('socket', path=self.listen_address)

        return editor

    @staticmethod
    def _exe_path():
        """Where is neovim located?"""
        return which("nvim")

    def __repr__(self) -> str:
        return f"<Nvim: {self.__class__.__name__}, {self._exe_path()}>"

    def run(self) -> Optional[subprocess.CompletedProcess[bytes]]:
        try:
            return subprocess.run(
                ["nvim", "--startuptime", self.log, self.path, "-c", ":qall"]
            )
        except subprocess.CalledProcessError:
            pass


def main(arguments=None):
    # id probably do as well to refactor and make this a general decorator
    # ugh this fell apart. todo. there was a programmatic way i found to find nvim config dir.
    args = _parse_arguments() if arguments is None else arguments
    user_args = args.parse_args()
    LOG_LEVEL = user_args.log_level
    LOGGER = logging.getLogger(name=__name__)
    LOGGER.setLevel(LOG_LEVEL)
    now = datetime.date.isoformat(datetime.datetime.now())
    output_file = now + "-" + user_args.output
    neovim = Neovim(user_args.path, output_file=output_file)
    for i in range(user_args.reruns):
        LOGGER.info("Running neovim # of times: %s", i)
        neovim.run()


if __name__ == "__main__":
    sys.exit(main())
