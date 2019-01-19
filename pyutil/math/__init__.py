<<<<<<< .merge_file_HrbRks
import logging
from logging import NullHandler
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)
logging.getLogger(__name__).addHandler(NullHandler())
||||||| .merge_file_KtWP2F
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Requires setuptools to declare namespace package."""
import pkg_resources
pkg_resources.declare_namespace(__name__)
>>>>>>> .merge_file_nyJUKh
