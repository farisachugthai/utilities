#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This package is undergoing a thorough rewriting.

Set up logging in a general manner and use :mod:`pkg_resources` provided by
:mod:`setuptools` in order to create the directory as a namespace package.
"""
import logging
from logging import NullHandler
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
