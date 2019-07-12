========
todo
========

The list of todos.

scripts
---------

- Either add doctests, logging or unittests to `dlink <https://github.com/farisachugthai/utilities/python/dlink.py>`_
- Continue adding these support structures until  you feel confident enough to begin basing
  `dot_sym.ipy <https://github.com/farisachugthai/utilities/python/dot_sym.ipy>`_ off of it
- At some point we can then begin basing `newbuntu <https://github.com/farisachugthai/newbuntu>`_
  off of that.
- A script that utilizes `dlink <https://github.com/farisachugthai/utilities/python/dlink.py>`_
  to update the scripts in `<~/bin>`_. Quite annoying to do this manually.
- Rsync and rclone scripts aren't close to done. Part of that will be
  encrypting/archiving your notebooks and pulling them down on different devices.

Linting
-------

- Run :mod:`rstcheck` on all of the rst files in `<./docs>`_. If you want to do it
  from Termux you'll need to specify ``rstcheck -j 1`` because :mod:`multiprocessing` doesn't work.
- Also this needs to be able to pass a standard :mod:`flake8` lint.
