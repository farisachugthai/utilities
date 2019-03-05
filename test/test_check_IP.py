#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unit tests for :mod:`pyutil.check_IP`.

.. module:: test_check_IP.py

"""
import unittest

from pyutil import check_IP


class TestCheckIP(unittest.TestCase):
    """Ensure :mod:`check_IP` behaves as expected.

    In addition, appreciate the need to stop naming functions using verbs.
    TestCheck is such a clumsy sounding string of words.
    """

    def test_get_public_url(self):
        """Assert that we received a status code that indicated success."""
        response = check_IP.get_public_ip()
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
