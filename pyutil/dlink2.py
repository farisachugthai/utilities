#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Possibly rewrote the entire module in half as many lines.

Now utilizes necessary libraries like glob.

TODO:
    Argparse?

    .. note:

        I was just in ~/.config/nvim trying to symlink my dots from ~/projects/viconf/.config/nvim and running::

            dlink2.py ~/projects/viconf/.config/nvim while in ~/.config/nvim did nothing at all.
"""
import glob
import os
import sys


def main(i, j=os.getcwd):
    """Symlink user provided files."""
    for i in glob.glob("./**", recursive=True):
        if os.path.isfile(i):
            try:
                os.symlink(i, j)
            except FileExistsError:
                pass
            #  except OSError as e:
            #      print(e)


if __name__ == "__main__":
    args = sys.argv[:]
    if len(args) == 3:
        j = args[1]
        i = args[2]
        main(i, j)
    elif len(args) == 2:
        i = args[1]
        main(i)
    else:
        # TODO:
        print("Usage: ")
