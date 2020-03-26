==================
Filesystem Scripts
==================

:mod:`batch_renamer`
--------------------

.. automodule:: pyutil.batch_renamer
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`dir_cleaner`
------------------

.. automodule:: pyutil.dir_cleaner
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`dlink`
------------

.. automodule:: pyutil.dlink
    :members:
    :undoc-members:
    :show-inheritance:



Directory Linker Rewrite
-------------------------

.. currentmodule:: pyutil.dlink2

This is a rewrite of a script I've had for years, so I decided to go above
and beyond.

The idea behind it was to create something that would easily allow for
creating arbitrarily nested trees of symlinks.

.. todo:: Sep 17, 2019: Recursive option

    Currently doesnt work.

.. todo::
    Logging doesnt log the right files.


`dlink2` Summary
-----------------

Generate symlinks to every file in the directory 'destination_dir'.

The module doesn't immediately check for correct permissions or
operating system.

As a result, the onus is put on the user to ensure that the necessary
requirements per OS are met.

Namely on Windows 10, that if symlinks are allowed on the filesystem,
whether they can only be created by an administrator. Recent enough
versions of Windows 10 have introduced the ability for regular users
to create symlinks as well as admins.

.. automodule:: pyutil.dlink2
    :synopsis: Utilize argparse, pathlib and IPython to generate symlinks.
    :members:
    :undoc-members:
    :show-inheritance:

