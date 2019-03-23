#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Well this isn't set up yet but if you want something that may help.

See Also
--------
:mod:`IPython.utils.tempdir`


Gives you::


    class NamedFileInTemporaryDirectory(object):

        def __init__(self, filename, mode='w+b', bufsize=-1, **kwds):
            Open a file named `filename` in a temporary directory.

            This context manager is preferred over `NamedTemporaryFile` in
            stdlib `tempfile` when one needs to reopen the file.

            Arguments `mode` and `bufsize` are passed to `open`.
            Rest of the arguments are passed to `TemporaryDirectory`.


And also gives you a new TemporaryDirectory class.


"""
import logging
import os
from pathlib import Path
import tempfile
import unittest

from pyutil import backup_nt_and_posix


class TestBackupDirectory(unittest.TestCase):
    """Test that a directory was backed up correctly."""

    long_message = True  # is this how we do this?

    def setUp(self):
        """Create a temporary directory to backup."""
        d = Path(tempfile.TemporaryDirectory())
        for i in range(10):
            tempfile.mktemp(dir=d)

        logging.debug("The temp files in the temp dir are: ")
        logging.debug(os.listdir(d))

    def test_timestamped_dir(self):
        """Test that a directory is backed up correctly."""
        self.assertIsInstance(self.setUp.d, tempfile.TemporaryDirectory)
        return_code = backup_nt_and_posix(self.setUp.d)
        self.assertEqual(return_code, 0)


if __name__ == "__main__":
    unittest.main()
