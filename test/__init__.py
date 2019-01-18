#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Requires setuptools to declare namespace package."""
import pkg_resources

import logging
from logging import NullHandler

pkg_resources.declare_namespace(__name__)
logging.getLogger(__name__).addHandler(NullHandler())