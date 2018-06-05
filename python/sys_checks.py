#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Maintainer: Faris Chugthai

import os
import sys


def main():
    """
    Just all the system checks that could be performed in any situation.
    """
    if os.uname()[0] != 'Linux':
        raise OSError("This script assumes a Linux operating system.")
        sys.exit()
