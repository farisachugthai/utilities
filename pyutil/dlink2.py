#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Utilize argparse, pathlib and IPython to generate symlinks.

=========================
Directory Linker Rewrite
=========================

.. versionchanged:: Added argparse

This is a rewrite of a script I've had for years, so I decided to go above and beyond.



See Also
---------

IPython's :func:`IPython.utils.path.ensure_dir_exists()`

"""
import argparse
import logging
import sys
from pathlib import Path

from IPython.utils.path import ensure_dir_exists
from pyutil.__about__ import __version__

logging.getLogger(name=__name__)


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

    parser.add_argument('-V',
                        '--version',
                        action='version',
                        version='%(prog)s' + __version__)

    logging.debug("Dir(parser): {} ".format(dir(parser)))

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        return parser.parse_args()


def generate_dest(dest, glob_pattern=None):
    """Return a generator for all the files in the destination directory."""
    if not ensure_dir_exists(dest):
        logging.error('%s' % dest, exc_info=1)
    if glob_pattern:
        yield Path(dest).glob(glob_pattern)
    else:
        yield Path(dest).glob('*')


def main(destination_dir, source_dir):
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


    Parameters
    ----------
    destination_dir : str
         Directory where symlinks point to.
    source_dir : str, optional
        Directory where symlinks are created.

    """
    # for i in glob.glob(destination_dir + "/**", recursive=True):
    for i in Path(destination_dir).glob('*'):
        if i.is_file():
            source_file = i.joinpath(source_dir)
            # source_file = os.path.join(source_dir, i)
            try:
                # os.symlink(i, source_file)
                i.symlink_to(sourcefile)
            except FileExistsError:
                pass
            # except OSError:
            # let's be a little more specific
            except WindowsError:
                print("Ensure that you are running this script as an admin"
                      " if it's being run on Windows!")
                raise RuntimeError


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    args = _parse_arguments()

    dest = args.destination

    try:
        src = args.source
    except (IndexError, AttributeError):
        src = Path().cwd()
    # except Exception: logger.error('what happened'); sys.exit()

    main(dest, src)
    # TODO: add recursive as a parameter
