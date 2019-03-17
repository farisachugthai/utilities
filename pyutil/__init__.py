#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize the package for all scripts used in IPython startup.

This module intends to establish a few different things.

    - Initialize logging in a general manner.
    - Use :mod:`pkg_resources` provided by :mod:`setuptools` in order to create the directory as a namespace package
    - Define generic dunder methods.
    - Extend the user's ``$PATH `` to include this directory even if it != os.cwd


NOQA F401

"""
import logging
from logging import NullHandler
import os
from pkgutil import extend_path
import sys

import pkg_resources

from pyutil.__about__ import (  # noqa F401
    __author__, __copyright__, __description__, __docformat__, __license__,
    __title__, __package_name__,
)

__all__ = [
    'backup_nt_and_posix',
    'batch_renamer',
    'check_IP',
    'conda_export',
    'dir_cleaner',
    'dlink',
    'dlink2',
    'dot_sym',
    'env',
    'env_checks',
    'find_pics',
    'g',
    'inspect_module',
    'itersrc',
    'json_sorter',
    'lazy_downloader',
    'linktree',
    'magic_aid',
    'mv_to_repo',
    'nvim_profiling',
    'ptags',
    'rclone',
    'strip_space',
    'sys_checks',
    'wrap',
    'yes_no_question',
]

logging.getLogger(__name__).addHandler(NullHandler())

logging.basicConfig(level=logging.DEBUG)

pyutil_d = os.path.dirname(os.path.abspath('__init__.py'))

logging.debug('Path is: ' + str(sys.path))

__path__ = extend_path(sys.path, pyutil_d)

logging.debug('Path is: ' + str(sys.path))

print(os.path.dirname(__file__))


logging.debug("Namespace would be: " + os.path.dirname(__file__))

pkg_resources.declare_namespace(os.path.dirname(__file__))
