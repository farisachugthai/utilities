#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Programmatically work with subprocesses and Git.

04/16/19
There is a silly amount of repitition in this file.

Implementing a base class to work with a safer subprocess with the intention
of building up a safer minimal Git object.
"""
import codecs
import logging
# from pathlib import Path not yet
import shlex
import subprocess
import sys
import sysconfig
"""
don't need this but could utilize
try:
    from git import Git
except ImportError:
    sys.exit()
"""

SRCDIR = sysconfig.get_config_var('srcdir')

logger = logging.getLogger(name=__name__)


class BaseCommand(object):
    """Create a base command class."""

    def run(self, cmd=None):
        """Run a safer subprocess.

        Parameters
        ----------
        cmd : str, optional
            cmd to run in subprocess

        Returns
        -------
        output : bytes
            Output from subprocess. Can return `NoneType` if no `cmd`.
        """
        if cmd:
            cmd = shlex.split(cmd)
        else:
            return None
        output = subprocess.run([cmd], capture_output=True)

        validated_output = _validate(output)
        return validated_output

    def _validate(subprocess_output):
        """Take output from :func:`subprocess.run()`.

        First the func will check :attr:`returncode`.

        Then the bytes that were returned from the *presumably* Unix OS
        will be decoded into a human readable format.
        """
        if subprocess_output.returncode != 0:
            logging.error(subprocess_output.returncode)
        else:
            if isinstance(subprocess_output.stdout, bytes):
                decoded_output = codecs.decode(subprocess_output.stdout)
                # also probably gonna wanna pprint that when you receive it
                return decoded_output
            else:
                logging.warning("Subprocess didn't return bytes. Maybe str?")
                logging.warning(type(subprocess_output.stdout))
                return subprocess_output


class Git(BaseCommand):
    """Create a base class for working with Git in Python.

    For the time being we only really need to run the :func:`g.BaseCommand.run`
    What other parameters do we need to pay attention to?
    State that would be useful to grab?
    Silencing the warnings about :attr:`version` is a start. So I guess
    learning how to properly initialize a class.

    """

    def __init__(self, version=None, root=None, **kwargs):
        """Initialize a few necessary parameters."""
        self.root = root
        self.version = version
        super.__init__(self, **kwargs)

    def _quote_cmd(self, cmd):
        """Is this a @staticmethod?"""
        return shlex.quote(cmd)



def git_touch(args):
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
        return subprocess.check_output(
            cmd, stderr=subprocess.STDOUT, cwd=SRCDIR)
    except subprocess.CalledProcessError:
        return None


def get_git_upstream_remote():
    """Get the remote name to use for upstream branches.

    Uses "upstream" if it exists, "origin" otherwise
    """
    cmd = "git remote get-url upstream".split()
    try:
        subprocess.check_output(cmd, stderr=subprocess.DEVNULL, cwd=SRCDIR)
    except subprocess.CalledProcessError:
        return "origin"
    return "upstream"


if __name__ == "__main__":
    args = sys.argv[:]

    logging.basicConfig(level=logging.WARN)

    # git_touch(args)

    # The above is basically a placeholder. This should be run interactively
    # and will expose commands as necessary and give useful defaults and
    # prompts that guide users in the right direction to running a correct
    # command short of "read 170 different man pages"
