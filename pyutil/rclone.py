#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Backup files using :ref:`rclone`.

======
rclone
======

.. rubric:: Requires

`rclone`_, a Golang package.


* Set up a simple single use case backup.
    * Realistically this should be more of the focus.
* However if it's not, then we could make a :class:`collections.defaultdict`
  that holds default values for each option.
  * Actually wouldn't :class:`configparser.ConfigParser` make more sense?
* In addition we could use :class:`collections.ChainMap()` to set
  precedence of `backupdir`.
* Expand :mod:`argparse` usage with :func:`argparse.fromfile_prefix_chars()`
  to emulate rsync's file input.

.. _`rclone`: https://rclone.org

"""
import argparse
import logging
import os
import shlex
import shutil
import subprocess
import sys

from pyutil.__about__ import __version__

LOG_LEVEL = "logging.WARNING"


def _parse_arguments(cwd=None, **kwargs):
    """Parse user-given arguments."""
    if cwd is None:
        cwd = os.getcwd()

    parser = argparse.ArgumentParser(
        description="Automate usage of rclone for "
        "simple backup creation.")

    parser.add_argument(action='store',
                        dest='src',
                        default=cwd,
                        metavar='source_dir',
                        help="The source directory. Defaults to the cwd.")

    parser.add_argument(
        "dst",
        action='store',
        metavar='dest_directory',
        help="The folder that the files should be backed up to."
        "Can be a remote instance as well. See rclone.org for "
        "all accepted values for this parameter")

    # config = parser.add_subparsers(
    #     help="Configure rclone. Additional options can't be specified;"
    #     "however, :mod:`pyutil.rclone` will halt execution as rclone is configured."
    # )

    parser.add_argument(
        '-ll',
        '--log_level',
        dest='log_level',
        metavar='log_level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Set the logging level')

    parser.add_argument('-f',
                        '--follow',
                        action='store_true',
                        default=False,
                        help="Follow symlinks.")

    parser.add_argument('-V',
                        '--version',
                        action='version',
                        version='%(prog)s' + __version__)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        return parser.parse_args()


def _set_debugging():
    """Enable debug logging."""
    root = logging.getLogger(name=__name__)
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)


def run(cmd, **kwargs):
    """Execute the required command in a subshell.

    First the command is splited used typical shell grammer.

    A new process is created, and from the resulting subprocess object,
    the :func:`subprocess.Popen().wait()`.

    This function returns the return code of split `cmd`, so any
    non-zero value will lead to a ``SystemExit`` with a passed value
    of ``returncode``.

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


# uhhh how do we implememt this
class CloudProvider():
    """Emulate the provider rclone is syncing to."""

    @property
    def url(self):
        logging.debug("URL was: " + self.url)

    @url.setter
    def url(self):
        logging.debug("Old URL was: " + self.url)
        # set it
        logging.debug("New URL is: " + self.url)


def main():
    """Receive user arguments and begin executing module appropriately."""
    cwd = os.getcwd()
    args = _parse_arguments(cwd)

    try:
        log_level = args.log_level
    except AttributeError:  # IndexError?
        logging.basicConfig(level=LOG_LEVEL)
    else:
        logging.basicConfig(level=log_level)

    if args.src:
        src = args.src
    else:
        src = cwd

    dst = args.dst

    if args.follow:
        rclone_follow(dst, src)


if __name__ == "__main__":
    # This feels like a necessary stop-gap
    if not shutil.which('rclone'):
        sys.exit('rclone not in $PATH. Exiting.')

    sys.exit(main())
