#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Possibly rewrote the entire module in half as many lines.

Now utilizes necessary libraries like glob.

.. note:

    I was just in ``~/.config/nvim`` trying to symlink my dots from
    ``~/projects/viconf/.config/nvim`` and running::

        dlink2.py ~/projects/viconf/.config/nvim

    while in ~/.config/nvim did nothing at all.

.. version-changed:: Added argparse

"""
import argparse
import glob
import os
import sys

from pyutil.__about__ import __version__


def _parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "destination",
        type=str,
        metavar="destination",
        nargs=1,
        help="Files to symlink to."
    )

    parser.add_argument(
        "-s",
        "--source",
        default=os.getcwd,
        type=str,
        metavar="source",
        nargs=1,
        help="Files to symlink to."
    )

    parser.add_argument(
        '-V',
        '--version',
        metavar='version',
        action='version',
        version='%(prog)s' + __version__)


    args = parser.parse_args()

    return args


def main(i, j=os.getcwd):
    """Symlink user provided files."""
    for i in glob.glob("./**", recursive=True):
        if os.path.isfile(i):
            try:
                os.symlink(i, j)
            except FileExistsError:
                pass
            #  except OSError as e:
            #      print(e)


if __name__ == "__main__":
    args = _parse_arguments()
    dest = args.destination
    try:
        src = args.source
    except Exception:
        src = None

    main(i=dest, j=src)
