#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Deletes extraneous files.

Run in :envvar:`$PREFIX`/tmp

However, there has to be a middle ground between deleting thousands of files
one by one and ``rm -rf /tmp/*``.

This module attempts that.

Initially tested on the android app Termux, this specifically deletes
directories with only month old sockets.
    - :envvar:`$PREFIX`/tmp/nvim
    - :envvar:`$PREFIX`/tmp/ssh

- Failing that, specifically delete directories with only month old sockets
    - :envvar:`$PREFIX`/tmp/nvim*
    - :envvar:`$PREFIX`/tmp/ssh*

"""
from glob import glob
import os
import shutil


def dir_cleaner(i):
    """Yield all directories before november."""
    if i.is_dir():
        # The 8th element is st_mtime. That timestamp is before nov 1st
        if i.stat()[8] < 1541097635:
            try:
                os.rmdir(i)
            except OSError:
                pass  # more than likely dir not empty.


def extract_dir():
    """Could be used in dir_cleaner. Yeah let's do that.

    .. todo::

        *sigh* Alright so we need to add a check that the zip starts with a dir
        If the top level isn't a dir holding everything then you'll have loose
        files everywhere.

    """
    for i in glob('*.zip'):
        shutil.unpack_archive(i)
        os.unlink(i)


def clean(ftype='*.pyc', recursive=False):
    """Remove all pyc files. Add input for filetype later.

    Parameters
    ----------
    recursive : Bool
    ftype : filetype
        File to iterately remove.

    """
    j = [os.unlink(i) for i in glob(ftype, recursive=recursive)]
    return j


if __name__ == "__main__":
    try:
        tmp = os.environ.get('PREFIX') + '/tmp/'
    except (OSError, TypeError):
        tmp = '/tmp/'
    tmpd = os.scandir(tmp)
    for i in tmpd:
        dir_cleaner(i)
