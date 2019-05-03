#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Wrap text similarly to :func:`textwrap.dedent()` but with multiple paragraphs.

Allow the user to input any parameters that are accepted by
:class:`textwrap.TextWrapper()`

.. seealso:: :mod:`IPython.utils.text`


In it's current implementation ZimText doesn't do anything and wrap_paragraph
doesn't write the text to a file :/

Just dropped string2lines down there thanks to docutils and the
:mod:`docutils.state_machine`.


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

    Now the publicly available methods from textwrapper.
    """

    def __init__(self,
                 width=80,
                 break_long_words=False,
                 break_on_hyphens=False,
                 **kwargs):
        """Initialize the class."""
        self.width = width
        self.break_long_words = break_long_words
        self.break_on_hyphens = break_on_hyphens
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


def string2lines(astring,
                 tab_width=8,
                 convert_whitespace=False,
                 whitespace=re.compile('[\v\f]')):
    """
    Return a list of one-line strings with tabs expanded, no newlines, and
    trailing whitespace stripped.

    Each tab is expanded with between 1 and `tab_width` spaces, so that the
    next character's index becomes a multiple of `tab_width` (8 by default).

    Parameters:

    - `astring`: a multi-line string.
    - `tab_width`: the number of columns between tab stops.
    - `convert_whitespace`: convert form feeds and vertical tabs to spaces?
    """
    if convert_whitespace:
        astring = whitespace.sub(' ', astring)
    return [s.expandtabs(tab_width).rstrip() for s in astring.splitlines()]


if __name__ == '__main__':
    args = sys.argv[:]
    if len(args) < 2:
        raise RuntimeError("Needs a file to reformat as an argument.")
    else:
        for i in args[1:]:
            if is_file(i):
                wrap_paragraphs(args[1:])
