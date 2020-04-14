==============
Text Utilities
==============

:mod:`json_sorter`
==================

.. automodule:: pyutil.json_sorter
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`~pyutil.wrap`
===================

.. currentmodule:: pyutil.wrap

Wrap text similarly to :func:`textwrap.dedent()` but with multiple paragraphs.

Allow the user to input any parameters that are accepted by
:class:`textwrap.TextWrapper`

.. class:: TextWrap

   Subclass :class:`textwrap.TextWrapper()`.

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

   ``__init__().text`` defaults to None.

   However, it is still a required parameter. It's simply not enforced.
   We're all responsible users here right?

   :param text: A multi-line string.
   :type text: str
   
   .. method:: wrap_paragraphs(text, ncols)

      Wrap multiple paragraphs to fit a specified width.

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



.. seealso::
   :mod:`IPython.utils.text`
