#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Possibly rewrote the entire module in half as many lines.

Now utilizes necessary libraries like glob.
Should add pathlib in here for a nice one stop shop for symlinking, getting
relative paths, symlinks and globs.

.. versionchanged:: Added argparse

04/25/2019:

Well now this is going to be the testing ground for getting a version of this
script functional on Windows!

"""
import argparse
import glob
import logging
import os
from pathlib import Path
import sys
# import subprocess

from pyutil.__about__ import __version__

logging.basicConfig(level=logging.DEBUG)


def _parse_arguments():
    parser = argparse.ArgumentParser(prog='Directory Linker 2.0',
                                     description=__doc__)

    parser.add_argument(
        "destination",
        metavar="destination",
        nargs='?',
        type=Path,
        help="Files to symlink to.")

    parser.add_argument(
        "-s",
        "--source",
        metavar="source",
        nargs='?',
        help="Where to create the symlinks. Defaults to the cwd.")

    parser.add_argument(
        '-V', '--version', action='version', version='%(prog)s' + __version__)

    logging.debug("Dir(parser): {} ".format(dir(parser)))

    if len(sys.argv) == 1:
        parser.print_usage()
        sys.exit()
    else:
        return parser.parse_args()


def main(destination_dir, source_dir):
    """Symlink user provided files.

    The module doesn't immediately check for correct permissions or operating system.

    As a result, the onus is put on the user to ensure that the necessary requirements
    per OS are met. Namely on Windows 10, that if symlinks are allowed on the filesystem,
    they can only be created by an administrator.

    If we're refactoring for pathlib check out what we have to work with.::

        :func:`pathlib.glob`
        :func:`pathlib.iterdir`
        :func:`pathlib.rglob`

    Holy cow. I mean call that a wrap right? Let's spend some time dissecting
    the information we're given via argparse and log it if necessary, but after
    running a recursive glob on the destination then we should easily be able
    to handle the rest.


    Parameters
    ----------
    destination_dir : str
         Directory where symlinks point to.
    source_dir : str, optional
        Directory where symlinks are created.

    """
    for i in glob.glob(destination_dir + "/**", recursive=True):
        if os.path.isfile(i):
            source_file = os.path.join(source_dir, i)
            try:
                os.symlink(i, source_file)
            except FileExistsError:
                pass
            except OSError:
                print("Ensure that you are running this script as an admin"
                      " if it's being run on Windows!")
                raise RuntimeError


if __name__ == "__main__":
    args = _parse_arguments()

    dest = args.destination

    try:
        src = args.source
    except IndexError:
        src = Path().cwd()
    # except Exception: logger.error('what happened'); sys.exit()

    main(dest, src)
    # TODO: add recursive as a parameter
