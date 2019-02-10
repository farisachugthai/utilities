#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Rewriting rclone.sh as a python module.

.. code:: bash

    rclone.py [src] dst

Requires
---------
rclone

The remaining roadmap.

.. todo::

    - :param:`args` is used as a parameter to both :class:`argparse.ArgumentParser()` and
      :func:`subprocess.run()`
        - Switch the name for one of them as this'll get confusing quickly.
    - Set up a simple single use case backup.
    - Add :func:`collections.ChainMap()` to set precedence of backupdir.
    - Add in multiple invocations of rclone and create args to reflect use cases.
    - Expand :mod:`argparse` usage with :func:`argparse.fromfile_prefix_chars()`
     to emulate rsync's file input.

"""
import argparse
import os
import subprocess
import sys


def _parse_arguments():
    """Parse user-given arguments."""
    # parser = argparse.ArgumentParser("Automate usage of rclone for simple backup creation.")
    # parser.add_argument(dest=src, required=True, help='A directory, presumably local, to sync with a remote.')
    parser = argparse.ArgumentParser(
        usage="%(prog)s [options]",
        description="Automate usage of rclone for "
        "simple backup creation.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        src, default=cwd, help="The source directory. "
        "Defaults to the cwd.")

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
    cmd = [
        'rclone', 'copy', '--update', '--track-renames'
        '--copy-links', src, dst
    ]
    subprocess.run(cmd)


if __name__ == "__main__":
    cwd = os.getcwd()

    # This forces a Linux only implementation. Should expand the following to
    # a function
    home = os.path.expanduser("~")

    # Quite honestly most of everything below was garbage and needs to be
    # rewritten ground up.

    # Use :Glog if you want a reference of what was here.
    parser = _parse_arguments()

    parser.parse_args()
