#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in IPython startup.

Mar 19, 2019

So with our sys.path hack, we can now do the following successfully::

    from pyutil import g

However we still have a problem.

Scratch that!::

    import pyutil.env

Now successfully works!!!

Let it doctest!

>>> import pyutil
>>> import pyutil.ytdl
>>> from pyutil import g


NOQA F401

"""
import logging
from logging import NullHandler
import os
import sys

import pkg_resources

from .__about__ import (  # noqa F401
    __author__, __copyright__, __description__, __docformat__, __license__,
    __title__,
)

logging.getLogger(__name__).addHandler(NullHandler())

PYUTIL_DIR = os.path.dirname(os.path.abspath('__init__.py'))

sys.path.insert(0, PYUTIL_DIR)

pkg_resources.declare_namespace('.')
