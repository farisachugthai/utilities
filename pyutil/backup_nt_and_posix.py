#!/usr/bin/env python
"""Backup a directory by appending the date and time and copying over.

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
    backup_dir : path-like object
        Directory to backup

    Returns
    -------
    return_code, error message : list

    The specific implementation of this is as follows.

    None: NoneType
        No error.
    0: Int
        Success
    -1 : Int
        Failure
    error : string
        the exact error string

    .. todo:: Change this so that it utilizes :func:`subprocess.check_call()` and we handle return codes in a better and more *true to form* way.

    """
    if os.name == "nt":
        shell_command = "move"

    elif os.name == "posix":
        shell_command = "mv"

    else:
        return [-1, "Not supported on %s platform" % (os.name)]

    cmd = subprocess.Popen([shell_command, path, backup_dir],
                           shell=True,
                           stdout=subprocess.PIPE,
                           stdin=subprocess.PIPE,
                           stderr=subprocess.PIPE)

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
