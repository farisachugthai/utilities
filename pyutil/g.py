#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Export functions to ease IPython/Git interactions.

:File: 40_git_helpers.py
:Author: Faris Chugthai
:Github: `https://github.com/farisachugthai`_

.. todo::

    What version of python was subprocess.check_output() introduced in?


"""
import subprocess
import sys
import sysconfig

# try:
#     from git import Git
# except ImportError:
#     pass
SRCDIR = sysconfig.get_config_var('srcdir')


def git_touch(args):
    """Convenience function that creates a file and git add's it.

    Parameters
    -----------
    args : str (path-like object)
        Path to a file that's needs to be staged and added to the Git index.

    Returns
    --------
    None.

    Examples
    ---------
    TODO

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
        return subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return None


def get_git_branch():
    """Get the symbolic name for the current git branch."""
    cmd = "git rev-parse --abbrev-ref HEAD".split()
    try:
        return subprocess.check_output(cmd,
                                       stderr=subprocess.DEVNULL,
                                       cwd=SRCDIR)
    except subprocess.CalledProcessError:
        return None


def get_git_upstream_remote():
    """Get the remote name to use for upstream branches.

    Uses "upstream" if it exists, "origin" otherwise
    """
    cmd = "git remote get-url upstream".split()
    try:
        subprocess.check_output(cmd,
                                stderr=subprocess.DEVNULL,
                                cwd=SRCDIR)
    except subprocess.CalledProcessError:
        return "origin"
    return "upstream"


if __name__ == "__main__":
    args = sys.argv[:]

    # git_touch(args)

    # The above is basically a placeholder. This should be run interactively
    # and will expose commands as necessary and give useful defaults and
    # prompts that guide users in the right direction to running a correct
    # command short of "read 170 different man pages"
