#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maintainer: Faris Chugthai

import sys
import shutil
from pathlib import Path
import os

home = Path.home()
repo = Path.joinpath(home, 'projects', 'dotfiles', 'unix', '')


# TODO: Remove hard coded path. argparse and set that as dedault option.
# Well looks like Ive already started with mv_repo2.py
def sys_checks():
    """Checks that system requirements are met."""
    if sys.version_info < (3, 4):
        sys.exit("Requires Python3.4 and up")

    if os.uname()[0] not in ["Darwin", "Linux"]:
        raise OSError("This script assumes a Unix operating system.")
        sys.exit()


def repo_dir_check(dest):
    """
    Checks that the directory is in the repository and make one otherwise.
    """

    if dest.is_dir() is not True:
        #  https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
        # To mimic behavior of mkdir -p, use flags parents=True and exists_ok=True
        dest.mkdir(parents=True, exist_ok=True)


def backup_file(src):
    """ Backs up file 'src' """
    # TODO: Look into pros/cons of copy/copy2/copyfile
    # TODO2: Should we do anything if src.bak already exists?
    shutil.copy(str(src), str(src) + ".bak")


def main(src, dest, dest_file):
    """
    Runs checks, calls func to backup file 'src', moves it to the dotfiles
    repo and symlinks it.
    Moves file to a hardcoded path but will be generalized to take as an argument.

    Parameters:
        Name of file to backup, move and symlink.

    Assumes:
        User runs the script from inside the folder of the file they want to
        move. As a result a pathname cannot be given to a file.
    """

    if src.is_file() is not True:
        sys.exit("This is not a file. Aborting.")

    sys_checks()
    repo_dir_check(dest)

    backup_file(src)

    shutil.move(str(src), str(dest))
    src.symlink_to(dest_file)


if __name__ == '__main__':
    """
    Determine if a file name is in the current directory or absolute path.
    Then set up a relative path from $HOME. Use the root of the repo as the new
    root and move the file there, all while creating directories and backups.

    Relatively long if __name__ block because we spend so much code handling
    user input that we don't deal with when the functions arebeing imported.
    """
    # Are we getting into argparse territory?
    # Setup the file to move
    inputted = sys.argv[1] if len(sys.argv) >= 2 else sys.exit("Takes at least one filename.")
    src = Path(inputted)
    if src.is_absolute:
        rel_path = Path.relative_to(home)
    else:
        cwd: Path = Path.cwd()
        rel_path = Path.relative_to(cwd, home)
    # Setup the file we're moving to
    dest = sys.argv[2] if len(sys.argv) == 3 else Path.joinpath(repo, rel_path)

    # TODO: Probably gonna need os.basepath if argv[1] was an absolute path.
    # possibly tp the effect of
    # dest_file = Path.joinpath(repo, rel_path, sys.argv[1].basename) but really not too sure
    dest_file = Path.joinpath(dest, sys.argv[1])

    main(src, dest, dest_file)
