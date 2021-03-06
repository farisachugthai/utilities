#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import shutil
import sys


def ensure_dir_exists(dest):
    """Check that the directory is in the repository and make one otherwise.

    `Useful info about mkdir <https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir>`_:

        To mimic behavior of ``mkdir -p``, use flags ``parents=True`` and
        ``exists_ok=True``


    Parameters
    ----------
    dest : str
        Checks that the file to move has a corresponding directory in the repo


    """
    if dest.is_dir() is not True:
        dest.mkdir(parents=True, exist_ok=True)


def backup_file(src):
    """Backs up file src. Utilizes :func:`shutil.copy2`.

    Parameters
    ----------
    src : str
        File to backup

    """
    shutil.copy2(src, src + ".bak")


def main():
    """Dispatch the remaining implementation of the module.

    Determine if a file name is in the current directory or absolute path.

    Then set up a relative path from :envvar:`HOME`. Use the root of the repo
    as the new root and move the file there, all while creating
    directories and backups.

    Runs checks, calls func to backup file `src`, moves it to the dotfiles
    repo and symlinks it.

    Moves file to a hardcoded path but will be generalized to take as an
    argument.

    .. rubric:: Assumes

    User runs the script from inside the folder of the file they want to move.

    """
    src = Path(
        sys.argv[1] if len(sys.argv) >= 2 else sys.exit("Takes at least one filename.")
    )

    if src.is_file() is not True:
        print("This is not a file. Aborting.")
        return

    rel_path = Path.relative_to(Path.cwd(), Path.home())
    # Setup the file we're moving to
    dest = sys.argv[2] if len(sys.argv) == 3 else Path.joinpath(repo, rel_path)

    dest_file = Path.joinpath(dest, inputted)
    ensure_dir_exists(dest)

    backup_file(src)

    shutil.move(str(src), str(dest))
    src.symlink_to(dest_file)


if __name__ == "__main__":
    home = Path.home()
    repo = Path.joinpath(home, "projects", "dotfiles", "unix", "")
    main()
