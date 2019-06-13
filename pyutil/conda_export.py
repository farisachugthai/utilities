#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Iterate over the list of conda environments that are present.

Update and upgrade Conda environments programmatically.

Just found the `docs`_ for interfacing with Conda with Python.

.. _docs: https://conda.io/projects/conda/en/latest/api/python_api.html

"""
import argparse
import codecs
from shlex import split
from subprocess import run, PIPE
import sys

try:
    from conda.cli.python_api import Commands, run_command
except (ImportError, ModuleNotFoundError):
    sys.exit('Conda not installed.')

from pyutil.__about__ import __version__


def _parse_arguments():
    """Parse user arguments based on the information given by the class
    :class:`conda.cli.python_api.Commands`.

    Returns
    -------
    args : namespace
        :mod:`argparse` arguments.

    """
    commands = [method for method in dir(Commands) if not method.startswith('_')]

    parser = argparse.ArgumentParser(prog='%(prog)s',
            description="Interface with Conda in an automated fashion.",
            epilog="Commands: {}".format(',\t,'.join(commands)))

    parser.add_argument(
        'command',
        nargs='+',
        type=str,  # wait how is this not bytes
        choices=dir(Commands),
        help='Optional. Command to pass to Conda.')

    parser.add_argument(
        '-u',
        '--update-all-envs',
        dest='update',
        action='store_true',
        help='Iterate through all Conda environments and update all.')

    parser.add_argument(
        '-V', '--version', action='version', version='%(prog)s' + __version__)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        return parser.parse_args()


def _cmd_wrapper(cmd=None):
    """Handle any command that the user wants to pass to conda.

    The module should be able to execute and produce meaningful output without
    a user provided argument.

    .. note::

        :kbd:`-u` seemingly doesn't do anything.

    Parameters
    ----------
    cmd : str, optional
        cmd to pass to conda

    Returns
    -------
    output : str
        Output from subprocess passed to conda. Can return `NoneType` if no
        `cmd`.

    """
    if cmd:
        pieces = split(cmd)
        # if len(pieces) == 1:
        if not pieces[0] == 'conda':
            pieces.insert(0, 'conda')

        output = run([pieces], capture_output=True)
        return output


def get_envs():
    """Iterate through conda environments.

    Return a list holding each environment as an element. Providing the argument
    `universal_newlines=True` should allow the implementation to skip the
    `_validate` function; however, it's provided as a backup.

    Returns
    --------
    `short_envs` : list
        list of conda environments

    Examples
    --------

    .. code-block:: shell-session

        $ python3 conda_export.py
        # ['base', 'dynamic', 'flask', 'navigator', 'tdd', 'utilities']

    """
    envlist = run(["conda", "env", "list"], stdout=PIPE, stderr=PIPE, universal_newlines=True)

    if envlist.returncode != 0:
        sys.exit(envlist.returncode)
    else:
        # Most returned values from the system are gonna be in bytes. However we should check
        if not isinstance(envlist.stdout, str):
            decoded = codecs.decode(envlist.stdout)
        else:  # even if it is a str, keep the name change consistent.
            decoded = envlist.stdout

        # Now let's take this long unwieldy string we have and clean it up
        decoded = decoded.splitlines()
        # Initially it prints out a few unnecessary lines. Let's chop them off
        envs = decoded[2:-1]

        short_envs = []
        # now let's get rid of extraneous info
        for env in envs:
            short_envs.append(env.split()[0])

        return short_envs


def main():
    """Call other functions."""
    # First things first
    args = _parse_arguments()
    try:
        cmd = args.comm
    except IndexError:  # ? idk what error
        full_name_envs = get_envs()
        return full_name_envs
    # else:
    #     return _cmd_wrapper(cmd)


if __name__ == "__main__":
    sys.exit(main())
