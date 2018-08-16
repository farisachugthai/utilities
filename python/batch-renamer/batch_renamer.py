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

TODO: Wait how much do module docstrings get indented?
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
import uuid

# Wth is the order up top supposed to be? I might Ijust leave it but there are docs like
# pep 8 that get SO specific everyones code starts looking the same.


class BatchRename(Template):
    delimiter = '%'


def tmpfiles():
    """Here so that if you don't want to keep botching family photos, you can
    test this module on emporary files.

    Utilize the tempfile module in order to simulate IO processes, and wrap i in a
    context manager to ensure that all connections are closed when the script completes.
    """

# we could take a predetermined value for the range. shrugs.
def batch_helper():
    """Created to produce sparse and light files to accommodate testing the script."""
for tmp0 in range(35):
    tmp_file = open('capitalsquiz%s.txt' %(quizNum + 1), 'w') as f:
        f.write('Arbitrary Header:\nDate'+datetime.datetime.now()


def main(d):
    """Renames a dir of files."""
    # fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
# Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

    t = BatchRename(fmt)
    date = time.strftime('%d%b%y')
    for i, filename in enumerate(os.listdir(d)):
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
