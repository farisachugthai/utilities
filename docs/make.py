#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Expedite documentation builds.

:mod:`make`
================================================

.. module:: make
    :synopsis: Expedite documentation builds.


:File: make.py
:Author: Faris Chugthai
:Github: `https://github.com/farisachugthai`_
:Date: |today|

"""
import argparse
import os
import shlex
# import shutil
import subprocess
import sys


def _parse_args():
    """Read in the user's input with :class:`argparse.ArgumentParser()`."""
    sys_args = sys.argv[:]

    if len(sys_args) == 1:
        sys.exit('Please provide a builder for the command.')

    parser = argparse.ArgumentParser(prog=sys_args[0],
                        description='Make the documentation for the Pyutil project.')

    parser.add_argument('sourcefile', metavar = 'SOURCEFILE',
                        help = 'file containing Python sourcecode')

    parser.add_argument('-b', '--browser', action = 'store_true',
                        help = 'launch a browser to show results')

    args = parser.parse_args()
    return args


def run(cmd):
    """Execute the required command in a subshell.

    First the command is splited used typical shell grammer.
    A new process is created, and from the resulting subprocess object,
    the :func:`subprocess.Popen().wait()`. This function returns the return
    code of split ``cmd``, so any non-zero value will lead to a ``SystemExit``
    with a passed value of the returncode.

    Parameters
    ----------
    cmd : str
        The command to be called

    Returns
    -------
    process.returncode : int
        The returncode from the process.


    """
    cmd = shlex.split(cmd)
    process = subprocess.Popen(cmd)

    if process.wait():
        raise SystemExit(process.returncode)
    else:
        return process.returncode


if __name__ == "__main__":
    jobs = f'{os.cpu_count()}'
    # TODO: Check that the f string syntax is correct. Possibly now need to import sys_checks and ensure that we
    # have python > 3.6

    args = _parse_args()

    run(f'make -j{jobs}')
    # TODO: Copy the sources over to the right spot. And that static dir I guess.
    # shutil.copytree(src, dst)
