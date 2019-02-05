#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Requires setuptools to declare namespace package."""
from pkgutil import extend_path
import sys

import pkg_resources

__path__ = extend_path(sys.path, __file__)

pkg_resources.declare_namespace(__name__)
