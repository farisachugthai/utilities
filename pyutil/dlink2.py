#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Utilize argparse, pathlib and IPython to generate symlinks.

=========================
Directory Linker Rewrite
=========================

.. module:: dlink2

.. highlight:: python

.. versionchanged:: Added argparse

This is a rewrite of a script I've had for years, so I decided to go above
and beyond.


See Also
---------
:func:`IPython.utils.path.ensure_dir_exists()` : function
    Check for a dir and create it if it doesn't exist.

"""
import argparse
import logging
import sys
from pathlib import Path

try:
    from IPython.core.error import UsageError
    from IPython.utils.path import ensure_dir_exists
except (ImportError, ModuleNotFoundError):

    class UsageError(Exception):
        pass

    # TODO
    # def ensure_dir_exists(dir):

from pyutil.__about__ import __version__


class PermissionsError(OSError):
    """Symlinking error typically from Windows."""
    pass


def _parse_arguments():
    parser = argparse.ArgumentParser(
        prog='Directory Linker 2.0',
        description="Iterate over a `dest` folder"
        " and create symlinks in directory "
        "`source`. If `source` is not provided use"
        " current working directory."
    )

    parser.add_argument(
        "destination",
        metavar="destination",
        nargs='?',
        type=Path,
        help="Files to symlink to."
    )

    parser.add_argument(
        "-s",
        "--source_directory",
        metavar="SOURCE_DIRECTORY",
        dest='source',
        nargs='?',
        default=Path().cwd(),
        help="Where to create the symlinks. Defaults to the cwd."
    )

    parser.add_argument(
        '-g',
        '--glob-pattern',
        metavar='GLOB_PATTERN',
        help='Filter files in the destination dir with a glob pattern.'
    )

    parser.add_argument(
        '-r',
        '--recursive',
        action='store_true',
        default=False,
        help=
        "Whether to recursively symlink the child directories below the destination folder as well."
    )

    parser.add_argument(
        '-V', '--version', action='version', version='%(prog)s' + __version__
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        return parser


def generate_dest(dest, glob_pattern=None):
    """Return a generator for all the files in the destination directory."""
    if not ensure_dir_exists(dest):
        logging.error('%s' % dest, exc_info=1)
    if glob_pattern:
        yield Path(dest).glob(glob_pattern)
    else:
        yield Path(dest).glob('*')


def get_basenames(directory):
    """Get the basenames of all the files in a directory."""
    return [i.stem + i.suffix for i in directory.iterdir()]


def dlink(destination_dir, source_dir, is_recursive=False, glob_pattern=None):
    """Symlink user provided files.

    The module doesn't immediately check for correct permissions or
    operating system.

    As a result, the onus is put on the user to ensure that the necessary
    requirements per OS are met.

    Namely on Windows 10, that if symlinks are allowed on the filesystem,
    whether they can only be created by an administrator. Recent enough
    versions of Windows 10 have introduced the ability for regular users
    to create symlinks as well as admins.

    Parameters
    ----------
    destination_dir : str
         Directory where symlinks point to.
    source_dir : str, optional
        Directory where symlinks are created.
    recursive : bool, optional
        Whether to recursively symlink directories beneath the
        `destination_dir`. Defaults to False.
    glob_pattern : str
        Only symlink files that match a certain pattern.

    """
    base_destination_files = sorted(get_basenames(destination_dir))

    full_destination_files = sorted([j for j in destination_dir.iterdir()])

    full_source_files = sorted(
        Path(source_dir).joinpath(i) for i in base_destination_files
    )

    for idx, src_file in enumerate(full_source_files):
        logging.debug('\ni is {0!s}'.format(src_file))
        logging.debug(
            '\nfull_destination_files is {!s}'.format(full_destination_files)
        )
        logging.debug('\nfull_source_files is {!s}'.format(full_source_files))
        logging.debug('\nsource_dir is {}'.format(source_dir))
        logging.debug(
            '\nbase_destination_files: {!r}'.format(base_destination_files)
        )
        logging.info("idx: {}\tsrc_file: {}\t".format(idx, src_file))
        if full_destination_files[idx].is_dir():
            src_dir = Path(src_file)
            if not src_dir.exists():
                src_dir.mkdir(755)

            # then call it recursively
            if src_file.is_dir():
                dlink(
                    destination_dir=src_file,
                    source_dir=source_dir.joinpath(src_file),
                    is_recursive=is_recursive,
                    glob_pattern=glob_pattern
                )

        else:
            symlink(src_file, full_destination_files[idx])


def symlink(src, dest):
    """Execute the symlinking part of this."""
    try:
        src.symlink_to(dest)
    except FileExistsError:
        pass
    except OSError:
        # let's be a little more specific
        # except WindowsError: breaks linux
        raise PermissionsError(
            'Ensure that you are running this script as an admin'
            ' when running on Windows!'
        )


def main():
    """Set up the module."""
    logging.basicConfig(level=logging.INFO)
    user_arguments = _parse_arguments()
    args = user_arguments.parse_args()

    dest = args.destination

    if not dest.is_dir():
        sys.exit("Provided target not a directory. Exiting.")

    try:
        src = args.source
    except (IndexError, AttributeError) as e:
        raise UsageError(e)

    try:
        glob_search = args.glob_pattern
    except (AttributeError):
        glob_search = None

    try:
        recursive = args.recursive
    except AttributeError:
        recursive = False

    dlink(dest, src, is_recursive=recursive, glob_pattern=glob_search)


if __name__ == "__main__":
    main()
