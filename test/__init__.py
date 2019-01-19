<<<<<<< .merge_file_2zDSsD
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Slight variation on the one in the std lib."""
from pkgutil import extend_path
import sys

path = sys.path

__path__ = extend_path(path, __name__)
||||||| .merge_file_g2aOos
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Requires setuptools to declare namespace package."""
import pkg_resources

import logging
from logging import NullHandler

pkg_resources.declare_namespace(__name__)
logging.getLogger(__name__).addHandler(NullHandler())
>>>>>>> .merge_file_4JRMlx
