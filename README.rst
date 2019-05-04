.. _root-readme:

======
pyutil
======

.. currentmodule:: readme

.. title:: utilities

.. highlight:: sh

This repository houses a number of functional scripts I utilize to
administer multiple workstations.


.. contents: Table of Contents
    :local:
    :backlinks: "entry"


.. _root-installation:

Installation
------------
Python offers it's users a large number of ways to install new packages.

One can install the python modules by:

* Installing with pip

  Install from newest dev version in master branch

.. code-block:: sh

    pip install git+https://github.com/farisachugthai/utilities

* Cloning with git and installing with pip

.. code-block:: sh

    git clone git+https://github.com/farisachugthai/utilities
    pip install .

* As an alternative to a pip install, obtain the source code and run the `setup.py`_ file.

If you are on a Unix-like system, the following will ensure everything
below pyutil/ is in your PATH and give you the ability to modify the source
code in place.


.. code-block:: sh

    git clone https://github.com/farisachugthai/utilities
    cd utilities

    python3 setup.py build && python3 -m pip install -U -e .

* After which point, the only necessary step will be ensuring that the scripts in sh/ are in ``$PATH``.

.. code-block:: sh

    # The script at pyutil/dlink.py is useful for creating symlinks for every
    # file in a directory. If the directory ~/bin is in your path...

    # Check which directories are in the ``$PATH`` env var
    echo $PATH

    # Then link the scripts in sh/ to a directory in your path!
    python3 pyutil/dlink.py "$PWD/sh" ~/bin

For anyone using Windows 10, the Powershell installation will be slightly
different; however, not tremendously.

.. code-block:: console

    git clone https://github.com/farisachugthai/utilities

    # `cd` is aliased to set-location for most instances of powershell;
    # however in the interest of using domain specific built-ins:
    set-location utilities

    python3 setup.py bdist_wheel && python3 -m pip install -I -e .

    # to view the environment variable path, run:
    get-childitem -path env:path

    # then ensure that the directory you pick is in your path, and run
    python3 pyutil\dlink.py "$pwd\sh" C:\users\path\to\directory


.. _root-docs:

Building Documentation From Source
----------------------------------
The documentation can be read online at `GitHub Pages <https://farisachugthai.github.io/utilities>`_

However, the documentation can be built locally as well.

After following the installation instructions at `root-installation`_, one can run

.. code-block:: shell

   cd doc
   make html

Then, direct your browser to ``_build/html/index.html``.

To do so in a more direct manner, a *htmlview* target has been created as a
convenience in the docs/Makefile.

This target will build the documentation and open up your default web browser
automatically.

Testing
-------
To run the tests with the interpreter available as ``python``, use

.. code-block:: sh

    make test

If you want to explicitly define which interpreter, e.g. ``python3``, use

.. code-block:: sh

    PYTHON=python3 make test

License
-------
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
