#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Deletes extraneous files.

Without frequent monitoring, directories like /tmp and /var/log can frequently
grow to sizes that are difficult to manage because of clutter and files.

However, there has to be a middle ground between deleting thousands of files
one by one and :command:`rm -rf /tmp/*`.

This module attempts that.

Initially tested on the android app Termux, this specifically deletes
directories with only month old sockets.
    - :envvar:`$PREFIX`/tmp/nvim
    - :envvar:`$PREFIX`/tmp/ssh

.. note:: On Ubuntu the big one is /var/log/journal so we might need to
          remind the user for credentials. :func:`getpass.getpass`?

In addition, it felt like a good way to get more familiar with the new
:mod:`pathlib` module.

"""
from glob import glob
import os


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
