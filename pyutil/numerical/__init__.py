#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from logging import NullHandler
import os
import sys

logging.getLogger(__name__).addHandler(NullHandler())

sys.path.insert(0, os.path.dirname(os.path.abspath(__name__)))

import pyutil
from .gcd_iter import gcd_iter
from .gcd_recur import gcd_recur
