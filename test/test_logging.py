#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Unittest the logging in this package.

It'll probably be a good idea to check out
:func:`unittest.TestCase().assertlog()`

Idk if that's the actual call but it'll probably be useful.

 assertLogs(self, logger=None, level=None)                                      |      
 Fail unless a log message of level *level* or higher is emitted            |      on *
 logger_name* or its children.  If omitted, *level* defaults to         |      INFO 
 and *logger* defaults to the root logger.
       |

|      This method must be used as a context manager, and will yield       |      a recording object with two attributes: `output` and `records`.
       |      At the end of the context manager, the `output` attribute will             |      be a list of the matching formatted log messages and the
       |      `records` attribute will be a list of the corresponding LogRecord
       |      objects.
       |                                                                                 |      
Example::
       |
with self.assertLogs('foo', level='INFO') as cm:

 logging.getLogger('foo').info('first message')  
 |             
 logging.getLogger('foo.bar').error('second message')

|       
self.assertEqual(cm.output, ['INFO:foo:first message',                 
|
'ERROR:foo.bar:second message']) 
|

"""
import logging
import unittest

from pyutil._logging import _set_debugging


class TestLogging(unittest.TestCase):

    def test_set_debugging(self):
        LOGGER = _set_debugging()
        self.assertIsInstance(LOGGER, logging.Logger)


if __name__ == "__main__":
    unittest.main()
