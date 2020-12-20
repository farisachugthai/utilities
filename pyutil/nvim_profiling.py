#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Automate profiling nvim."""
import argparse
import datetime
import logging
import os
import subprocess
from shutil import which
from typing import Optional

import pynvim

from pyutil.__about__ import __version__


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

    now = datetime.date.isoformat(datetime.datetime.now())
    output_file = now + "-" + "nvim.log"
    parser.add_argument(
        "-o",
        "--output",
        default=output_file,
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
        default=20,
        choices=[0, 10, 20, 30, 40],
        help="Set the logging level",
    )

    # __version__ = "1"
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
        output_file: str = "nvim.log",
    ):
        """Initialize the instance.

        Parameters
        ----------
        file_to_open : str
            Invoke the nvim process with the name of a buffer to open.
        output_file : str
            The file to put the output in.
        """
        self.log = output_file
        self.path = file_to_open

    @property
    def listen_address(self) -> Optional[str]:
        """Is neovim running?

        Returns
        -------
        str or None
            str if running, None if not.
        """
        try:
            return os.environ.get("NVIM_LISTEN_ADDRESS")
        except OSError:
            return

    def attach_to_process(self):
        # This probably isnt gonna work. We need an already running
        # instance and this is more used for controlling the already
        # running nvim process
        breakpoint()
        child_argv = os.environ.get('NVIM_CHILD_ARGV')
        if child_argv is None and self.listen_address is None:
            child_argv = ["nvim", "--embed", "--headless", f"{self.path}"]

        if child_argv is not None:
            editor = pynvim.attach('child', argv=child_argv)
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
    args = _parse_arguments() if arguments is None else arguments
    user_args = args.parse_args()
    LOG_LEVEL = user_args.log_level
    logging.basicConfig(level=LOG_LEVEL)
    neovim = Neovim(user_args.path, output_file=user_args.output)
    for i in range(user_args.reruns):
        logging.info("Running neovim # of times: %s", i)
        neovim.run()


if __name__ == "__main__":
    # sys.exit(main())
    main()
