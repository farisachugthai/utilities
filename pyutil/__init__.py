#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This package is undergoing a thorough rewriting.

Set up logging in a general manner and use :mod:`pkg_resources` provided by
:mod:`setuptools` in order to create the directory as a namespace package.

Jan 21, 2019.

Still haven't cleanly figured out what **needs** to go in this file.

Now that there's a working `setup file <../setup.py>`_ I'm not sure if we need
to use either pkg_util or pkg_resources.
"""
import logging
from logging import NullHandler
from pkg_util import extend_path

import pkg_resources

from __about__ import (
    __author__,
    __copyright__,
    __description__,
    __docformat__,
    __email__,
    __license__,
    __title__,
    __package_name__,
)

logging.getLogger(__name__).addHandler(NullHandler())

pkg_resources.declare_namespace(__name__)

__path__ = extend_path(__path__, __name__)
