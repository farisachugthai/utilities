#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in IPythom startup.

:File: __init__.py
:Author: Faris Chugthai
:Github: `https://github.com/farisachugthai`_

This module intends to establish a few different things.

- Initialize logging in a general manner
- Use :mod:`pkg_resources` provided by :mod:`setuptools` in order to
create the directory as a namespace package
- Define generic dunder methods
- Extend the user's $PATH to include this directory even if it != os.cwd
"""
import logging
from logging import NullHandler
from pkgutil import extend_path
import sys

import pkg_resources

from pyutil import *

logging.getLogger(__name__).addHandler(NullHandler())

pkg_resources.declare_namespace(__name__)

__path__ = extend_path(sys.path, __file__)

# Feb 05, 2019: How am i atill having path issues.
