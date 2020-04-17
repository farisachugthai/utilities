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
import logging
from logging import NullHandler
import os
import sys

from .__about__ import (  # noqa F401
    __author__,
    __copyright__,
    __description__,
    __docformat__,
    __license__,
    __title__,
    __version__,
)

