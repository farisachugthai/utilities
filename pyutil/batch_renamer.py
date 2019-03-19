#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renames a directory of files based on a template.

.. module:: batch_renamer.py

Largely argparse and doctest practice.
From the Official Python documentation in the section Tutorials:
`tutorials stdlib2`_ with some reformatting.

Still uses old style strings as a result.

.. code-block:: python3

    >>> os.listdir("/path/to/dir")
    ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

.. code-block:: shell-session

    batch_renamer.py /path/to/dir
    img_1074.jpg --> Ashley_0.jpg
    img_1076.jpg --> Ashley_1.jpg
    img_1077.jpg --> Ashley_2.jpg

This would be quite an easy module to create unittests for IN ADDITION to the
fact that you could add some fixtures in and learn that.

.. _`tutorials stdlib2`: https://docs.python.org/3/tutorial/stdlib2.html#templating

"""
import argparse
import os
import logging
import shutil
from string import Template
import time

import pyutil


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
        '-V',
        '--version',
        action='version',
        version='%(prog)s' + pyutil.__about__['version'])

    args = parser.parse_args()

    return args


def fix_extension():
    """Rename files that have have the wrong filename extension.

    .. todo:: Fuck I didn't consider the case where there are 2 words separated by dots that we want to keep.

    """
    for i in os.listdir('.'):
        parts = i.split(sep='.')
        new = parts[0] + '.' + parts[1]
        shutil.move(i, new)


def main(directory):
    """Rename a user provided directory of files.

    Parameters
    ----------
    directory : str
        The directory to iterate over.

    """
    fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
    # Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f
    t = BatchRename(fmt)
    date = time.strftime('%d%b%y')
    for i, filename in enumerate(os.listdir(directory)):
        base, ext = os.path.splitext(filename)
        newname = t.substitute(d=date, n=i, f=ext)
        print('{0} --> {1}'.format(filename, newname))


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

    # Wait until we're sure we got the args we needed before setting the log
    # level.
    # Now we can configure that level based on user input and default to WARNING
    logging.basicConfig(level=logging.WARNING)

    logging.debug("The directory that was chosen was: " + str(d))

    main(d)
