#!/usr/bin/env python
# Maintainer: Faris Chugthai
"""Simple module that pretty prints the user's environment variables.

This is actually implemented as an IPython magic but to make it easier
to use in a typical Python REPL it's also implemented here.

The ``if name == '__main__'`` is left off so that it can be run directly
or sourced.

"""
import os
import pprint


def current():
    """Prints all current environment variables."""
    pprint.pprint(sorted(os.environ.items()))
    return dict(sorted(os.environ.items()))


class Env:
    """Memoize the user's current environment variable settings."""

    def __init__(self, env=None):
        if env is None:
            self.env = dict(os.environ.copy())
        else:
            self.env = env

        # eh there should be a cleaner way to do this.
        # self.windows = True if platform.system() == 'Windows'

    @property
    def _is_windows(self):
        """TODO"""
        pass


# wow this is god awful


class WindowsEnv(Env):
    """Windows specific things."""

    def __init__(self, admin=False):
        import winreg

        if admin:
            self.key = "HKEY_CURRENT_USER"
        else:
            self.key = "HKEY_LOCAL_MACHINE"
        self.key.prepend("winreg.")

    def get_registry(self):
        pass
