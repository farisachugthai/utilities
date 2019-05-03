#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Configure module wide logging."""
import logging
from collections import deque


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
FMT_NORMAL = logging.Formatter(fmt='%(asctime)s %(levelname).4s %(message)s',
                               datefmt='%H:%M:%S')
FMT_DEBUG = logging.Formatter(
    fmt='%(asctime)s.%(msecs)03d %(levelname).4s [%(name)s] %(message)s',
    datefmt='%H:%M:%S')


def setup_logging(debug=True, logfile=None, name='__name__'):
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
