#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Display an iterative method for determining the greatest common denom.

Jan 17, 2019:

    Just added in :mod:`sys` so that we accept input from the user.

"""
import sys


def gcd_iter(a, b):
    """Find the greatest common denominator with 2 arbitrary integers.

    Parameters
    ----------
    a : int
        User provided integer
    b : int
        User provided integer

    Returns
    -------
    gcd : int

    """
    orig_b = b
    orig_a = a
    if a > b:
        while b > 0:
            if a % b == 0 and orig_b % b == 0:
                return b
            b -= 1
    else:
        while a > 0:
            if b % a == 0 and orig_a % a == 0:
                return a
            a -= 1


if __name__ == "__main__":
    args = sys.argv[:]
    if len(args) > 2:
        a = args[1]
        b = args[2]
    gcd_iter(a, b)
