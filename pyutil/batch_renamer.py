#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renames a directory of files based on a template.

.. module:: batch_renamer.py

First we'll examine the contents of a directory and ensure it only contains
files with names we want to rename.


.. code-block:: python3

    >>> os.listdir("/path/to/dir")
    ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']


As we can see it does we'll then invoke the script like so.

.. code-block:: shell-session

    python3 batch_renamer.py /path/to/dir
    img_1074.jpg --> Ashley_0.jpg
    img_1076.jpg --> Ashley_1.jpg
    img_1077.jpg --> Ashley_2.jpg

"""
import argparse
import os
import logging
from pathlib import Path
# import shutil
from string import Template

from .__about__ import __version__

LOG_LEVEL = "logging.WARNING"


class BatchRename(Template):
    """Delimiter for string substitutions."""

    delimiter = '%'


def _parse_arguments():
    """Parse user arguments."""
    parser = argparse.ArgumentParser(description=__doc__)

    # should add in either globbing or fnmatch capabilities
    parser.add_argument(
        "-d",
        "--directory",
        nargs=1,
        default=Path.cwd(),
        help="Directory containing only the files to be renamed.")

    parser.add_argument('old_format',
                        nargs=1,
                        metavar='old_format',
                        help=r'Enter old format to replace.')

    parser.add_argument(
        'rename_format',
        nargs=1,
        metavar='rename_format',
        help=
        r'Enter rename style (%d-date %n-seqnum %f-format I.E.  Ashley_%n%f)')

    parser.add_argument(
        '-ll',
        '--log_level',
        dest='log_level',
        metavar='log level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Set the logging level')

    parser.add_argument('-V',
                        '--version',
                        action='version',
                        version='%(prog)s' + __version__)

    args = parser.parse_args()

    return args


def batch_mover(pattern, new_pattern, directory=None):
    """Move files in the current working directory that match a pattern.

    Parameters
    ----------
    pattern : str
        Pattern to check filenames for. Functionally would be the old extension.
    new_pattern : str
        What to replace the old pattern with.
    directory : str, optional
        Directory where files that need to be renamed can be found.

    Returns
    -------
    Bool

    """
    if directory is None:
        directory = Path().cwd()

    for i in os.scandir(directory):
        if file_check(pattern, i.name):
            pass
            # shutil.move(i.name, yeah we gotta change a lot here


def file_check(pattern, file_to_check):
    """Check that the file exists and matched the desired pattern."""
    if file_to_check.name.__contains__(pattern):
        yield True


def main():
    """Execute module."""
    args = _parse_arguments()
    d = args.directory
    fmt = args.rename_format
    old = args.old_pattern

    try:
        log_level = args.log_level
    except Exception:  # IndexError?
        logging.basicConfig(level=LOG_LEVEL)
    else:
        logging.basicConfig(level=log_level)

    logging.debug("The directory that was chosen was: " + str(d))
    batch_mover(pattern=old, new_pattern=fmt, directory=d)


if __name__ == '__main__':
    main()
