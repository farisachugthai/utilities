#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module that finds jpg and jpegs files in the current dir.

.. module:: find_pics
    :synopsis: Module that finds jpg and jpegs files in the current dir.

.. todo:: Should accept command line arguments.

We'll say that another thing on the todo list is
return a path-like object from :func:`find_pics()`.
# print(os.path.abspath(match)

"""
import re
import os


def find_pics(picture):
    """Finds jpegs and jpgs.

    .. todo:: Format the match object so it's more usable


    Parameters
    ----------
    picture : str
        Path to a file that may or may not be a jpg/jpeg


    Yields
    ------
    matched : :class:`re.match()` object
        Filename that matches a jpg/jpeg regex.

    """
    matched = re.match(".*jp(e)?g", picture)
    if matched:
        yield matched


if __name__ == "__main__":
    path = os.listdir(".")

    matches = [f for f in path if find_pics(f)]
