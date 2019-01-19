<<<<<<< .merge_file_ffPzC1
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Vim: set ft=python:
import re
import os


def find_pics(path):
    """Finds jpegs and jpgs.
    One of my rare successful invocations of re.

    :param path: path to a directory to check
    :type path: str or path-like object

    :yields: an re-match object

    TODO:
        Format the match object so it's more usable

    All in all its functional though!
    """
    matched = re.match(".*jp(e)?g", f)
    if matched:
        yield f


if __name__ == "__main__":
    path = os.listdir(".")
    # list comprehesion with a function?
    matches = [i if find_pics(path) for f in path]
||||||| .merge_file_P0PA8s
=======
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
>>>>>>> .merge_file_JukKV2
