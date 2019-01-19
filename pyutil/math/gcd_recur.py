<<<<<<< .merge_file_6bfWeK
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Give a one sentence summary in the imperative

Elaborate a little
File:
Author: Faris Chugthai
Email: farischugthai@gmail.com
Github: https://github.com/farisachugthai

Attributes:

    module_level_variables (type): Explanation and give an inline docstring
    immediately afterwards if possible

Example:

    Any example of how to use this module goes here:: sh

        $ python exampleofrst.py

.. 'any directives::'

    example text

"""
import sys


def gcdRecur(a, b):
    if b == 0:
        return a
    if b > a:
        tmp = b
        b = a
        a = tmp
    return gcdRecur(b, a % b)


if __name__ == "__main__":
    a, b = sys.argv[1:3]
    gcdRecur(a, b)
||||||| .merge_file_CnzHcT
=======
def gcdRecur(a, b):
    if b == 0:
        return a
    if b > a:
        tmp = b
        b = a
        a = tmp
    return gcdRecur(b, a % b)
>>>>>>> .merge_file_PwL4vK
