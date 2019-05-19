#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Set up general logging parameters and write everything to separate files.

Logger
=======
Set up a more generalized logger. This differs from 05_log.py in that it
should be decoupled from IPython and provide reasonable defaults to fall back
on if it is executed by something other than IPython.

This will occur as the directory in which the :class:`logging.Logger()` is
determined in either a module function or a class method.

Formatter
----------

From :class:`logging.Formatter()`:

    Formatter instances are used to convert a LogRecord to text.

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

"""
from collections import deque
import logging
from pathlib import Path
import time


class QueueHandler(logging.Handler):
    """This handler store logs events into a queue."""

    def __init__(self, queue):
        """Initialize an instance, using the passed queue."""
        self.queue = queue
        super().__init__()

    def enqueue(self, record):
        """Enqueue a log record."""
        self.queue.append(record)

    def emit(self, record):
        self.enqueue(self.format(record))


QUEUE = deque(maxlen=1000)
FMT_NORMAL = logging.Formatter(
    fmt='%(asctime)s %(levelname).4s %(message)s', datefmt='%H:%M:%S')
FMT_DEBUG = logging.Formatter(
    fmt='%(asctime)s.%(msecs)03d %(levelname).4s [%(name)s] %(message)s',
    datefmt='%H:%M:%S')


def queued_logging(debug=True, logfile=None, name='__name__'):
    """
    All the produced logs using the standard logging function
    will be collected in a queue by the `queue_handler` as well
    as outputted on the standard error `stderr_handler`.

    The verbosity and the format of the log message is
    controlled by the `debug` parameter

    - debug=False:
           a concise log format will be used, debug messsages will be discarded
           and only important message will be passed to the `stderr_handler`

    - debug=True:
           an extended log format will be used, all messages will be processed
           by both the handlers

    Parameters
    ----------
    debug : Bool
        Set the logger to :obj:`logging.DEBUG`.
    logfile : str, optional
        Path-like object
    name : :class:`~logging.Logger()` name, optional
        Optional but better to set a more tailored logger than the root logger.

    """
    mod_logger = logging.getLogger(name=name)

    if debug:
        log_level = logging.DEBUG
        formatter = FMT_DEBUG
    else:
        log_level = logging.WARNING
        formatter = FMT_NORMAL

    handlers = []
    handlers.append(QueueHandler(QUEUE))

    # In it's current implementation logfile=None and if it isn't specified there's no else...?
    # So shouldn't it just not do anything at all?
    if logfile:
        if logfile == '-':
            handlers.append(logging.StreamHandler())
        else:
            handlers.append(logging.FileHandler(logfile))

    for handler in handlers:
        handler.setLevel(log_level)
        handler.setFormatter(formatter)
        mod_logger.addHandler(handler)

    return mod_logger


def setup_ipython_logger():
    """Plug and play logging. No params so you can import and forget.

    Uses the default ``datefmt`` that comes with :class:`~logging.Formatter`
    classes. For example::

        >>> default_time_format = '%Y-%m-%d %H:%M:%S'

    Can be found under the ``__init__()`` method of the logging
    :class:`~logging.Formatter`.

    """
    from IPython.paths import locate_profile
    ipython_profile = Path(locate_profile())
    log_title = '_log-' + time.strftime('%Y-%m-%d')

    log_name = ipython_profile.joinpath('log', '_log-' + log_title + '.log')
    logger = logging.getLogger(name=log_title)
    logger.setLevel(logging.WARNING)

    file_handler = logging.FileHandler(log_name, encoding='utf-8')
    formatter = logging.Formatter(
        '%(asctime)s : %(levelname)s : %(module)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


def _set_debugging():
    """Enable debug logging. From rclone.py"""
    root = logging.getLogger(name=__name__)
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)
