#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Wrap text similarly to :func:`textwrap.dedent()` but with multiple paragraphs.

Allow the user to input any parameters that are accepted by
:class:`textwrap.TextWrapper()`

.. seealso:: :mod:`IPython.utils.text`



TextWrapper
-----------

Help on class TextWrapper in textwrap:

textwrap.TextWrapper = class TextWrapper(builtins.object)
 | textwrap.TextWrapper(width=70, initial_indent='', subsequent_indent='',
 | expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False,
 | break_long_words=True, drop_whitespace=True, break_on_hyphens=True,
 | tabsize=8, *, max_lines=None, placeholder=' [...]')
 |
 |  Object for wrapping/filling text.  The public interface consists of
 |  the wrap() and fill() methods; the other methods are just there for
 |  subclasses to override in order to tweak the default behaviour.
 |  If you want to completely replace the main wrapping algorithm,
 |  you'll probably have to override _wrap_chunks().
 |
 |  Several instance attributes control various aspects of wrapping:
 |    width (default: 70)
 |      the maximum width of wrapped lines (unless break_long_words
 |      is false)
 |    initial_indent (default: "")
 |      string that will be prepended to the first line of wrapped
 |      output.  Counts towards the line's width.
 |    subsequent_indent (default: "")
 |      string that will be prepended to all lines save the first
 |      of wrapped output; also counts towards each line's width.
 |    expand_tabs (default: true)
 |      Expand tabs in input text to spaces before further processing.
 |      Each tab will become 0 .. 'tabsize' spaces, depending on its position
 |      in its line.  If false, each tab is treated as a single character.
 |    tabsize (default: 8)
 |      Expand tabs in input text to 0 .. 'tabsize' spaces, unless
 |      'expand_tabs' is false.
 |    replace_whitespace (default: true)
 |      Replace all whitespace characters in the input text by spaces
 |      after tab expansion.  Note that if expand_tabs is false and
 |      replace_whitespace is true, every tab will be converted to a
 |      single space!
 |    fix_sentence_endings (default: false)
 |      Ensure that sentence-ending punctuation is always followed
 |      by two spaces.  Off by default because the algorithm is
 |      (unavoidably) imperfect.
 |    break_long_words (default: true)
 |      Break words longer than 'width'.  If false, those words will not
 |      be broken, and some lines might be longer than 'width'.
 |    break_on_hyphens (default: true)
 |      Allow breaking hyphenated words. If true, wrapping will occur
 |      preferably on whitespaces and right after hyphens part of
 |      compound words.
 |    drop_whitespace (default: true)
 |      Drop leading and trailing whitespace from lines.
 |    max_lines (default: None)
 |      Truncate wrapped lines.
 |    placeholder (default: ' [...]')
 |      Append to the last line of truncated text.
 |
 |  Methods defined here:
 |
 |  __init__(self, width=70, initial_indent='', subsequent_indent='',
 | expand_tabs=True, replace_whitespace=True, fix_sentence_endings=False,
 | break_long_words=True, drop_whitespace=True, break_on_hyphens=True,
 | tabsize=8, *, max_lines=None, placeholder=' [...]')
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  fill(self, text)
 |      fill(text : string) -> string
 |
 |      Reformat the single paragraph in 'text' to fit in lines of no
 |      more than 'self.width' columns, and return a new string
 |      containing the entire wrapped paragraph.
 |
 |  wrap(self, text)
 |      wrap(text : string) -> [string]
 |
 |      Reformat the single paragraph in 'text' so it fits in lines of
 |      no more than 'self.width' columns, and return a list of wrapped
 |      lines.  Tabs in 'text' are expanded with string.expandtabs(),
 |      and all other whitespace characters (including newline) are
 |      converted to space.
 |

"""
import re
import sys
from textwrap import dedent, fill, TextWrapper

try:
    from prompt_toolkit import print_formatted_text as print
except ImportError:
    pass


class ZimText(TextWrapper):
    """Subclass :class:`textwrap.TextWrapper()`."""

    def __init__(self, **kwargs):
        """Initialize the class."""
        self.width = 80
        self.break_long_words = False
        self.break_long_words_hyphens = False
        # kwargs = {}
        # kwargs = **kwargs
        super().__init__(**kwargs)

    @property
    def body(self, text):
        """No idea if I'm doing this right."""
        print(text)
        return (text)


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
        sys.exit('Requires a file to re-format.')
    else:
        sys.exit(wrap_paragraphs(args[1:]))

    # it might be easier to do the above.
    # can't do it like the below because then we have to hardcode the value of
    # ncols so we could force some kw args for the script but it's then easier
    # for the user to import the function and use it themselves.

    # if len(args) > 2:
    # for i in args[1:]:
    # wrap_paragraphs(i, 80)
