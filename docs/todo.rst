====
TODO
====
Not too dissimilar to the world's worst kanban board, this file is going
to be a manually created index for every **TODO** I write in this repo.

docs
----
It's not much but the docs build. However your readme file still renders as
markdown so you'll probably wanna change the file extension there and rewrite
it.

**02-06-19**

syntax highlighting
^^^^^^^^^^^^^^^^^^^

Just like that they don't. As a mental note when the build works again try this

.. code-block:: python3

   from sphinx.pygments_style import SphinxStyle

   global sph
   sph = SphinxStyle()
   sph.styles

Will print off all the token configs. Figure out how to return the global
instance and then we have a gruvbox pygments file on termux. Override to
your hearts content.

Feb 12, 2019:

Docs are building better. Modules are building well; however the index is still
incredibly wrong. Doesn't list anything at all though it should.1

scripts
---------
- Either add doctests, logging or unittests to `dlink <https://github.com/farisachugthai/utilities/python/dlink.py>`_ that you feel confident enough to begin basing `dot_sym.ipy <https://github.com/farisachugthai/utilities/python/dot_sym.ipy>`_ off of it and then begin basing `newbuntu <https://github.com/farisachugthai/newbuntu>`_ off of that.

- Make a script that deletes empty dirs in ``$PREFIX/tmp`` Termux has 100s now.

- A script that utilizes `dlink <https://github.com/farisachugthai/utilities/python/dlink.py>`_ to update the scripts in `<~/bin>`_. Quite annoying to do this manually.

- Rsync and rclone scripts aren't close to done. Part of that will be encrypting/archiving your notebooks and pulling them down on different devices.

Linting
-------
- Run ``rstcheck`` on all of the rst files in ./docs. If you want to do it from termux you'll need to specify ``rstcheck -j 1`` because :mod:`multiprocessing` doesn't work.

- Also this needs to be able to pass a standard :mod:`flake8` lint.

- Then I want a simple unit test suite created for all publicly exported functions.
  - Not a high bar, but a necessary one.
