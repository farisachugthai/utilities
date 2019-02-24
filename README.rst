.. _readme:

utilities
===========

.. currentmodule:: readme

This repository houses a number of functional scripts I utilize to
administer multiple workstations.

.. contents: Table of Contents


Installation
------------
One can install the package by:

* Cloning with git
* Running the setup.py file.
* Ensuring that the scripts in ./sh/ are in ``$PATH``

If you are on a Unix-like system, the following should work perfectly then.


.. code-block:: bash

   git clone https://github.com/farisachugthai/utilities
   cd utilities

   # The command below will ensure everything below pyutil/ is in your PATH
   python3 setup.py build && python3 setup.py install

   # The script at ./pyutil/dlink.py is useful for creating symlinks for every
   # file in a directory. If the directory ~/bin is in your path...

   # Check which directories are in the $PATH env var
   echo $PATH

   # Then link the scripts in ./sh to a directory in your path!
   python3 pyutil/dlink.py "$PWD/sh" ~/bin


For anyone using Windows 10, the Powershell installation will be slightly
different; however, not tremendously.

.. code-block:: powershell

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
