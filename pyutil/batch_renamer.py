#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Renames a directory of files based on a template.

.. module:: batch_renamer.py

Largely argparse and doctest practice.
From pydocs tutorials stdlib2 with some reformatting.
Still uses old style strings as a result.

.. code-block:: python

    >>> os.listdir("/path/to/dir")
    ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
    >>>  batch_renamer.py /path/to/dir
    img_1074.jpg --> Ashley_0.jpg
    img_1076.jpg --> Ashley_1.jpg
    img_1077.jpg --> Ashley_2.jpg

.. todo::

    First things first ensure it works at all.

    This would be quite an easy module to create unittests for IN ADDITION
    to the fact that you could add some fixtures in and learn that.

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

    .. todo::

        Fuck I didn't consider the case where there are 2 words
        separated by dots that we want to keep.
    """
    for i in os.listdir('.'):
        parts = i.split(sep='.')
        new = parts[0] + '.' + parts[1]
        shutil.move(i, new)


def main(d):
    """Rename a dir of files.

    .. todo::

        Uhhhh??

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


def batch_mover(pattern):
    """Move files in the current working directory that match a pattern.

    .. todo::

        Fix docstring to numpy style... in the meanwhile ensure all
        3 of these render correctly as is.

    :param pattern: Pattern to check filenames for.
    :returns: True or False
    :rtype: Bool
    """
    cwd = os.cwd()
    for i in os.scandir(cwd):
        if i.name.__contains__(pattern):
            yield True


if __name__ == '__main__':

    logging.basicConfig()

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d",
        "--directory",
        help="Directory containing only the files to be renamed.")

    args = parser.parse_args()

    logging.debug(args.directory)

    d = args.directory
    main(d)
def fix_botched_renamer():
    """Realistically nobody should ever be excited they wrote this but I just got a hotfix to work on the first try.
    Parameters
    ----------
    I guess the files to fix?
    
    Returns
    --------
    Yo shit fixed.
    
    So I ran the following::
    
        >>> from glob import glob
        >>> import shutil
        >>> r = glob('*.rst')
        >>> for i in r:
            >>> shutil.move(i, 'source' + i)
            
    Thinking I was gonna move some restructured text files into the source directory. Nope. No path sep.
    The below is how I fixed it, and I got it on the first try!!! I'm actually pretty pumped. No doc lookups or anything.
    This is pure memory.
    """
    from glob import glob
    r = glob('*.rst')
    for i in r:
        shutil.move(i, i.split('source')[1])
    
