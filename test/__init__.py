#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in IPythom startup."""
import logging
from logging import NullHandler
import os
import sys

logging.getLogger(__name__).addHandler(NullHandler())

sys.path.insert(0, os.path.dirname(os.path.abspath('.')))
