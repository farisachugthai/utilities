import logging
import unittest

from pyutil._logging import _set_debugging


class TestLogging(unittest.TestCase):

    def test_set_debugging(self):
        LOGGER = _set_debugging()
        self.assertIsInstance(LOGGER, logging.Logger)


if __name__ == "__main__":
    unittest.main()
