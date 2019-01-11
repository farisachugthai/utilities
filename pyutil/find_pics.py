#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os


def find_pics(path):
    """Finds jpegs and jpgs.

    :param path: path to a directory to check
    :type path: str or path-like object

    :yields: an re-match object

    .. todo::

        Format the match object so it's more usable
    """
    matched = re.match(".*jp(e)?g", f)
    if matched:
        yield f


if __name__ == "__main__":
    path = os.listdir(".")
    # list comprehesion with a function?
    matches = [f if find_pics(f) for f in path]
