#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://github.com/farisachugthai

All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = 'Faris Chugthai'
__copyright__ = 'Copyright (C) 2018 Faris Chugthai'
__license__ = 'MIT'
__email__ = 'farischugthai@gmail.com'

import os
import sys


# taken with almost no modifications from pyflakes
def iterSourceCode(paths):
    """
    Iterate over all Python source files in C{paths}.

    @param paths: A list of paths.  Directories will be recursed into and
        any .py files found will be yielded.  Any non-directories will be
        yielded as-is.
    """
    for path in paths:
        if os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    full_path = os.path.join(dirpath, filename)
                    yield full_path
        else:
            yield path


def dlink(dest, src):
    """
    Usage:
    Utilize in an analogous way to the shell command
    ln -s path/to/dir/* path/to/src/

    Parameters:
    Dest is the directory where the real files are located.
    src is the directory where the symlinks are to be created.
    If the src argument isn't provided, it is assumed that the current working
    directory is the src dir.
    """

    for i in os.listdir(dest):
        dest_file = os.path.join(dest, i)
        src_file = os.path.join(src, i)
        if os.path.isdir(dest_file) and not os.path.isdir(src_file):
            try:
                os.mkdir(src_file, 0o777)
            except Exception as e:
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
                          + "will not create a symlink.")
                    print(e)
            # you could totally make this a root logger if you wanted some
            # pointless noise otherwise let's spare our poor victims
            #  else:
            #      print("symlinking: " + dest_file + " from " + src_file)


def main():
    cwd = os.path.join(os.getcwd(), '')
    src = sys.argv[-1] if len(sys.argv) == 3 else cwd
    dest = sys.argv[1]

    if not os.path.isdir(dest):
        sys.exit("Dir: " + dest + " is not a recognized directory. Exiting.")

    #  print("Your variable src is: " + src + " and type: " + str(type(src)))
    #  print("Your variable dest is: " + dest + " and type: " + str(type(dest)))
    #  print("The files that we'll be symlinking to : " + str(os.listdir(dest)))

    dlink(dest, src=cwd)


if __name__ == '__main__':
    main()
