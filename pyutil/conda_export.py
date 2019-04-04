#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Iterate over the list of conda environments that are present."""
import codecs
import shutil
from subprocess import run, PIPE
import sys


def munging():
    """Iterate through conda envs and return text files to replicate from.

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
    """Take output from pyutil.conda_export.munging, reduce and print to console.

    Parameters
    ----------
    envs : str
        Conda environments


    Returns
    -------
    short_envs : list of strs
        Shorter name of all envs. Printed to console.


    """
    short_envs = []

    for env in envs:
        short_envs.append(env.split()[0])

    return short_envs


def main():
    """TODO: Docstring for main.
    Returns
    -------
    TODO

    """
    # First things first
    if not shutil.which('conda'):
        sys.exit("It looks like conda isn't installed. Exiting...")

    full_name_envs = munging()

    truncated_envs = []
    for i in full_name_envs:
        truncated_envs.append(truncate(i))

    print(str(truncated_envs))


if __name__ == "__main__":
    sys.exit(main())
