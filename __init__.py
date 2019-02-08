#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""First time for us too buddy."""
import logging
from logging import NullHandler

import sys

from pkgutil import extend_path

__path__ = extend_path(sys.path, __name__)

logging.getLogger(__name__).addHandler(NullHandler())
