#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in IPython startup.

NOQA F401

"""
import logging
from logging import NullHandler
import os
from pkgutil import extend_path
import sys

import pkg_resources

logging.getLogger(__name__).addHandler(NullHandler())

pkg_resources.declare_namespace(__name__)

__path__ = extend_path(sys.path, __file__)

sys.path.insert(0, os.path.dirname(os.path.abspath(__name__)))

# noqa
import pyutil

from pyutil.__about__ import (
    __author__,
    __copyright__,
    __description__,
    __docformat__,
    __license__,
)

