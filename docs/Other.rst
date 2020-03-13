=================
Remaining Modules
=================

.. contents::
    :local:
    :depth: 2

:mod:`env`
==========

.. automodule:: pyutil.env
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`env_checks`
=================


.. currentmodule:: pyutil.env_checks

.. function:: get_username()

   More cross-platform implementation of retrieving a username.

`env_checks` Summary
--------------------

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
===============

.. automodule:: pyutil.itersrc
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`ptags`
===================

.. automodule:: pyutil.ptags
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`strip_space`
==========================

.. automodule:: pyutil.strip_space
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`sys_checks`
=========================

.. automodule:: pyutil.sys_checks
    :members:
    :undoc-members:
    :show-inheritance:


:mod:`_logging`
===============

Set up general logging parameters and write everything to separate files.

Logger
-------

Set up a more generalized logger. This differs from 05_log.py in that it
should be decoupled from IPython and provide reasonable defaults to fall back
on if it is executed by something other than IPython.

This will occur as the directory in which the :class:`logging.Logger` is
determined in either a module function or a class method.

Formatter
----------

From :class:`logging.Formatter`:

Formatter instances are used to convert a `logging.LogRecord` to text.

Formatters need to know how a LogRecord is constructed. They are
responsible for converting a LogRecord to (usually) a string which can
be interpreted by either a human or an external system. The base Formatter
allows a formatting string to be specified. If none is supplied, the
the style-dependent default value, "%(message)s", "{message}", or
"${message}", is used.

The Formatter can be initialized with a format string which makes use of
knowledge of the LogRecord attributes - e.g. the default value mentioned
above makes use of the fact that the user's message and arguments are pre-
formatted into a LogRecord's message attribute. Currently, the useful
attributes in a LogRecord are described by:

   %(name)s            Name of the logger (logging channel)
   %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                       WARNING, ERROR, CRITICAL)
   %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                       "WARNING", "ERROR", "CRITICAL")
   %(pathname)s        Full pathname of the source file where the logging
                       call was issued (if available)
   %(filename)s        Filename portion of pathname
   %(module)s          Module (name portion of filename)
   %(lineno)d          Source line number where the logging call was issued
                       (if available)
   %(funcName)s        Function name
   %(created)f         Time when the LogRecord was created (time.time()
                       return value)
   %(asctime)s         Textual time when the LogRecord was created
   %(msecs)d           Millisecond portion of the creation time
   %(relativeCreated)d Time in milliseconds when the LogRecord was created,
                       relative to the time the logging module was loaded
                       (typically at application startup time)
   %(thread)d          Thread ID (if available)
   %(threadName)s      Thread name (if available)
   %(process)d         Process ID (if available)
   %(message)s         The result of record.getMessage(), computed just as
                       the record is emitted

.. automodule:: pyutil._logging
    :members:
    :undoc-members:
    :show-inheritance:
