<<<<<<< .merge_file_RyckgA
def gcdIter(a, b):
    orig_b = b
    orig_a = a
    if a > b:
        while(b > 0):
            if a % b == 0 and orig_b % b == 0:
                return b
            b -= 1
    else:
        while(a > 0):
            if b % a == 0 and orig_a % a == 0:
                return a
            a -= 1

# alright you fucked this up. 
# let's think about gcd(9, 12). It returned 6. 
# a decrements and then when it gets to 6, 12 % 6 == 0. So it works.
# You need to save the original values of both variables in tmp vars
# and then when you run the if a % b == 0, you need to do that in the form of
# if a % b and original_b % b == 0 then you're good.
# honestly it took more typing to write these comments but i don't feel
# like rewriting this code i wanna move forward.
||||||| .merge_file_XnovNX
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Display an iterative method for determining the greatest common denom.

:File: gcd_iter.py
:Author: Faris Chugthai
:Email: farischugthai@gmail.com
:Github: https://github.com/farisachugthai

Jan 17, 2019:

    Just added in :mod:`sys` so that we accept input from the user.

.. todo::

    Let's think about gcd(9, 12). It returned 6.
    a decrements and then when it gets to 6, 12 % 6 == 0. So it works.
    You need to save the original values of both variables in tmp vars
    and then when you run the if a % b == 0, you need to do that in the form of
    if a % b and original_b % b == 0 then you're good.
"""
import sys


def gcdIter(a, b):
    orig_b = b
    orig_a = a
    if a > b:
        while(b > 0):
            if a % b == 0 and orig_b % b == 0:
                return b
            b -= 1
    else:
        while(a > 0):
            if b % a == 0 and orig_a % a == 0:
                return a
            a -= 1


if __name__ == "__main__":
    args = sys.argv[:]
    if len(args) > 2:
        a = args[1]
        b = args[2]
    gcdIter()
>>>>>>> .merge_file_1MPA76
