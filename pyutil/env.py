#!/usr/bin/env python
# Maintainer: Faris Chugthai
"""Simple module that pretty prints the user's environment variables.

This is actually implemented as an IPython magic but to make it easier
to use in a typical Python REPL it's also implemented here.

The if name == '__main__' is left off so that it can be run directly
or sourced.
"""
import os
import pprint


def current():
    """Prints all current environment variables."""
    pprint.pprint(sorted(os.environ.items()))
