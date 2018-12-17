#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Beginning of script. Not finished.

Run in $PREFIX/tmp.

Can modify to accept user input and fall back to that dir.

Implement once all the logic has panned out.

.. todo::

    - Write a second function that implemenents rm -r if `du dir==0`
    - Failing that, specifically delete directories with only month old sockets
        - $PREFIX/tmp/nvim-*
        - $PREFIX/tmp/ssh-*

Dec 01, 2018:

    I was writing this like on termux like 4 days ago. Cleaned up
    ~/python/tutorials/fnmatch_.py and realized it was the exact same thing.
"""
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


if __name__ == "__main__":
    try:
        tmp = os.environ.get('PREFIX') + '/tmp/'
    except (OSError, TypeError):
        tmp = '/tmp/'
    tmpd = os.scandir(tmp)
    for i in tmpd:
        dir_cleaner(i)
