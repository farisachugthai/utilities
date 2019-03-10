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
        print(e)


def strip_space(src):
    """Strips all trailing whitespace out of a file.

    Parameters
    ----------
    src : file
    File to strip trailing whitespace from. Backed up before anything.

    Returns
    -------
    None

    """
    print("Clearing whitespace...")

    with src.open('r') as f:
        tmp = [line.rstrip() + '\n' for line in f]

    with src.open('w') as f:
        f.writelines(tmp)

    print("Done!")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: strip_space.py file_obj")
    else:
        src = Path(sys.argv[1])

    if not Path.is_file(src):
        sys.exit()

    backup(src)

    strip_space(src)
