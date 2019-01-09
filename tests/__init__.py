#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Slight variation on the one in the std lib."""
from pkgutil import extend_path
import sys

path = sys.path

__path__ = extend_path(path, __name__)
