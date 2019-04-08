#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Rewriting rclone.sh as a python module.

.. rubric:: Requires

`rclone`_, a Golang package.


.. todo::

    - Set up a simple single use case backup.
    - Add :func:`collections.ChainMap()` to set precedence of backupdir.
    - Expand :mod:`argparse` usage with :func:`argparse.fromfile_prefix_chars()` to emulate rsync's file input.
    - How do you correctly use :mod:`argparse` and ``**kwargs`` together?

.. _`rclone`: https://rclone.org

"""
import argparse
import logging
import os
import shlex
import subprocess
import sys


def _parse_arguments(cwd=None, **kwargs):
    """Parse user-given arguments."""
    if cwd is None:
        cwd = os.getcwd()

    parser = argparse.ArgumentParser(
        description="Automate usage of rclone for simple backup creation.")
    # parser.add_argument(dest=src, required=True, help='A directory, presumably local, to sync with a remote.')
    parser = argparse.ArgumentParser(
        usage="%(prog)s [options]",
        description="Automate usage of rclone for "
        "simple backup creation.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        action='store',
        dest='src',
        default=cwd,
        help="the source directory. "
        "defaults to the cwd.")

    parser.add_argument(
        "dst",
        help="The folder that the files should be backed up to."
        "Can be a remote instance as well. See rclone.org for "
        "all accepted values for this parameter")

    parser.add_subparsers(
        "config",
        required=False,
        help="Configure rclone. Additional options can't be specified;"
        "however, :mod:`pyutil.rclone` will halt execution as rclone is configured."
    )

    parser.add_argument(
        '-f',
        '--follow',
        action='store_true',
        default=False,
        dest='follow',
        help="Follow symlinks.")

    return parser


def run(cmd, **kwargs):
    """Execute the required command in a subshell.

    First the command is splited used typical shell grammer.

    A new process is created, and from the resulting subprocess object,
    the :func:`subprocess.Popen().wait()`.

    This function returns the return code of split ``cmd``, so any
    non-zero value will lead to a ``SystemExit`` with a passed value
    of ``returncode``.

    .. should i use **kwargs as a parameter here? If so, how do i mark that up in a docstring?

    Parameters
    ----------
    cmd : str
        The command to be called

    Returns
    -------
    process.returncode : int
        The returncode from the process.


    """
    cmd = shlex.split(cmd)
    logging.debug("Cmd is: " + str(cmd))
    process = subprocess.Popen(cmd, kwargs)

    if process.wait():
        raise SystemExit(process.returncode)
    else:
        return process.returncode


def _dir_checker(dir_):
    """Check that necessary directories exist.

    If the default `dst` doesn't exist, definitely create it.
    If the user provided `src` doesn't exist, crash without making one.

    It's more likely that they typed the src dir incorrectly rather than
    running the script aware of the fact that it is nonexistent.
    """
    if os.path.isdir(dir_):
        return True
    else:
        sys.exit(str(dir_) + 'does not exist. Exiting.')


def rclone_base_case(src, dst):
    """Base case that all other functions build off of.

    This function shouldn't be executed directly; however, it serves as a good
    template detailing a function and useful command with parameters that
    rclone uses.

    For example, ``--follow`` is a flag that has conditionals associated it with it.

    There are situations in which one wants to follow symlinks and others
    that they don't.

    This command assumes a use case and configures it rclone for it properly.

    .. todo:: rclone takes an argument for user-agent


    Parameters
    ----------
    src : str
        directory to clone files from

    dst : str
        destination to send files to. Can be configured as a local directory,
        a dropbox directory, a google drive folder or a google cloud storage
        bucket among many other things.

    """
    cmd = ['rclone', 'copy', '--update', '--track-renames', src, dst]
    run(cmd)


def rclone_follow(dst, src):
    """Follow symlinks.

    Parameters
    ----------
    src : str
        directory to clone files from

    dst : str
        destination to send files to. Can be configured as a local directory,
        a dropbox directory, a google drive folder or a google cloud storage
        bucket among many other things.


    .. See Also
    .. --------
    .. :ref:`pyutil.rclone.rclone_base_case()` for a more detailed explanation

    """
    cmd = [
        'rclone', 'copy', '--update', '--track-renames'
        '--copy-links', src, dst
    ]
    run(cmd)


def main():
    """Run module."""
    cwd = os.getcwd()

    try:
        home = os.path.expanduser("~")
    except OSError:
        home = os.environ.get('userprofile')

    # Quite honestly most of everything below was garbage and needs to be
    # rewritten ground up.

    # Use :Glog if you want a reference of what was here.
    parser = _parse_arguments(cwd)

    args = parser.parse_args()

    if args.src:
        src = args.src
    else:
        src = cwd

    assert args.dst

    dst = args.dst

    if args.follow:
        rclone_follow(dst, src)


if __name__ == "__main__":
    sys.exit(main())
