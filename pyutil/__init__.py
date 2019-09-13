#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in :mod:`IPython` startup.

Mar 19, 2019

So with our ``sys.path`` hack, we can now do the following successfully::

    from pyutil import g

Let it doctest!

>>> import pyutil
>>> from pyutil import g

"""
import argparse
import logging
from logging import NullHandler
import os
import sys

logging.getLogger(__name__).addHandler(NullHandler())

PYUTIL_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, PYUTIL_DIR)

import pyutil
from pyutil import dlink, dlink2, _paths, _logging

from .__about__ import (  # noqa F401
    __author__, __copyright__, __description__, __docformat__, __license__,
    __title__, __version__)

from .env import Env
from .g import Git
from .itersrc import iter_source_code
from .shell import BaseCommand
from .sys_checks import py_gt_exit, py_gt_raise, py_lt_exit
