#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maintainer: Faris Chugthai

import os
import sys

# TODO: FIX THIS FUNCTION DOCSTRING THIS IS GARBAGE!!!


def py_gte(max_py_version):
    """
    Import this function and call it with the highest allowable version
    of python the program accepts.

    If you'll crash on python3.4 but work on 3.3, call this func with 3.3.

    params: max_py_version
        args: tuple
    """
    if sys.version_info > max_py_version:
        sys.exit("Can not use python interpreter above: " + max_py_version)


def main():
    """Checks that system requirements are met."""

# Useful if you import pathlib, pandas etc
    if sys.version_info < (3, 4):
        sys.exit("Requires Python3.4 and up")

    if os.uname()[0] not in ["Darwin", "Linux"]:
        raise OSError("This script assumes a Unix operating system.")
        sys.exit()


if __name__ == '__main__':
    print("Source this file don't run it directly!")
    sys.exit(main())
