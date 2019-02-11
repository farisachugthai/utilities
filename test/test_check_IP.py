#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyutil import check_IP

import unittest


class TestCheckIP(unittest.TestCase):
    """Ensure :mod:`check_IP` works 
    
    In addition, appreciate the need to never name a function using a verb.
    TestCheck is such a clumsy sounding string of words...abs
    """
    def test_get_public_url(self):
        """Assert that we received a status code that indicated success."""
        response = check_IP.get_public_ip()
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
