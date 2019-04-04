#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Temporary module holding rewrites to dlink.

This module will be renamed in the future. For the time being it's a testing ground for rewriting the dlink module.

For this script, I'm attempting to try exclusively using :mod:`pathlib`.

"""
import argparse
from pathlib import Path
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
        default=Path.cwd(),
        metavar="source",
        nargs='?',
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


def main():
    """Symlink user provided files."""
    args = _parse_arguments()
    dest = args.destination
    try:
        src = args.source
    except IndexError:
        src = None
    cwd = Path()
    for i in glob.glob("./**", recursive=True):
        if os.path.isfile(i):
            try:
                os.symlink(i, j)
            except FileExistsError:
                pass
            #  except OSError as e:
            #      print(e)


if __name__ == "__main__":
    sys.exit(main())
