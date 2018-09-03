#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maintainer: Faris Chugthai
""" Move a file into my dotfiles repository.

Depends:
    sys_checks

Assumes:
    Dotfiles directory is at ~/projects/dotfiles
    Script is executed in the same directory the file is in

"""

import argparse
import os
from pathlib import Path
import shutil
import sys

from . import sys_checks


def main():
    """ Move a file to my local dotfiles repo.

    Determine if a file name is in the current directory or absolute path.
    Then set up a relative path from $HOME. Use the root of the repo as the new
    root and move the file there, all while creating directories and backups.

    Runs checks, calls func to backup file 'src', moves it to the dotfiles
    repo and symlinks it.
    Moves file to a hardcoded path but will be generalized to take an argument.

    Parameters:
        Name of file to backup, move and symlink.

    Assumes:
        User runs the script from inside the folder of the file they want to
        move.

    """

    cwd = Path.cwd()
    rel_path = Path.relative_to(cwd, home)
    dest = args.destination
    dest_file = Path.joinpath(dest, args.fname)

    # Quite honestly this is so declarative that there's not any point to
    # creating functions for this
    #  https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
    # To mimic behavior of mkdir -p, use parents=True and exists_ok=True
    if dest.is_dir() is not True:
        dest.mkdir(parents=True, exist_ok=True)

    # TODO: Which shutill.copy and what errors do either of these functions raise?
    shutil.copy(str(src), str(src) + ".bak")
    shutil.move(str(src), str(dest))

    src.symlink_to(dest_file)


if __name__ == '__main__':
    # Check that the system can run this script first
    sys_checks()

    # Keep all global modules in this loop
    home = Path.home()
    repo = Path.joinpath(home, 'projects', 'dotfiles', 'unix', '')

    # Now let's parse the user's arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('fname', help='The file to move to the dotfiles repo')
    parser.add_argument('-d', '--destination', default=repo,
                        help='The directory to put the file in. Defaults to' +
                        'the location of my dotfiles repository')
    # TODO:
    # parser.add_argument('-v','--verbose', help='Increase verbosity')
    args = parser.parse_args()

    if args.fname.is_file() is not True:
        sys.exit("This is not a regular file or there is a permissions" +
                 "issue. Aborting.")
    main()
