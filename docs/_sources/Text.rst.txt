==============
Text Utilities
==============

:mod:`json_sorter`
==================

.. module:: json_sorter
    :synopsis: Sort a JSON file by key without losing organization for nested elements.

Take a :mod:`json` file, sort the keys and insert 4 spaces for indents.

One Line Solution
-----------------

>>> sorted((json.loads(open('settings.json').read()).items()), key=operator.getitemattr)

You definitely shouldn't implement it as a one liner, *as you can clearly see,*;
however 5 functions and a handful of instantiated classes and debugging, and
we're somehow barely closer to done.

The functions for reading and writing files could be refactored and used over the
entire package.

The logger **should** be set up that way.

This code is going to easily clear 100 lines when a JSON encoded object shouldn't
take more than a few lines to de-serialize and work with.

This'll serve as a good template for testing out tools to build a simple
script with.

The problem is already solved. Let's see what we can't squeeze out of our tools
along the way.

Interestingly enough, this display of excessiveness started as a simple
quick fix.

Originally, this module was used to fix my `<../.vscode/settings.json>`_ from VSCode.

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

      :param text: text to wrap using :mod:`re` and :func:`textwrap.dedent()`
      :type text: str
      :param ncols: column to wrap text at
      :type ncols: int
      :returns wrapped_text: list of complete paragraphs, wrapped to fill `ncols` columns.
      :rtype: list of str


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


