#!/usr/bin/env python3
# Maintainer: Faris Chugthai
"""Strip only trailing whitespace from a file.

Leading whitespace is significant in Python so don't touch it.

Python Requirement
------------------
<Python 3.4

Still need to implement
-----------------------
Give some kind of undo option.
Needs more file checks.

"""
import logging
from pathlib import Path
import shutil
import sys


def backup(src):
    """Backs up a file before doing anything.

    Parameters
    ----------
    src : file
        File to strip trailing whitespace from. Backed up before anything.

    Returns
    -------
    None

    """
    try:
        shutil.copy(str(src), str(src) + ".bak")
    except (shutil.SameFileError, shutil.SpecialFileError) as e:
        logging.warning(e)


def strip_space(src=sys.stdin):
    """Strip all trailing whitespace out of a file.

    Assumes a plaintext file. Uses :ref:`sys.stdin` if no argument provided.

    Parameters
    ----------
    src : str
        File to strip trailing whitespace from. Backed up before anything.

    Returns
    -------
    None

    """
    logging.warning("Clearing whitespace...")

    with src.open('rt') as f:
        tmp = [line.rstrip() + '\n' for line in f if line != ""]

    with src.open('wt') as f:
        f.writelines(tmp)

    logging.warning("Done!")


def main(file_obj):
    """Dispatch :ref:`pyutil.strip_space.strip_space()`."""
    if not Path.is_file(file_obj):
        sys.exit("File is not readable. Exiting.")

    backup(file_obj)
    strip_space(file_obj)


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING)

    if len(sys.argv) >= 2:
        file_list = sys.argv[1:]
    elif len(sys.argv) == 2:
        src = Path(sys.argv[1])
    else:
        # How do I set this up right? Do I set src = None?
        pass

    for i in file_list:
        main(i)
