#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Renames a directory of files based on a template

Largely argparse and doctest practice.
From pydocs tutorials stdlib2. Reformatted.
Still uses old style strings as a result.

Examples::

    >>> os.listdir("/path/to/dir")
    # ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
    >>> python3 batch_renamer.py /path/to/dir
    #  img_1074.jpg --> Ashley_0.jpg
    #  img_1076.jpg --> Ashley_1.jpg
    #  img_1077.jpg --> Ashley_2.jpg

Wait how much do module docstrings get indented?
Both the text and the quotes.
"""

__author__ = 'Faris Chugthai'
__copyright__ = 'copyright (c) 2018 Faris Chugthai'
__email__ = 'farischugthai@gmail.com'
__license__ = 'MIT'
__url__ = 'https://github.com/farisachugthai'

import argparse
import os.path
from string import Template
import time


class BatchRename(Template):
    delimiter = '%'


def main(d):
    """Renames a dir of files."""
    # fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
# Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

    t = BatchRename(fmt)
    date = time.strftime('%d%b%y')
    for i, filename in enumerate(os.listdir(d))0:
        base, ext = os.path.splitext(filename)
        newname = t.substitute(d=date, n=i, f=ext)
        print('{0} --> {1}'.format(filename, newname))


if __name__ = '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Directory containing only the files to be renamed.")
    args = parser.parse_args()
    print(args.directory)
    d = args.directory
    main(d)

    # first things first ensure it works at all
    #  import doctest
    #  doctest.docmod()
    # then build up the module. Add arg to handle different string template.
