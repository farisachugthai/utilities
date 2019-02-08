#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test :mod:`find_pics`.

:File: test_find_pics.py
:Author: Faris Chugthai
:Github: https://github.com/farisachugthai

"""
import tempfile
import unittest

from pyutil import find_pics


class TestFindPics(unittest.TestCase):
    """Tests for :mod:`pyutil.find_pics`."""

    def setUp(self):
        """Create dummy temporary picture files."""
        with tempfile.TemporaryFile() as f:  # don't know what args it needs
            pass


if __name__ == "__main__":
    unittest.main()
