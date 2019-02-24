#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test that the batch renamer handles filenames correctly.

:File: test_batch_renamer.py
:Author: Faris Chugthai
:Email: farischugthai@gmail.com
:Github: https://github.com/farisachugthai

"""
import unittest
from pyutil import batch_renamer


class BatchTestCase(unittest.TestCase):
    """Tests for :mod:`batch_renamer`."""

    def test_fix_extension(self):
        """Do filenames like 'shutil.rst.txt' work?"""
        # todo
        pass

    def test_fix_multipart_filename(self):
        """todo"""
        pass


if __name__ == "__main__":
    unittest.main()
