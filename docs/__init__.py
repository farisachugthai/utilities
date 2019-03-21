#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in IPython startup.

This module intends to establish a few different things.

    - Initialize logging in a general manner.
    - Use :mod:`pkg_resources` provided by :mod:`setuptools` in order to create the directory as a namespace package
    - Define generic dunder methods.
    - Extend the user's ``$PATH `` to include this directory even if it != os.cwd


NOQA F401

"""
import logging
from logging import NullHandler
import os
import sys

from pyutil.__about__ import (
    __author__,
    __copyright__,
    __description__,
    __docformat__,
    __license__,
)

logging.getLogger(__name__).addHandler(NullHandler())

sys.path.insert(0, os.path.dirname(os.path.abspath('.')))
