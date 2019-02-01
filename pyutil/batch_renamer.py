#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Renames a directory of files based on a template

Largely argparse and doctest practice.
From pydocs tutorials stdlib2 with some reformatting.
Still uses old style strings as a result.

.. code-block:: python

    >>> os.listdir("/path/to/dir")
    # ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
    >>>  batch_renamer.py /path/to/dir
    #  img_1074.jpg --> Ashley_0.jpg
    #  img_1076.jpg --> Ashley_1.jpg
    #  img_1077.jpg --> Ashley_2.jpg

.. todo::

    First things first ensure it works at all.

    This would be quite an easy module to create unittests for IN ADDITION
    to the fact that you could add some fixtures in and learn that.
"""
import argparse
import os.path
import shutil
from string import Template
import time


def fix_extension():
    """Rename files that have have the wrong filename extension.

    .. bugs::

        Fuck I didn't consider the case where there are 2 words separated by dots that we want to keep.
    """
    for i in os.listdir('.'):
        parts = i.split(sep='.')
        new = parts[0] + '.' + parts[1]
        shutil.move(i, new)


def fix_multipart_filename():
    """TODO. I mean a lot of todos. Gotta fix the function above a little.

    Gotta clean whatever the hell is going on below up.
    Then we gotta fix the module so that it properly handles names like
    :ref:`os.path.rst.txt`.
    """
    pass


def main(d):
    """Renames a dir of files.

    :param d: The directory to iterate over.
    """
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
