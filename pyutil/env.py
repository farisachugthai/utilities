#!/usr/bin/env python
# Maintainer: Faris Chugthai
"""Simple module that handles the user's environment variables.

This file can be either executed directly or sourced in a startup file.
"""
import os
import pprint


def to_console():
    """Print env vars to console."""
    pprint.pprint(sorted(os.environ.items()))


def env_ns():
    """Save the env vars for use in a REPL namespace."""
    env = os.environ.copy()
    return env


if __name__ == "__main__":
    to_console()
