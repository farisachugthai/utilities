#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Wrap text similarly to :func:`textwrap.dedent()` but with multiple paragraphs.

Allow the user to input any parameters that are accepted by
:class:`textwrap.TextWrapper()`

.. seealso:: :mod:`IPython.utils.text`


"""
import re
import sys
from textwrap import dedent, fill, TextWrapper

try:
    from prompt_toolkit import print_formatted_text as print
except (ImportError, ModuleNotFoundError):
    pass

from pyutil.sys_checks import is_file


class ZimText(TextWrapper):
    """Subclass :class:`textwrap.TextWrapper()`.

    Primarily want to modify initialized arguments.
    Not entirely looking to reimplement the text formatting methods, both
    private and public.
    """

    def __init__(self, text, **kwargs):
        """Initialize the class."""
        self.width = 80
        self.break_long_words = False
        self.break_on_hyphens = False
        super().__init__(**kwargs)


def wrap_paragraphs(text, ncols=80):
    """Wrap multiple paragraphs to fit a specified width.

    This is equivalent to :func:`textwrap.wrap()`, but with support for multiple
    paragraphs, as separated by empty lines.

    Considering initializing an instance of :class:`textwrap.TextWrapper()`
    for increased configurability.

    Parameters
    ----------
    text : str
        text to wrap using :mod:`re` and :func:`textwrap.dedent()`
    ncols : int
        column to wrap text at


    Returns
    -------
    wrapped_text : list of str
        list of complete paragraphs, wrapped to fill `ncols` columns.


    """
    paragraph_re = re.compile(r'\n(\s*\n)+', re.MULTILINE)
    text = dedent(text).strip()
    paragraphs = paragraph_re.split(text)[::2]  # every other entry is space
    wrapped_text = []
    indent_re = re.compile(r'\n\s+', re.MULTILINE)
    for p in paragraphs:
        # presume indentation that survives dedent is meaningful formatting,
        # so don't fill unless text is flush.
        if indent_re.search(p) is None:
            # wrap paragraph
            p = fill(p, ncols)
        wrapped_text.append(p)
    return wrapped_text


if __name__ == '__main__':
    args = sys.argv[:]
    if len(args) < 2:
        print("Needs a file to reformat as an argument.")
        raise RuntimeError
    else:
        for i in args[1:]:
            if is_file(i):
                wrap_paragraphs(args[1:])
