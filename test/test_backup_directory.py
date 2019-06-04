#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Well this isn't set up yet but if you want something that may help.

.. highlight:: python3

See Also
--------
:mod:`IPython.utils.tempdir`

That module gives you::

    class NamedFileInTemporaryDirectory(object):
        def __init__(self, filename, mode='w+b', bufsize=-1, **kwds):
            '''Open a file named `filename` in a temporary directory.
            This context manager is preferred over `NamedTemporaryFile` in
            stdlib `tempfile` when one needs to reopen the file.
            Arguments `mode` and `bufsize` are passed to `open`.
            Rest of the arguments are passed to `TemporaryDirectory`.'''


And also gives you a new :class:`tempfile.TemporaryDirectory` class.


"""
import atexit
import os
import shutil
import tempfile
import unittest

from pyutil.backup_nt_and_posix import timestamped_dir
from pyutil._logging import _set_debugging

LOGGER = _set_debugging()


class TestBackupDirectory(unittest.TestCase):
    """Test that a directory was backed up correctly."""

    long_message = True  # is this how we do this?

    def setUp(self):
        """If the config directory can not be created, create a temporary directory."""
        configdir = (tempfile.mkdtemp(prefix='pyutil-'))
        LOGGER.debug("The temp dir is: %s"  % configdir)
        atexit.register(shutil.rmtree, configdir)
        return configdir

    def test_timestamped_dir(self):
        """Test that a directory is backed up correctly."""
        d = self.setUp()
        return_code = timestamped_dir(d, path=os.path.abspath(d))
        self.assertEqual(return_code, 0)


if __name__ == "__main__":
    unittest.main()
