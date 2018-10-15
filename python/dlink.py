#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Symlink all of the files in one directory into another.

Usage::
    `<ln -s path/to/dest/* [path/to/src]>`

This module is intended to be used in the same fashion as
in a conventional Unix shell

Bugs::
    Doesn't work if nested directories need to be made.
    Although I suppose the original purpose of this was to replicate
    ln -s dest/*

"""
__author__ = 'Faris Chugthai'
__copyright__ = 'Copyright (C) 2018 Faris Chugthai'
__email__ = 'farischugthai@gmail.com'
__license__ = 'MIT'
__url__ = 'https://github.com/farisachugthai'

import os
import sys


# this would be a great function to call with the results of os.listdir('root')
# taken with almost no modifications from pyflakes
def iter_source_code(paths):
    """Iterate over all Python source files in C{paths}.

    Directories will be recursed into and any .py files found will be yielded.
    Any non-directories will be yielded as-is.

    :param paths: A list of paths.

    :returns: fname
    """
    for fname in paths:
        if os.path.isdir(fname):
            for dirpath, dirnames, filenames in os.walk(fname):
                for filename in filenames:
                    absolute_path = os.path.join(dirpath, filename)
                    yield absolute_path
        else:
            yield fname


def dlink(dest, src):
    """Symlinks all files in one directory from another.

    Utilize in an analogous way to the shell command ln -s ./*

    Usage::
        ln -s path/to/dir/* path/to/src/

    :param dest: The directory where the original files are located.
    :param src: Optional argument indicating the directory where the symlinks
    are to be created.

    If the src argument isn't provided, it is assumed that the current working
    directory is the src dir.

    Returns::
        None

    Bugs::
        Doesn't handle nested directories.

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


def main():
    """Set up the rest of the module."""
    cwd = os.path.join(os.getcwd(), '')
    src = sys.argv[-1] if len(sys.argv) == 3 else cwd

    try:
        dest = sys.argv[1]
    except IndexError:
        sys.exit("What directory do you want to link to?")

    if not os.path.isdir(dest):
        sys.exit("Dir: " + dest + " is not a recognized directory. Exiting.")

    dlink(dest, src)


if __name__ == '__main__':
    main()
