#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Deletes extraneous files.

Without frequent monitoring, directories like /tmp and /var/log can frequently
grow to sizes that are difficult to manage because of clutter and files.

However, there has to be a middle ground between deleting thousands of files
one by one and :command:`rm -rf /tmp/`.

This module attempts that.

Initially tested on the android app Termux, this specifically deletes
directories with only month old sockets.

    - :envvar:`$PREFIX`/tmp/nvim
    - :envvar:`$PREFIX`/tmp/ssh

.. note:: On Ubuntu the big one is /var/log/journal so we might need to
          remind the user for credentials. :func:`getpass.getpass`?

In addition, it felt like a good way to get more familiar with the new
:mod:`pathlib` module.

Well it will be after rewriting it all.

"""
from glob import glob
import logging
import os
# from pathlib import Path
# import shlex
import shutil
import sys

logger = logging.getLogger(__name__)

def dir_cleaner(i):
    """Yield all directories before november."""
    if i.is_dir():
        # The 8th element is st_mtime. That timestamp is before nov 1st
        if i.stat()[8] < 1541097635:
            try:
                os.rmdir(i)
            except OSError:
                pass  # more than likely dir not empty.


def clean(ftype='*.pyc', recursive=False):
    """Remove all pyc files. Add input for filetype later.

    Parameters
    ----------
    ftype : filetype
        File to iterately remove.
    recursive : Bool, Optional
        Whether to search the directory recursively or not.

    """
    j = [os.unlink(i) for i in glob(ftype, recursive=recursive)]
    return j


def rmtree(path, ignore_errors=False, onerror=None):
    """Returns :func:`shutil.rmtree`."""
    return shutil.rmtree(path, ignore_errors, onerror)


def main():
    """Directory cleaner."""
    # There are better ways to determine if Android. check :envvar:`ANDROIDROOT`?
    try:
        tmp = os.environ.get('PREFIX') + '/tmp/'
    except (OSError, TypeError):
        tmp = '/tmp/'
    tmpd = os.scandir(tmp)
    # Also let's start handling command line arguments please?
    # args = shlex.split(sys.argv[:])

    for i in tmpd:
        dir_cleaner(i)


if __name__ == "__main__":
    sys.exit(main())
