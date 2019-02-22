Tutorial.rst - The pyutils tutorial
===================================

.. module:: tutorial
   :synopsis: The pyutils tutorial

This package combines different scripts that aide in working with computers
ranging from Windows 10 to Linux to Ubuntu to automate regular,
repetitive and error prone tasks.

Installation
-------------

.. code-block:: shell

   python setup.py build
   python setup.py install

Alternatively

.. code-block:: shell

   python setup.py develop

Which is similar to

.. code-block:: shell

   pip wheel -e .

Contributing
------------
This package has recently adopted the :ref:`numpy` convention for docstrings.
As a result, all docstrings must conform to this standard.


A bare template for a full docstring with all :ref:`numpy` subsections has been
included below.

.. include:: numpydoc_docstring.rst

.. jesus i don't know why i struggled with that so much. Refer to
.. http://docutils.sourceforge.net/docs/ref/rst/directives.html#include
