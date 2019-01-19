#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Automate profiling nvim.

Examples::
    Case

Tests::
    something

Errors/Bugs::
    abc

So yeah.
"""
import datetime
import os
import shutil
import subprocess


def get_script_dir():
    """Determine the directory this script is in."""
    return os.path.dirname(os.path.realpath(__file__))


def check_profiling_dir():
    """Ensure a directory has been created for the results.
    Need to change now that we take xdg into account.
    """
    if os.path.isdir(os.path.join(dirname, 'profiling')) is False:
        os.mkdir(os.path.join(dirname, 'profiling')


def main():
    """Profile nvim."""
    now = datetime.date.isoformat(datetime.datetime.now())

    get_script_dir()

    # check_profiling_dir():

    # results = os.path.join(dirname, 'profiling', now)

    # TODO: use subprocess to run
    # nvim --startuptime results somepyfile.py results
    # got it working in other session


if __name__ == "__main__":
    main()
