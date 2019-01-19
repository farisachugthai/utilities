#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Renames a directory of files based on a template

Largely argparse and doctest practice.
From pydocs tutorials stdlib2. Reformatted.
Still uses old style strings as a result.


First things first ensure it works at all. Then add some doctests.

.. code::

    >>> import doctest
    >>> doctest.docmod()

Then build up the module. Add arg to handle different string template.

"""
import argparse
import os.path
import shutil
from string import Template
import time


class BatchRename(Template):
    delimiter = '%'


def fix_extension():
    """Basically a batch renamer.

    .. usage::

        # This isn't very helpful but whatever. cd into intended dir
        fix_extension()

    .. bugs::

        Fuck I didn't consider the case where there are 2 words separated by dots that we want to keep.
    """
    for i in os.listdir('.'):
        parts = i.split(sep='.')
        new = parts[0] + '.' + parts[1]
        shutil.move(i, new)


def main(d):
    """Renames a dir of files."""
    fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
    # Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f
    t = BatchRename(fmt)
    date = time.strftime('%d%b%y')
    for i, filename in enumerate(os.listdir(d)):
        base, ext = os.path.splitext(filename)
        newname = t.substitute(d=date, n=i, f=ext)
        print('{0} --> {1}'.format(filename, newname))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directory",
        help="Directory containing only the files to be renamed.")
    args = parser.parse_args()
    print(args.directory)
    d = args.directory
    main(d)
