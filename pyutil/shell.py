#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Base class for shell commands."""
import os
import sys
import subprocess


class Command:
    """Run a shell command."""

    def __init__(self, shell=None, *args, **kwargs):
        """Initialize the command."""
        shell = self.shell
        args = self.args
        kwargs = self.kwargs

    def _vers(self):
        vers = sys.version_info[0:2]
        if vers > (3, 6, ):
            has37 = True
        else:
            has37 = False

        return has37

    def get_shell(self):
        """Determine the user's shell. May be able to decorate with property."""
        try:
            shell = os.getenv('SHELL')
        except OSError:
            shell = os.getenv('COMSPEC')

        return shell

    def run(self, args, kwargs):
        """Run a command."""
        if Command._vers(self):
            # subprocess.run([cmd], capture_output=True)
            subprocess.run([args], kwargs)
