#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Wrap text similarly to :func:`textwrap.dedent()` but with multiple paragraphs.

Allow the user to input any parameters that are accepted by
:class:`textwrap.TextWrapper()`

Utilizes :mod:`prompt_toolkit.print_formatted_text` to easily display
prettified text.


.. seealso:: :mod:`IPython.utils.text`

Just dropped string2lines down there thanks to docutils and the
:mod:`docutils.state_machine`.

"""
import re
import sys
from textwrap import dedent, TextWrapper

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

    Now the publicly available methods from :class:`~textwrap.TextWrapper`.::

        >>> from textwrap import TextWrapper
        >>> dir(TextWrapper)
        ['_fix_sentence_endings',
        '_handle_long_word',
        '_munge_whitespace',
        '_split',
        '_split_chunks',
        '_wrap_chunks',
        'fill',
        'sentence_end_re',
        'unicode_whitespace_trans',
        'uspace',
        'wordsep_re',
        'wordsep_simple_re',
        'wrap',
        'x']

    """

    def __init__(self,
                 text=None,
                 width=80,
                 break_long_words=False,
                 break_on_hyphens=False,
                 **kwargs):
        """Initialize the class. ``__init__().text`` defaults to None.

        However, it is still a required parameter. It's simply not enforced.

        We're all responsible users here right?

        """
        self.width = width
        self.break_long_words = break_long_words
        self.break_on_hyphens = break_on_hyphens
        super().__init__(**kwargs)

    def wrap_paragraphs(self):
        """Wrap multiple paragraphs to fit a specified width.

        This is equivalent to :func:`textwrap.wrap()`, but with support for multiple
        paragraphs, as separated by empty lines.

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

        Examples
        --------
        >>> from wrap import ZimText
        >>> wrapper = ZimText()
        >>> f = open('unix-ide-editing.txt')
        >>> text = f.read()
        >>> wrapped = wrapper.wrap(text)
        >>> with open('unix-ide-editing.txt', 'wt') as f:
        ...     f.write(text)


        """
        paragraph_re = re.compile(r'\n(\s*\n)+', re.MULTILINE)
        self.text = dedent(self.text).strip()
        paragraphs = paragraph_re.split(
            self.text)[::2]  # every other entry is space
        wrapped_text = []
        indent_re = re.compile(r'\n\s+', re.MULTILINE)
        for p in paragraphs:
            # presume indentation that survives dedent is meaningful formatting,
            # so don't fill unless text is flush.
            if indent_re.search(p) is None:
                # wrap paragraph
                p = self.fill(p)
            wrapped_text.append(p)
        return wrapped_text

    def string2lines(self, convert_whitespace=True):
        """

        Parameters:
        -----------
        text : str
            A multi-line string.
        convert_whitespace : bool
            convert form feeds and vertical tabs to spaces

        Returns
        -------
        list of str
            Return a list of one-line strings with tabs expanded, no newlines, and
            trailing whitespace stripped.

        """
        if convert_whitespace:
            self.text = self._munge_whitespace(self.text)
        new_text = [s for s in self.text.splitlines()]
        return new_text


if __name__ == '__main__':
    args = sys.argv[:]
    if len(args) < 2:
        raise RuntimeError("Needs a file to reformat as an argument.")
    else:
        for i in args[1:]:
            if is_file(i):
                print("Rewrapping " + i)
                wrapper = ZimText()
                wrapper.wrap_paragraphs(args[1:])
