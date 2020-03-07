=================
Remaining Modules
=================

.. contents::
    :local:
    :depth: 2

:mod:`env`
----------

.. automodule:: pyutil.env
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`env_checks`
-----------------

.. currentmodule:: pyutil.env_checks

.. function:: get_username()

   More cross-platform implementation of retrieving a username.

Summary
-------
This function checks the environment variables :envvar:`LOGNAME`,
:envvar:`USER`, :envvar:`LNAME` and :envvar:`USERNAME`, in order, and
returns the value of the first one which is set to a non-empty string.  If
none are set, the login name from the password database is returned on
systems which support the :mod:`pwd` module, otherwise, an exception is
raised.

In general, this function should be preferred over :func:`os.getlogin()`.

.. automodule:: pyutil.env_checks
    :members:
    :undoc-members:
    :show-inheritance:

:mod:`itersrc`
---------------

.. automodule:: pyutil.itersrc
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`ptags`
-------------------

.. automodule:: pyutil.ptags
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`strip_space`
--------------------------

.. automodule:: pyutil.strip_space
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`sys_checks`
-------------------------

.. automodule:: pyutil.sys_checks
    :members:
    :undoc-members:
    :show-inheritance:
