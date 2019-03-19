#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    sphinxcontrib
    ~~~~~~~~~~~~~

    This package is a namespace package that contains all extensions
    distributed in the ``sphinx-contrib`` distribution.

    :copyright: Copyright 2007-2014 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
import logging
from logging import NullHandler
from pkgutil import extend_path
import os
import sys

import pkg_resources

from pyutil.__about__ import (
    __author__,
    __copyright__,
    __description__,
    __docformat__,
    __license__,
)

logging.getLogger(__name__).addHandler(NullHandler())

# pkg_resources.declare_namespace(__name__)

__import__('pkg_resources').declare_namespace(__name__)

__path__ = extend_path(sys.path, __name__)

sys.path.insert(0, os.path.dirname(os.path.abspath(__name__)))
