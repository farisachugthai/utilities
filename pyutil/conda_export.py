#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Iterate over the list of conda environments that are present.

Assumes
---------
Working conda installation.

Example
--------

.. code-block:: shell

    python3 conda-export.py

Returns
-------
Separate text files. 2 for each environment.
- One with general metadata
- One with a list of packages.


.. todo::

    - Possibly refactor into more functions.
        - Would this warrant a class?
    - Shell highlighting is really light. Hard to read.
    - Add logging. Return more useful info besides just printing.

Work in progress.

"""
import codecs
import shutil
from subprocess import run, PIPE
import sys


def munging():
    """Iterate through conda envs and return text files to replicate from.abs

    Parameters
    -----------
    None


    Returns
    --------
    envs: list
        list of conda environments


    """
    ENVLIST = run(["conda", "env", "list"], stdout=PIPE, stderr=PIPE)

    if ENVLIST.returncode != 0:
        sys.exit(ENVLIST.returnode)
    else:
        # Unfortunately the value that conda returns is in bytes. Ugh.
        decoded = codecs.decode(ENVLIST.stdout)

        # Now let's take this long unwieldy string we have and clean it up
        decoded = decoded.splitlines()
        # Initially it prints out a few unnecessary lines. Let's chop them off
        envs = decoded[2:-1]

        return envs


def truncate(envs):
    """Take the decoded environments and reduce them down to the parts we need."""
    # I want this list comprehension to work so badly I cant tell you
    short_envs = []

    for env in envs:
        short_envs.append(env.split()[0])

    return short_envs


if __name__ == "__main__":
    # First things first
    if not shutil.which('conda'):
        sys.exit("It looks like conda isn't installed. Exiting...")

    full_name_envs = munging()

    envs = truncate(full_name_envs)

    print(envs)
