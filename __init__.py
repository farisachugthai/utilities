#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in IPython startup."""
import logging
from logging import NullHandler
from pkgutil import extend_path
import sys

import pkg_resources

import pyutil  # noqa F401
from pyutil.__about__ import (  # noqa F401
    __author__, __copyright__, __description__, __docformat__, __license__,
)

pyutil = logging.getLogger(__name__)

pkg_resources.declare_namespace(__name__)
