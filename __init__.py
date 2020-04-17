#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in IPython startup."""
import logging
from logging import NullHandler
import sys

import pyutil  # noqa F401
from pyutil.__about__ import (  # noqa F401
    __author__, __copyright__, __description__, __docformat__, __license__,
)

pyutil_logger = logging.getLogger(__name__)
