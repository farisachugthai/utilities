#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maintainer: Faris Chugthai
""" Move a file into my dotfiles repository.

Dude fuck I gotta debug this :\

Depends:
    sys_checks

Assumes:
    Script is executed in the same directory the file is in

"""

import argparse
import os
from pathlib import Path
import shutil
import sys

import sys_checks


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

    src = Path(args.fname)
    dirname = os.path.dirname(src)
    rel_path = Path.relative_to(dirname, home)
    # turn the str into a path object
    dest = Path(args.destination)


    # i feel like the below line HAS to be wrong. we need to use relpath to
    # go from src to home. then we already know the distance from home to dest. it's the
    # original distance [ the relpath ] plus any prefix before teh dotfiles repo.
    # this is very not ready to handle user input jesus.
    # you're overcomplicating both of these files.
    # stop trying to implement 2 things

    # this file should either use the hardcoded path because otherwise how do we know what the
    # repository structure we're going to is or go all user input
    # but don't do both in the same file man

    # dest_file should have the repo dir. then add on the relative path thing [because the repo structure is
    # mirrored on your local FS
    # then fname itself
    # if no argument was provided than at this point dest actually is repo
    # oh shit so all we were missing in the rel_path! and it's being noted as not used up there
    # rel_path kinda only makes sense if dest was provided as user input though....
    dest_file = Path.joinpath(dest, rel_path, args.fname)

    dest_dir = Path(os.path.dirname(dest_file))

    if dest_dir.is_dir() is not True:
        dest.mkdir(parents=True, exist_ok=True)

    shutil.copy(str(src), str(src) + ".bak")
    shutil.move(str(src), str(dest))

    src.symlink_to(dest_file)


if __name__ == '__main__':
    # Check that the system can run this script first
    sys_checks.main()

    # Keep all global modules in this loop
    home = Path.home()
    # might be more aptly named dest dir
    repo = Path.joinpath(home, 'projects', 'dotfiles', 'unix', '')
    cwd = os.getcwd()

    # Now let's parse the user's arguments
    parser = argparse.ArgumentParser(add_help=True, allow_abbrev=True,
                                     description='Moves a file into a new'
                                     'directory and then symlinks back'
                                     'from the original location. useful for'
                                     'managing dotfiles.')

    parser.add_argument('fname', help='The file to move to the dotfiles repo')

    parser.add_argument('-d', '--destination', default=repo,
                        help='The directory to put the file in. Defaults to' +
                        'the location of my dotfiles repository')

    args = parser.parse_args()

    if src.is_file() is not True:
        sys.exit("This is not a regular file or there is a permissions" +
                 "issue. Aborting.")
    main()

    if args.fname not in os.listdir(cwd):
        print('some kind of warning')
        raise Exception         # did we forget how to raise exceptions?
