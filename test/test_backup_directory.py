#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Well this isn't set up yet but if you want something that may help.

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
import logging
import os
import tempfile
import unittest

from pyutil.backup_nt_and_posix import timestamped_dir

logging.getLogger(name=__name__)


class TestBackupDirectory(unittest.TestCase):
    """Test that a directory was backed up correctly."""

    long_message = True  # is this how we do this?

    def setUp(self):
        """Create a temporary directory to backup."""
        d = tempfile.TemporaryDirectory()
        logging.debug("The temp dir is: ")
        logging.debug(d)
        return d

    def test_timestamped_dir(self):
        """Test that a directory is backed up correctly."""
        d = self.setUp()
        return_code = timestamped_dir(d, path=os.path.abspath(d))
        self.assertEqual(return_code, 0)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
