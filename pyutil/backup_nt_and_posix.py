#!/usr/bin/env python
"""Backup a directory by appending the date and time and copying over.

:mod:`backup_nt_and_posix`
==========================

Motivation
----------

This script aims to be platform agnostic and in the long term will be used
on Windows, Linux, Mac and Android systems.

Usage
------

.. code-block:: bash

    python backup_nt_and_posix.py /path/to/dir

.. todo::

    Consider rewriting using classes to hold state based on OS.
    Then utilize :mod:`pathlib`.
"""
import os
import subprocess
import sys
from time import strftime


def timestamped_dir(backup_dir):
    r"""Create a backup of a directory. Append date and time to new dir name.

    Parameters
    ----------
    backup\_dir : Directory to backup

    Returns
    -------
    None: means no error occurred.
    0: to signify the success
    -1 : to signify the failure
    error string: the exact error string
    """

    # Windows Specific Implementation
    if os.name == "nt":
        cmd = subprocess.Popen(["move", path, backup_dir],
                               shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    # POSIX
    elif os.name == "posix":
        cmd = subprocess.Popen(["mv", path, backup_dir],
                               shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    else:
        return [-1, "Not supported on %s platform" % (os.name)]

    (out, err) = cmd.communicate()

    if len(err) != 0:
        return [-1, err]

    else:
        os.mkdir(path)
        return [0, None]


if __name__ == "__main__":
    args = sys.argv[:]

    path = args[1]

    if os.path.exists(path):
        backup_dir = path + strftime('-%Y-%m-%d-%Hh%Mm%Ss')
        timestamped_dir(backup_dir)
