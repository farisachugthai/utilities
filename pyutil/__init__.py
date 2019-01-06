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
"""
from __about__ import (
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

logging.getLogger(__name__).addHandler(NullHandler())
