#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Iterate over the list of conda environments that are present.

Assumes:
    Working conda installation.

Examples:

    $ python3 conda-export.py

Returns:

    Separate text files. 2 for each environment.
    - One with general metadata
    - One with a list of packages.

TODO::
    Possibly refactor into more functions. Would this warrant a class?

Work in progress.
"""
import codecs
import shutil
from subprocess import run, PIPE
import sys


def munging():
    """Iterate through conda envs and return text files to replicate from"""
    ENVLIST = run(["conda", "env", "list"], stdout=PIPE, stderr=PIPE)

    if ENVLIST.returncode is not 0:
        sys.exit(ENVLIST.returnode)
    else:
        # Unfortunately the value that conda returns is in bytes. Ugh.
        decoded = codecs.decode(ENVLIST.stdout)

        # Now let's take this long unwieldy string we have and clean it up
        decoded = decoded.splitlines()
        # Initially it prints out a few unnecessary lines. Let's chop them off
        decoded = decoded[2:-1]

        return decoded


def truncate(envs):
    """Take the decoded environments and reduce them down to the parts we need."""
    # I want this list comprehension to work so badly I cant tell you
    short_envs = [env for env.split()[0] in envs]
    return short_envs


if __name__ == "__main__":
    # First things first
    if not shutil.which('conda'):
        sys.exit("It looks like conda isn't installed. Exiting...")
    full_name_envs = munging()
    envs = truncate(full_name_envs)
    print(envs)
