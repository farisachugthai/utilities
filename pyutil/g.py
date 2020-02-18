#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
=====================================================
g --- Programmatically work with subprocess' and Git.
=====================================================

.. highlight:: ipython

.. module:: g
    :synopsis: Make working with Git safer and easier.

This module intends to build a base class through subprocesses in order to
build up a trimmed-down, and more importantly *safer* Git object.

Subprocess and Git
====================

Currently we need to move some module functions into our BaseCommand class.
I don't want it to attempt implementing too much however. But it should have
a method that checks output in the way that our module function does for the
:command:`git rev-parse` expression that sets up the git root.

You know what would be nice? Run the following commands in one.

.. code-block:: console

    git branch -d foo
    git branch -rd origin/foo
    git push origin :foo

There's no reason that that's 3 commands with differing syntax.

All you need to do is check if the branch exists both locally and
remotely and kill everything.

"""
import logging
from pathlib import Path
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
        if root is None:
            self.root = self._get_git_root()
        else:
            self.root = root
        super().__init__(self, **kwargs)

    def __repr__(self):
        return "{!r}\t{!r}".format(self.__class__.__name__, self.root)

    @property
    def version(self):
        """Return the version of Git we have."""
        return self.run("git --version")

    @staticmethod
    def _quote(self, cmd):
        """Which one of these two is preferable?"""
        return shlex.quote(cmd)

    def _quote_cmd(self, cmd):
        """Maybe this should be in the parent class?"""
        cmd = shlex.split(shlex.quote(cmd))
        return self.run(cmd)

    def _get_git_root(self):
        """Show the root of a repo."""
        cmd = "git rev-parse --show-toplevel".split()
        try:
            return subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError:
            return None

    def _check_output(self, cmd, **kwargs):
        """Checks output from a subprocess call."""
        try:
            output = subprocess.check_output(
                [self._quote(cmd), kwargs],
                universal_newlines=True,
                stderr=subprocess.PIPE,
            )
        except subprocess.CalledProcessError as e:
            return e
        return output

    def get_git_upstream_remote(self):
        """Get the remote name to use for upstream branches.

        Returns
        -------
        str : Remote git server
            Uses "upstream" if it exists, "origin" otherwise

        """
        cmd = "git remote get-url upstream"
        return self._check_output(cmd)


class Other:
    """Toy code always refers to other I.E. self != other. Let's write other!

    Haha just kidding. I'm testing out Git but one that doesn't subclass anything
    because the parent class is having problems
    """

    def __init__(self, root=None, version=None):
        """Initialize Git all by its lonesome."""
        if root is not None:
            self.root = root
        else:
            self.root = self._get_git_root()
        if version is not None:
            self.version = version
        else:
            self.version = self._get_version()

        self.Path = Path

        def __call__(self):
            """Got an error that the object isn't callable TODO"""
            if self._validate_dir(self.root):
                return repr(Path(self.root))

        def __repr__(self):
            return "{!r}".format(self.root)

        def _validate_dir(self, dir=None):
            real_dir = self.Path(dir).is_dir()
            return real_root

    def _get_version(self):
        try:
            output = subprocess.check_output(["git", "--version"], text=True)
        except CalledProcessError as e:
            return e
        else:
            return output

    def _get_git_root(self):
        """Show the root of a repo."""
        cmd = "git rev-parse --show-toplevel".split()
        try:
            return subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError:
            return None


def touch(args):
    """Create a file and ``git add`` it.

    Parameters
    ----------
    args : str (path-like object)
        Path to a file that's needs to be staged and added to the Git index.

    """
    if len(args) > 1:
        files = args.split()
        fname = files[0:]
        for element in fname:
            subprocess.run(["git", "add", fname])
    elif len(args) < 1:
        sys.exit("No file provided. Exiting.")
    else:
        fname = args[1]
        subprocess.run(["git", "add", fname])


def get_git_branch():
    """Get the symbolic name for the current git branch."""
    cmd = "git rev-parse --abbrev-ref HEAD".split()
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        return None
    else:
        return output


if __name__ == "__main__":
    args = sys.argv[1:]

    LOGGER.setLevel(logging.WARNING)
