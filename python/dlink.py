#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Symlink all of the files in one directory into another.

Usage::
    `ln -s path/to/dest/* [path/to/src]`

This module is intended to be used in the same fashion as
in a conventional Unix shell

Bugs::
    Doesn't work if nested directories need to be made.
    Although I suppose the original purpose of this was to replicate
        `ln -s dest/*`
    Not arbitrarily start adding in globbing/recursive functionality.

"""
__author__ = 'Faris Chugthai'
__copyright__ = 'Copyright (C) 2018 Faris Chugthai'
__email__ = 'farischugthai@gmail.com'
__license__ = 'MIT'
__url__ = 'https://github.com/farisachugthai'

import os
import sys


def dlink(dest, src):
    """Symlinks all files in one directory from another.

    Utilize in an analogous way to the shell command ln -s ./*

    Usage::
        ln -s path/to/dir/* path/to/src/

    :param: dest: The directory where the original files are located.
    :param: src: Optional argument indicating the directory where the symlinks
    are to be created.

    If the src argument isn't provided, it is assumed that the current working
    directory is the src dir.

    Returns:
        None
    """
    for i in os.listdir(dest):
        dest_file = os.path.join(dest, i)
        src_file = os.path.join(src, i)
        if os.path.isdir(dest_file) and not os.path.isdir(src_file):
            try:
                os.mkdir(src_file, 0o777)
            except IsADirectoryError as e:
                sys.exc_info()
                print(e)

        elif os.path.isfile(dest_file):
            try:
                os.symlink(dest_file, src_file)
            except FileExistsError as e:
                if os.path.islink(src_file):
                    pass
                elif os.path.isfile(src_file):
                    print(src_file + " is already a file in the src dir. We "
                                     "will not create a symlink.")
                    print(e)
            # you could totally make this a root logger if you wanted some
            # pointless noise otherwise let's spare our poor victims
            #  else:
            #      print("symlinking: " + dest_file + " from " + src_file)


if __name__ == '__main__':
    # Main has been refactored out because there's no reason to have
    # global vars defined in main. Let's have less function calls
    # and only define these variables if we're not being sourced.
    cwd = os.path.join(os.getcwd(), '')
    src = sys.argv[-1] if len(sys.argv) == 3 else cwd

    try:
        dest = sys.argv[1]
    except IndexError:
        sys.exit("What directory do you want to link to?")

    if not os.path.isdir(dest):
        sys.exit("Dir: " + dest + " is not a recognized directory. Exiting.")

    dlink(dest, src)