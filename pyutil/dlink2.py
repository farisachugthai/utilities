#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Utilize argparse, pathlib and IPython to generate symlinks.

=========================
Directory Linker Rewrite
=========================

.. versionchanged:: Added argparse

This is a rewrite of a script I've had for years, so I decided to go above
and beyond.


See Also
---------
:func:`~IPython.utils.path.ensure_dir_exists()` : function
    Check for a dir and create it if it doesn't exist.

"""
import argparse
import logging
import sys
from pathlib import Path

from IPython.utils.path import ensure_dir_exists

from pyutil.__about__ import __version__


def _parse_arguments():
    parser = argparse.ArgumentParser(
        prog='Directory Linker 2.0',
        description="Iterate over a `dest` folder"
        " and create symlinks in directory "
        "`source`. If `source` is not provided use"
        " current working directory.")

    parser.add_argument("destination",
                        metavar="destination",
                        nargs='?',
                        type=Path,
                        help="Files to symlink to.")

    parser.add_argument(
        "-s",
        "--source_directory",
        metavar="SOURCE_DIRECTORY",
        nargs='?',
        help="Where to create the symlinks. Defaults to the cwd.")

    parser.add_argument(
        '-g',
        '--glob-pattern',
        metavar='GLOB_PATTERN',
        help='Filter files in the destination dir with a glob pattern.')

    parser.add_argument(
        '-r',
        '--recursive',
        action='store_true',
        default=False,
        help=
        "Whether to recursively symlink the child directories below the destination folder as well."
    )

    parser.add_argument('-V',
                        '--version',
                        action='version',
                        version='%(prog)s' + __version__)

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
    """This might be a good method in a dataclass if we wanted to try that."""
    return [i.stem + i.suffix for i in directory.iterdir()]


def main(destination_dir, source_dir, is_recursive=False, glob_pattern=None):
    """Symlink user provided files.

    The module doesn't immediately check for correct permissions or operating system.

    As a result, the onus is put on the user to ensure that the necessary requirements
    per OS are met. Namely on Windows 10, that if symlinks are allowed on the filesystem,
    they can only be created by an administrator.

    If we're refactoring for pathlib check out what we have to work with.::

        :func:`pathlib.glob`
        :func:`pathlib.iterdir`
        :func:`pathlib.rglob`

    Holy cow. I mean call that a wrap right? Let's spend some time dissecting
    the information we're given via argparse and log it if necessary, but after
    running a recursive glob on the destination then we should easily be able
    to handle the rest.

    That list comprehension is made and then iterated over. Should be a
    smarter way to do this.

    Ah poop. I think we need to combine the output from `generate_dest` and
    the list comprehension.

    Also gonna throw another function out that might help.

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
    base_destination_files = get_basenames(destination_dir)

    full_destination_files = [j for j in destination_dir.iterdir()]

    full_source_files = [
        Path(i).joinpath(source_dir) for i in base_destination_files
    ]
    for i in full_source_files:
        logging.debug('\ni is {0!s}'.format(i))
        logging.debug('\nfull_destination_files is {!s}'.format(full_destination_files))
        logging.debug('\nsource_dir is {}'.format(source_dir))
        logging.debug('\nbase_destination_files: {!r}'.format(base_destination_files))
        try:
            i.symlink_to(full_destination_files)
        except FileExistsError:
            pass
        except OSError:
            # let's be a little more specific
            # except WindowsError: breaks linux
            raise RuntimeError(
                'Ensure that you are running this script as an admin'
                ' when running on Windows!')

        # then call it recursively
        if i.is_dir():
            main(destination_dir=i,
                 source_dir=source_dir.joinpath(i),
                 recursive=recursive,
                 glob_pattern=glob_pattern)


if __name__ == "__main__":
    # uh you have to do something about this because it doesn't substitute
    # parameters correctly.
    # logging.basicConfig(level=logging.DEBUG,
    #                     format='{filename} : {asctime} : {levelno}\t{msg}')
    logging.basicConfig(level=logging.DEBUG)
    user_arguments = _parse_arguments()
    # Moved this up and out of _parse_arguments so you can introspect...and we can kill
    # that unnecessary logging call
    args = user_arguments.parse_args()

    dest = args.destination

    if not dest.is_dir():
        sys.exit("Provided target not a directory. Exiting.")

    try:
        src = args.source
    except (IndexError, AttributeError):
        src = Path().cwd()

    try:
        glob_pattern = args.glob_pattern
    except (AttributeError):
        glob_pattern = None

    try:
        recursive = args.recursive
    except AttributeError:
        recursive = False

    main(dest, src, recursive, glob_pattern)
