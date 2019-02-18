#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Display an iterative method for determining the greatest common denom.

:File: gcd_iter.py
:Author: Faris Chugthai
:Github: `<https://github.com/farisachugthai>`_

Jan 17, 2019:

    Just added in :mod:`sys` so that we accept input from the user.

.. todo::

    Let's think about ``gcd(9, 12)``. It returned 6.
    ``a`` decrements and then when it gets to 6, 12 % 6 == 0. So it works.

    You need to save the original values of both variables in tmp vars
    and then when you run the ``if a % b == 0``, do that in the form of
    ``if a % b`` and ``original_b % b == 0`` then you're good.

"""
import sys


def gcd_iter(a, b):
    """Find the greatest common denominator with 2 arbitrary integers."""
    orig_b = b
    orig_a = a
    if a > b:
        while (b > 0):
            if a % b == 0 and orig_b % b == 0:
                return b
            b -= 1
    else:
        while (a > 0):
            if b % a == 0 and orig_a % a == 0:
                return a
            a -= 1


if __name__ == "__main__":
    args = sys.argv[:]
    if len(args) > 2:
        a = args[1]
        b = args[2]
    gcd_iter()
