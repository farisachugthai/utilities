#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Programmatically work with subprocess' and Git.

Subprocess and Git
====================

This module intends to build a base class through subprocesses in order to
build up a trimmed-down, and more importantly *safer* Git object.

05/03/2019:

    Currently we need to move some module functions into our BaseCommand class.
    I don't want it to attempt implementing too much however. But it should have
    a method that checks output in the way that our module function does for the
    :command:`git rev-parse` expression that sets up the git root.

    Also we need some module wide logging. I mean all across :ref:`pyutil` it's nuts
    how poorly spread out and inconsistent it is.

"""
import codecs
import logging
# from pathlib import Path not yet
import shlex
import subprocess
import sys

from pyutil.shell import BaseCommand

LOGGER = logging.getLogger(name=__name__)


class Git(BaseCommand):
    """Create a base class for working with Git in Python.

    For the time being we only really need to run the :func:`g.BaseCommand.run`
    What other parameters do we need to pay attention to?
    State that would be useful to grab?
    Silencing the warnings about :attr:`version` is a start. So I guess
    learning how to properly initialize a class.

    """

    def __init__(self, root=None, **kwargs):
        """Initialize a few necessary parameters."""
        self.root = root
        super.__init__(self, **kwargs)

    @property
    def version(self):
        """Return the version of Git we have."""
        return self.run('git --version')

    @staticmethod
    def _static_quote_cmd(self, cmd):
        """Which one of these two is preferable?"""
        return shlex.quote(cmd)

    def _quote_cmd(self, cmd):
        """Maybe this should be in the parent class?"""
        cmd = shlex.quote(cmd)
        return self.run(cmd)


def touch(args):
    """Create a file and ``git add`` it.

    Parameters
    ----------
    args : str (path-like object)
        Path to a file that's needs to be staged and added to the Git index.


    """
    if len(args) > 2:
        files = args.split()
        fname = files[1:]
    elif len(args) < 2:
        sys.exit("No file provided. Exiting.")
    else:
        fname = args[1]
        subprocess.run(['git', 'add', fname])


def get_git_root():
    """Show the root of a repo."""
    cmd = "git rev-parse --show-toplevel".split()
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        return None


def get_git_branch():
    """Get the symbolic name for the current git branch."""
    cmd = "git rev-parse --abbrev-ref HEAD".split()
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        return None
    else:
        return output


def get_git_upstream_remote():
    """Get the remote name to use for upstream branches.

    Returns
    -------
    str : Remote git server
        Uses "upstream" if it exists, "origin" otherwise

    """
    cmd = "git remote get-url upstream".split()
    try:
        subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return "origin"
    return "upstream"


if __name__ == "__main__":
    args = sys.argv[:]

    LOGGER.setLevel(logging.WARNING)
