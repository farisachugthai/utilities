#!/usr/bin/env python3
# Maintainer: Faris Chugthai
"""Strip only trailing whitespace from a file.

Leading whitespace is significant in Python so don't touch it.


"""
import logging
from pathlib import Path
import shutil
import sys

logging.getLogger(name=__name__)


def backup(src):
    """Backs up a file before doing anything.

    Parameters
    ----------
    src : file
        File to strip trailing whitespace from. Backed up before anything.

    """
    try:
        shutil.copy(str(src), str(src) + ".bak")
    except (shutil.SameFileError, shutil.SpecialFileError) as e:
        logging.warning(e)


def strip_space(src=sys.stdin):
    """Strip all trailing whitespace out of a file.

    Assumes a plaintext file. Uses sys.stdin if no argument provided.

    Parameters
    ----------
    src : str
        File to strip trailing whitespace from. Backed up before anything.

    """
    logging.warning("Clearing whitespace...")

    with src.open("rt") as f:
        tmp = [line.rstrip() + "\n" for line in f if line != ""]

    with src.open("wt") as f:
        f.writelines(tmp)

    logging.warning("Done!")


def main():
    """Dispatch the strip_space function."""
    logging.basicConfig(level=logging.WARNING)

    if len(sys.argv) >= 2:
        file_list = sys.argv[1:]
        for i in file_list:
            backup(i)
            strip_space(i)

    elif len(sys.argv) == 2:
        src = Path(sys.argv[1])
        backup(i)
        strip_space(src)

    else:
        src = sys.stdin
        strip_space(src)


if __name__ == "__main__":
    main()
