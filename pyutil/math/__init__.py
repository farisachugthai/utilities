#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Requires setuptools to declare namespace package."""
from pkgutil import extend_path
import sys

import pkg_resources

pkg_resources.declare_namespace(__name__)
__path__ = extend_path(sys.path, __file__)
