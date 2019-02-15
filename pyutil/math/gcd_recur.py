#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find the greatest common denominator using a slightly different algorithm.

:File: gcd_recur.py
:Author: Faris Chugthai
:Github: `<https://github.com/farisachugthai>`_


"""
import sys

def gcd_recur(a, b):
    """Find the greatest common denominator with 2 arbitrary integers."""
    if b == 0:
        return a
    if b > a:
        tmp = b
        b = a
        a = tmp
    return gcd_recur(b, a % b)


if __name__ == "__main__":
    args = sys.argv[:]
    if len(args) > 2:
        a = args[1]
        b = args[2]
    gcd_recur()
