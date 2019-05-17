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
import os
# from pathlib import Path
import subprocess

from pyutil.__about__ import __version__

# from pyutil.env_checks import get_home_3


def _parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "destination",
        type=str,
        metavar="destination",
        nargs='?',
        help="Files to symlink to.")

    parser.add_argument(
        "-s",
        "--source",
        default=os.getcwd(),
        type=str,
        metavar="source",
        nargs='?',
        help="Files to symlink to.")

    parser.add_argument(
        '-V', '--version', action='version', version='%(prog)s' + __version__)

    args = parser.parse_args()

    return args


def main(destination_dir, source_dir):
    """Symlink user provided files.

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
            #  except OSError as e:
            #      print(e)


def run(cmd=None):
    """Run a directory symlinker using Windows specific commands.

    Needs to check htat the user has admin access in order to create symlinks.

    Also what's up with ``NoneType`` being undefined? Like this implementation
    CAN'T be right.
    """
    NoneType = type(None)
    if isinstance(cmd, NoneType):
        return None
    elif not isinstance(cmd, list):
        cmd = cmd.split(' ')

    for i in os.listdir('.'):
        subprocess.run(cmd)


if __name__ == "__main__":
    # Side step everything for a moment
    # HACK
    from platform import system
    if system() == 'Windows':
        import sys
        cmd = sys.argv[1:]
        if len(cmd) >= 0:
            run(cmd)
        else:
            raise

    # Let's continue onwards as usual
    args = _parse_arguments()
    dest = args.destination
    try:
        src = args.source
    except Exception:
        src = None

    main(dest, src)
