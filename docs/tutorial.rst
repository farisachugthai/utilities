.. _tutorial:

Tutorial.rst
==============


.. module:: tutorial
   :synopsis: The pyutils tutorial

This package combines different scripts that aide in working with computers
ranging from Windows 10 to Linux to Ubuntu to automate regular,
repetitive and error prone tasks.

.. _tutorial-installation:

Installation
-------------

.. code-block:: shell

   python setup.py build
   python setup.py install


Alternatively, one can run the setup script in develop mode.

.. code-block:: shell

   python setup.py develop


Which is similar to

.. code-block:: shell

   pip wheel -e .


.. _tutorial-contributing:

Contributing
------------

This package has recently adopted the :mod:`numpy` convention for docstrings.
As a result, all docstrings must conform to this standard.


A bare template for a full docstring with all :mod:`numpy` subsections has been
included below.

.. include:: numpydoc_docstring.rst

.. jesus i don't know why i struggled with that so much. Refer to

.. http://docutils.sourceforge.net/docs/ref/rst/directives.html#include
