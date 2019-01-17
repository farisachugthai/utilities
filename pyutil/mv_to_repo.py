#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Moves files from anywhere in the home directory to the dotfiles repo.

This is a script I've been using for the better part of a year, so while
the docstring formatting isn't consistent and there are a couple odd sections,
this script has served a very utilitiarian purpose.

May refactor one day. But it continues to work.
"""
import os
from pathlib import Path
import shutil
import sys


def sys_checks():
    """Checks that system requirements are met."""
    if sys.version_info < (3, 4):
        sys.exit("Requires Python3.4 and up")

    if os.uname()[0] not in ["Darwin", "Linux"]:
        raise OSError("This script assumes a Unix operating system.")
        sys.exit()


def repo_dir_check(dest):
    """Checks that the directory is in the repository and make one otherwise."""

    if dest.is_dir() is not True:
        #  https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
        # To mimic behavior of mkdir -p, use flags parents=True and exists_ok=True
        dest.mkdir(parents=True, exist_ok=True)


def backup_file(src):
    """Backs up file 'src' """
    # TODO: Look into pros/cons of copy/copy2/copyfile
    # TODO2: Should we do anything if src.bak already exists?
    shutil.copy(str(src), str(src) + ".bak")


def main():
    """Dispatch the remaining implementation of the module.

    Determine if a file name is in the current directory or absolute path.
    Then set up a relative path from $HOME. Use the root of the repo as the new
    root and move the file there, all while creating directories and backups.

    Runs checks, calls func to backup file 'src', moves it to the dotfiles
    repo and symlinks it.
    Moves file to a hardcoded path but will be generalized to take as an argument.

    Parameters:
        Name of file to backup, move and symlink.

    Assumes:
        User runs the script from inside the folder of the file they want to
        move.
    """
    sys_checks()
    inputted = sys.argv[1] if len(sys.argv) >= 2 else sys.exit("Takes at least one filename.")
    src = Path(inputted)

    if src.is_file() is not True:
        sys.exit("This is not a file. Aborting.")

    cwd: Path = Path.cwd()
    rel_path = Path.relative_to(cwd, home)
    # Setup the file we're moving to
    dest = sys.argv[2] if len(sys.argv) == 3 else Path.joinpath(repo, rel_path)

    dest_file = Path.joinpath(dest, inputted)
    repo_dir_check(dest)

    backup_file(src)

    shutil.move(str(src), str(dest))
    src.symlink_to(dest_file)


if __name__ == '__main__':
    home = Path.home()
    repo = Path.joinpath(home, 'projects', 'dotfiles', 'unix', '')
    main()
