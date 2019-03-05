#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renames a directory of files based on a template.

.. module:: batch_renamer.py

Largely argparse and doctest practice.
From pydocs tutorials stdlib2 with some reformatting.
Still uses old style strings as a result.

.. code-block:: python3

    >>> os.listdir("/path/to/dir")
    ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
    >>>  batch_renamer.py /path/to/dir
    img_1074.jpg --> Ashley_0.jpg
    img_1076.jpg --> Ashley_1.jpg
    img_1077.jpg --> Ashley_2.jpg


.. todo:: First things first ensure it works at all.


This would be quite an easy module to create unittests for IN ADDITION to the
fact that you could add some fixtures in and learn that.

"""
import argparse
import os
import logging
import shutil
from string import Template
import time


class BatchRename(Template):
    """Delimiter for string substitutions."""

    delimiter = '%'


def fix_extension():
    """Rename files that have have the wrong filename extension.

    .. todo:: Fuck I didn't consider the case where there are 2 words separated by dots that we want to keep.
    """
    for i in os.listdir('.'):
        parts = i.split(sep='.')
        new = parts[0] + '.' + parts[1]
        shutil.move(i, new)


def main(d):
    """Rename a dir of files.

    Parameters
    ----------
    d : path-like object
        The directory to iterate over.


    Returns
    -------
    None

    """
    fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
    # Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f
    t = BatchRename(fmt)
    date = time.strftime('%d%b%y')
    for i, filename in enumerate(os.listdir(d)):
        base, ext = os.path.splitext(filename)
        newname = t.substitute(d=date, n=i, f=ext)
        print('{0} --> {1}'.format(filename, newname))


def batch_mover(pattern):
    """Move files in the current working directory that match a pattern.

    Parameters
    ----------
    pattern: str
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

    logging.basicConfig()

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "directory",
        "-d",
        "--directory",
        help="Directory containing only the files to be renamed.")

    args = parser.parse_args()

    d = args.directory

    logging.debug("The directory that was chosen was: " + str(d))

    main(d)
