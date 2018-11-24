#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Rewriting rclone.sh as a python module.

Usage::

.. code:: bash

    rclone.py [src] dst

.. requires::

    rclone

Roadmap:
    - Set up a simple single use case backup.
    - Add collections.ChainMap() to set precedence of backupdir.
    - Add in multiple invocations of rclone and create args to reflect use cases.
    - Expand argparse usage with `fromfile_prefix_chars` to emulate rsync's file input.

.. todo::

    - :param: args is used as a parameter to both ArgumentParser() and
      subprocess.run()
        - Switch the name for one of them as this'll get confusing quickly.
"""
import argparse
import os
from platform import machine
import subprocess
import sys


def _parse_arguments():
    """Parse user-given arguments."""
    # parser = argparse.ArgumentParser("Automate usage of rclone for simple backup creation.")
    # parser.add_argument(dest=src, required=True, help='A directory, presumably local, to sync with a remote.')
    parser = argparse.ArgumentParser(usage="%(prog)s [options]",
                                     description="Automate usage of rclone for \
                                     simple backup creation.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter
                                     )
    parser.add_argument(dest=src, default=cwd, help="The source directory.\
                        Defaults to the cwd.")

    return parser


def _dir_checker(dir_):
    """Check that necessary directories exist.

    If the default dst doesn't exist, definitely create it.
    If the user provided src doesn't exist, crash without making one.

    It's more likely that they typed the src dir incorrectly rather than
    running the script aware of the fact that it is nonexistent.
    """
    if os.path.isdir(dir_):
        return True
    else:
        sys.exit(str(dir_) + 'does not exist. Exiting.')


def rclone_base_case(src, dst):
    """Noop. Simply here to track the best and most general command to use.

    For example, --follow is a flag that has conditionals associated it with it.

    There are situations in which one wants to follow symlinks and others
    that they don't.

    This command assumes a use case and configures it rclone for it properly.

    .. todo::

        - rclone takes an argument for user-agent

    Parameters
    ----------
    src : directory to clone files from
    dst : destination to send files to. Can be configured as a local directory,
          a dropbox directory, a google drive folder or a google cloud storage
          bucket among many other things.

    Returns
    -------
    None.
    """
    cmd = ['rclone', 'copy', '--update', '--track-renames', src, dst]
    subprocess.run(cmd)


def rclone_follow(dst, src=cwd):
    """Follow symlinks."""
    cmd = ['rclone', 'copy', '--update', '--track-renames' '--copy-links', src, dst]
    subprocess.run(cmd)


if __name__ == "__main__":
    cwd = os.getcwd()

    # This forces a Linux only implementation. Should expand the following to
    # a function
    home = os.path.expanduser("~")

    # HACK
    # Determine device is an Android from CPU arch. Set backups appropriately
    if machine == 'aarch64':
        dest = '/sdcard/backups'
    elif machine == 'amd64':
        dest = os.path.join(home, 'backups')

    args = _parse_arguments()
    args.parse_args()

    # TODO: This gets outstandingly hard to follow from here and below.
    src = args.src
    dst = args.dst

    if args.follows:
        rclone_follow(dest, src=cwd)
    rclone_follow(src, dest)

    # No matter which one we pick, check it exists.
    _dir_check(dst)
    args = _parse_arguments()
    args.parse_args()

    if args.follows:
        rclone_follow(src, dst)

    else:
        rclone_base_case(src, dst)
    rclone_follow(src, dest)
    # No matter which one we pick, check it exists.
    _dir_check(dst)
    args = _parse_arguments()
    args.parse_args()

    if args.follows:
        rclone_follow(src, dst)

    else:
        rclone_base_case(src, dst)
    rclone_follow(src, dest)
