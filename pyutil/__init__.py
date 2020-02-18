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

import pyutil
from pyutil import dlink, dlink2, _paths, _logging

from .__about__ import (  # noqa F401
    __author__,
    __copyright__,
    __description__,
    __docformat__,
    __license__,
    __title__,
    __version__,
)

from . import dlink, dlink2, _logging, _paths, __about__
from .env import Env
from .itersrc import iter_source_code
from .g import Git
from .shell import BaseCommand
from .sys_checks import py_gt_exit, py_gt_raise, py_lt_exit

init_logger = logging.getLogger(__name__)
