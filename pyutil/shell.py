#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Base class for shell commands.

In it's current state the Command class is unusable but the BaseCommand class
is interesting and a good starting point.

05/14/2019

Moved the _validate function on its own. It doesn't entirely make sense to have
it with an instance or class because if the class is instantiated and _validate
is invoked by the user it doesn't really make sense.

It's better to leave it in the module for consistency and then have the class
simply utilize it.


"""
import codecs
import logging
import os
import shlex
import subprocess
import sys

LOGGER = logging.getLogger(name=__name__)


class Command:
    """Run a shell command."""

    def __init__(self, shell=None, *args, **kwargs):
        """Initialize the command."""
        self.shell = shell

    def _vers(self):
        vers = sys.version_info[0:2]
        if vers > (
                3,
                6,
        ):
            has37 = True
        else:
            has37 = False

        return has37

    def get_shell(self):
        """Determine the user's shell. May be able to decorate with property."""
        try:
            self.shell = os.getenv('SHELL')
        except OSError:
            self.shell = os.getenv('COMSPEC')

        return self.shell

    def run(self, args, kwargs):
        """Run a command."""
        if Command._vers(self):
            # subprocess.run([cmd], capture_output=True)
            subprocess.run([args], kwargs)


class BaseCommand:
    """Create a base command class.

    Pass ``cmd`` to :mod:`subprocess` and process output and build in logging.

    .. todo:: Use ``cmd`` or ``*args``.

    """

    def __init__(self, cmd=None):
        self.cmd = cmd
        logging.debug("Cmd is: " + str(self.cmd))

    def run(self):
        """Run a safer subprocess.

        Currently getting a TypeError. Need to cast to str. Might need to
        define __str__.

        Parameters
        ----------
        cmd : list, optional
            cmd to run in subprocess
        *args : list of str
            Command and parameters to be executed

        Returns
        -------
        output : bytes
            Output from subprocess. Can return `NoneType` if no `cmd`.

        Examples
        --------
        >>> BaseCommand().run('python', '--version')

        """
        try:
            self.cmd = shlex.quote(str(self.cmd))
        except TypeError:
            return None

        output = subprocess.run(self.cmd, capture_output=True)

        validated_output = _validate(output)
        return validated_output

    def popen(self, cmd=None):
        """Execute the required command in a subshell.

        First the command is split using :mod:`shlex`.

        A new process is created, and from the resulting subprocess object
        the :func:`subprocess.Popen().wait()` is invoked.

        When the subprocess returns, any non-zero value will lead to a
        `SystemExit` with a passed value of `returncode`.
        If we don't need to capture output, check the return code.

        Parameters
        ----------
        cmd : list, optional
                cmd to run in subprocess

        Returns
        -------
        process.returncode : int
            Output from subprocess.

        Raises
        ------
        subprocess.CalledProcessError
            If there is an error in the command.

        """
        if self.self.cmd:
            self.self.cmd = shlex.split(self.cmd)
            logging.debug("Cmd is: " + str(self.self.cmd))
            process = subprocess.Popen([self.self.cmd])

        if process.wait():
            raise SystemExit(process.returncode)
        else:
            return process.returncode


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
