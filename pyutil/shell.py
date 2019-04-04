#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Base class for shell commands."""
import os
import sys
import subprocess


class Command(*args=None, **kwargs=None):
    """Run a shell command."""

    def __init__(self, shell=None, *args, **kwargs):
        """Initialize the command."""
        shell = self.shell
        args = self.args
        kwargs = self.kwargs

    def _vers(self):
        VERS = sys.version_info[0:2]
        if VERS > (3, 6, ):
            HAS37 = True
        else:
            HAS37 = False

    def get_shell(self):
        """Determine the user's shell. May be able to decorate with property."""
        try:
            shell = os.getenv('SHELL')
        except OSError:
            shell = os.getenv('COMSPEC')

        return shell

    def run(self, args, kwargs):
        """Run a command."""
        if _vers(self):
            # subprocess.run([cmd], capture_output=True)
            subprocess.run([args], kwargs)
