#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Automate profiling nvim."""
import datetime
import os

from pyutil.env_checks import *  # noqa F403


def check_profiling_dir():
    """Ensure a directory has been created for the results.

    Need to change now that we take xdg into account.
    """
    if os.path.isdir(os.path.join(dirname, 'profiling')) is False:
        os.mkdir(os.path.join(dirname, 'profiling'))


def main():
    """Profile nvim."""
    now = datetime.date.isoformat(datetime.datetime.now())

    # TODO:
    # check_profiling_dir():

    # Why aren't I setting more variables along the way? We have too many
    # hard coded strings
    # results = os.path.join(dirname, 'profiling', now)

    # TODO: use subprocess to run
    # nvim --startuptime results somepyfile.py results
    # got it working in other session


if __name__ == "__main__":
    xdg = check_xdg_env()

    if xdg:
        nvimroot = os.environ.get("XDG_CONFIG_HOME")
    else:
        # hmm what do?
        # nvimroot = get_home() + os.path.join("config", "nvim", "")
        pass

    pdir = check_profiling_dir()

    main()
