#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

:mod:`make` --- Expedite documentation builds.
================================================

.. module:: make
    :synopsis: Expedite documentation builds.


:File: make.py
:Author: Faris Chugthai
:Github: `https://github.com/farisachugthai`_
:Date: |date|

"""
import os
import shlex
import shutil
import subprocess


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
    run(f'make -j{jobs}')
    # TODO: Copy the sources over to the right spot. And that static dir I guess.
    # shutil.copytree(src, dst)
