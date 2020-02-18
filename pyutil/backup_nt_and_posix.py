#!/usr/bin/env python
"""Backup a directory by appending the date and time and copying over.

===================
Backup NT and Posix
===================

.. highlight:: ipython

.. module:: backup_nt_and_posix

Motivation
----------
This script aims to be platform agnostic and in the long term will be used on
Windows, Linux, Mac and Android systems.

"""
import os
import subprocess
import sys
from time import strftime


def timestamped_dir(backup_dir, path="."):
    r"""Create a backup of a directory. Append date and time to new dir name.

    .. todo:: Change this so that it utilizes :func:`subprocess.check_call()` so we handle return codes in a better way.


    Parameters
    ----------
    backup_dir : str
        Directory to backup
    path : str, optional
        Directory to back up to. Defaults to cwd.

    Returns
    -------
    err_code : int
         Non-zero value indicates error code, or zero on success.
    err_msg : str or None
         Human readable error message, or None on success.

    """
    if os.name == "nt":
        shell_command = "move"

    elif os.name == "posix":
        shell_command = "mv"

    else:
        return [-1, "Not supported on %s platform" % os.name]

    cmd = subprocess.Popen(
        [shell_command, path, backup_dir],
        shell=True,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    (out, err) = cmd.communicate()

    if len(err) != 0:
        return [-1, err]

    else:
        os.mkdir(path)
        return [0, None]


if __name__ == "__main__":
    args = sys.argv[:]

    # if len(args) == 2:

    for directory in args[1:]:
        path = args[directory]

        if os.path.exists(path):
            backup_dir = path + strftime("-%Y-%m-%d-%Hh%Mm%Ss")
            timestamped_dir(backup_dir)
