#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Rewriting rclone.sh as a python module.

Usage::
    TODO

Requires::
    rclone

Roadmap is to set up a simple single use case backup.

Add collections.ChainMap() to set precedence of backupdir.

Add in multiple invocations of rclone and create args to reflect use cases.

Expand argparse usage with `fromfile_prefix_chars` to emulate rsync's file
input.
"""
import argparse
import os
from platform import machine
import subprocess


def _parse_arguments():
    """Parse user-given arguments."""
    parser = argparse.ArgumentParser(usage="%(prog)s [options]",
                                     description="Automate usage of rclone for \
                                     simple backup creation.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter
                                     )
    parser.add_argument(dest=src, default=cwd, help="The source directory.\
                        Defaults to the cwd.")

    return parser


def rclone_base_case():
    """Noop. Simply here to track the best command to use."""
    pass


# TODO: Change dest to dst because argparse takes dest
def rclone_follow(dest, src=cwd):
    """Follow symlinks."""
    args = ['rclone', 'copy', '--update', '--copy-links', src, dest]
    subprocess.run(args)


if __name__ == "__main__":

    cwd = os.getcwd()
    home = os.path.expanduser("~")

    # HACK
    # Determine device is an Android from CPU arch. Set backups appropriately
    if machine == 'aarch64':
        dest = '/sdcard/backups'
    elif machine == 'amd64':
        dest = os.path.join(home, 'backups')

    args = _parse_arguments()
    args.parse_args()

    if args.follows:
        rclone_follow(dest, src=cwd)
