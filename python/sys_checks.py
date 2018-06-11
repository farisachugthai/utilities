#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maintainer: Faris Chugthai

import os
import sys


def main():
    """Checks that system requirements are met."""

# Useful if you import pathlib, pandas etc
    if sys.version_info < (3, 4):
        sys.exit("Requires Python3.4 and up")

    if os.uname()[0] not in ["Darwin", "Linux"]:
        raise OSError("This script assumes a Unix operating system.")
        sys.exit()
