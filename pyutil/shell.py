#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import logging
import reprlib
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
        if self.cmd is None:
            return "BaseCommand: No cmd initialized"
        else:
            return "BaseCommand: {!r}".format(self.cmd)

    def run(self):
        """Run a safer subprocess.

        Parameters
        ----------
        cmd : list, optional
            cmd to run in subprocess
        *args : list of str
            Command and parameters to be executed

        Returns
        -------
        output : str
            Output from subprocess. Can return `NoneType` if no `cmd`.

        Examples
        --------
        >>> BaseCommand(['ls']).run()
        ... CompletedProcess(args='ls', returncode=0...)


        """
        shlexed_cmd = shlex.quote(" ".join(i for i in self.cmd if i))
        output = subprocess.run(shlexed_cmd, capture_output=True, text=True)
        # meth call should be something like reprlib.aRepr.repr_str(str, level)
        # aRepr isn't callable so don't worry about initializing
        # logging.info('Output: %s' % reprlib.Repr(output))
        return output

    def popen(self):
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
        if not self.cmd:
            return

        self.cmd = shlex.split(self.cmd)
        logging.debug("Cmd is: " + str(self.cmd))
        process = subprocess.Popen([self.cmd])

        if process.wait():
            raise subprocess.CalledProcessError(process.returncode)
        else:
            return process.returncode
