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
import shlex
import subprocess

LOGGER = logging.getLogger(name=__name__)


class BaseCommand:
    """Create a base command class.

    Pass ``cmd`` to :mod:`subprocess` and process output and build in logging.


    """

    def __init__(self, cmd=None):
        self.cmd = cmd

    def __repr__(self):
        return 'BaseCommand: {!r}'.format(self.cmd)

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
            self.cmd = shlex.split(shlex.quote(str(self.cmd)))
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
        if self.cmd:
            self.cmd = shlex.split(self.cmd)
            logging.debug("Cmd is: " + str(self.cmd))
            process = subprocess.Popen([self.cmd])

        if process.wait():
            raise SystemExit(process.returncode)
        else:
            return process.returncode


def _validate(subprocess_output):
    """Take output from :func:`subprocess.run()` and test

    First the func will check :attr:`returncode`.

    Then the bytes that were returned from the *presumably* Unix OS
    will be decoded into a human readable format.

    Admittedly, the subprocess.run() parameter universal_newlines
    would've been simpler than this.
    """
    if subprocess_output.returncode != 0:
        logging.error(subprocess_output.returncode)

    if isinstance(subprocess_output.stdout, bytes):
        decoded_output = codecs.decode(subprocess_output.stdout)
        # also probably gonna wanna pprint that when you receive it
        return decoded_output
    else:
        logging.warning("Subprocess didn't return bytes. Maybe str? Type was:")
        logging.warning('%s' % type(subprocess_output.stdout))
        return subprocess_output
