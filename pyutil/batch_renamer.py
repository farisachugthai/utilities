#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renames a directory of files based on a template.

.. module:: batch_renamer.py

Initially inspired f rom the Official Python documentation in the section
Tutorials: `tutorials stdlib2`_ with some reformatting.

Still uses old style strings as a result.

First we'll examine the contents of a directory and ensure it only contains
files with names we want to rename.


.. code-block:: python3

    >>> os.listdir("/path/to/dir")
    ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']


As we can see it does we'll then invoke the script like so.


.. code-block:: shell-session

    batch_renamer.py /path/to/dir
    img_1074.jpg --> Ashley_0.jpg
    img_1076.jpg --> Ashley_1.jpg
    img_1077.jpg --> Ashley_2.jpg

.. _`tutorials stdlib2`: https://docs.python.org/3/tutorial/stdlib2.html#templating

"""
import argparse
import os
import logging
import shutil
from string import Template
import time

from .__about__ import __version__


class BatchRename(Template):
    """Delimiter for string substitutions."""

    delimiter = '%'


def _parse_arguments():
    """Parse user arguments."""
    parser = argparse.ArgumentParser(description=__doc__)

    # should add in either globbing or fnmatch capabilities
    parser.add_argument(
        "directory",
        nargs=1,
        help="Directory containing only the files to be renamed.")

    parser.add_argument(
        'rename_format',
        nargs=1,
        help=
        r'Enter rename style (%d-date %n-seqnum %f-format I.E.  Ashley_%n%f)')

    parser.add_argument(
        '-V', '--version', action='version', version='%(prog)s' + __version__)

    args = parser.parse_args()

    return args


def fix_extension():
    """Rename files that have have the wrong filename extension."""
    for i in os.listdir('.'):
        parts = i.split(sep='.')
        new = parts[0] + '.' + parts[1]
        shutil.move(i, new)


def main(directory, fmt):
    """Rename a user provided directory of files.

    Parameters
    ----------
    directory : str
        The directory to iterate over.

    """
    # Enter rename style (%d-date %n-seqnum %f-format):
    t = BatchRename(fmt)
    date = time.strftime('%d%b%y')
    for i, filename in enumerate(os.listdir(directory)):
        base, ext = os.path.splitext(filename)
        newname = t.substitute(d=date, n=i, f=ext)
        logging.info('{0} --> {1}'.format(filename, newname))


def batch_mover(pattern):
    """Move files in the current working directory that match a pattern.

    Parameters
    ----------
    pattern : str
        Pattern to check filenames for.

    Returns
    -------
    bool

    """
    cwd = os.cwd()
    for i in os.scandir(cwd):
        if i.name.__contains__(pattern):
            yield True


if __name__ == '__main__':
    args = _parse_arguments()

    assert args.directory
    d = args.directory

    fmt = args.rename_format
    # Wait until we're sure we got the args we needed before setting the log
    # level.
    # Now we can configure that level based on user input and default to WARNING
    logging.basicConfig(level=logging.WARNING)

    logging.debug("The directory that was chosen was: " + str(d))

    if batch_mover(fmt):
        main(d, fmt)
