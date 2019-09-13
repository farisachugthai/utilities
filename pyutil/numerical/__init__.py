#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from logging import NullHandler
import os
from pkgutil import extend_path
import sys

import pkg_resources

logging.getLogger(__name__).addHandler(NullHandler())

pkg_resources.declare_namespace(__name__)

sys.path.insert(0, os.path.dirname(os.path.abspath(__name__)))

import pyutil
from .gcd_iter import gcd_iter
from .gcd_recur import gcd_recur
