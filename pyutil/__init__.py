#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This package is undergoing a thorough rewriting. Little is currently exported.

As a seal of approval, I'll add modules in one by one.

Dec 24, 2018:

    Wait should you import stuff in the __init__.py file like this?
    I feel like that should be reserved for an __all__.py type thing.

    Yeah I'm taking that out.

from dlink import dlink

import env

2018-12-24 16:46:44-0500

Took a few hours but don't put imports in init. If you must put them in
__main__.py so someone can go python -m mod
"""
from .__about__ import (
    __author__,
    __copyright__,
    __description__,
    __docformat__,
    __email__,
    __license__,
    __title__,
    __package_name__,
)

import logging
from logging import NullHandler

from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)

logging.getLogger(__name__).addHandler(NullHandler())
