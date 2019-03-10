#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Iterate over all of the python files in a directory recursively.

.. module:: itersrc.py
    :synopsis: Iterate over all of the python files in a directory recursively.

:File: itersrc.py
:Author: Faris Chugthai

`Github <https://github.com/farisachugthai>`_

.. versionchanged:: 0.0.1
    Just added a check for python files. This could be useful as a base
    for a test runner.

"""
import os
import sys


def iter_source_code(paths):
    """Iterate over all Python source files in C{paths}.

    Taken with almost no modifications from pyflakes.
    This would be a great function to call with :func:`os.listdir()`
    output.

    Parameters
    ----------
    paths: list
        A list of paths.  Directories will be recursed into and any .py
        files found will be yielded.


    Yields
    ------
    ``full_path`` : str
        Absolute path to a python file.


    """
    for path in paths:
        if os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    if filename.ends_with('.py'):
                        full_path = os.path.join(dirpath, filename)
                        yield full_path
        else:
            yield path


if __name__ == "__main__":
    paths = sys.argv[:]
    iter_source_code(paths)
