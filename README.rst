.. _readme:

utilities
==========

.. currentmodule:: readme

.. title:: utilities

This repository houses a number of functional scripts I utilize to
administer multiple workstations.


.. contents: Table of Contents


Installation
------------
One can install the package by:

* Cloning with git
* Running the `setup.py`_ file.
* Ensuring that the scripts in ./sh/ are in ``$PATH``

If you are on a Unix-like system, the following will ensure everything
below pyutil/ is in your PATH.


.. code-block:: bash

   git clone https://github.com/farisachugthai/utilities
   cd utilities

   python3 setup.py build && python3 setup.py install

   # The script at ./pyutil/dlink.py is useful for creating symlinks for every
   # file in a directory. If the directory ~/bin is in your path...

   # Check which directories are in the $PATH env var
   echo $PATH

   # Then link the scripts in ./sh to a directory in your path!
   python3 pyutil/dlink.py "$PWD/sh" ~/bin

For anyone using Windows 10, the Powershell installation will be slightly
different; however, not tremendously.

.. code-block:: ps1

   git clone https://github.com/farisachugthai/utilities
   # cd is aliased to Set-Location for most instances of Powershell; however in
   # the interest of using domain specific built-ins:
   Set-Location utilities
   python3 setup.py build && python3 setup.py install

   # To view the environment variable path, run:
   Get-Childitem -path env:Path
   # Then ensure that the directory you pick is in your path, and run
   python3 pyutil\dlink.py "$PWD\sh" C:\Users\path\to\directory

.. Building From Source
.. ---------------------

.. The documentation can be built as well. Commented out until the docs build more smoothly

Usage
------
Modules can be used to:

- `Back up directories.`_

- `Automate the process of downloading plain-text files from the Internet.`_

- `Automate downloading videos from YouTube.`_

- `Symlink files recursively`_

- `Inspect varying python modules.`_

- `Introspect environment variables.`_

- `Profiling nvim startup time.`_

- `Strip trailing whitespace from a file.`_


License
---------
MIT

Contributing
--------------
Even though these are mostly scripts I've thrown together; I'd absolutely love
any constructive criticism or pointers on how to get any module listed to work
better!

I hope it goes without saying, but if it doesn't, please don't hesitate
to fork or create an issue.

.. _`Back up directories.`: docs/api/pyutil/backup_nt_and_posix
.. _`Automate the process of downloading plain-text files from the Internet.`: pyutil/lazy_downloader.py
.. _`Automate downloading videos from YouTube.`: pyutil/yt_dl.py
.. _`Symlink files recursively`: pyutil/linktree.py
.. _`Inspect varying python modules.`: pyutil/inspect_module.py
.. _`Introspect environment variables.`: pyutil/env.py
.. _`Profiling nvim startup time.`: pyutil/nvim_profiling.py
.. _`Strip trailing whitespace from a file.`: pyutil/strip_space.py
.. _`setup.py`: setup.py
