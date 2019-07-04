import shutil
import subprocess
import unittest

from pyutil.shell import BaseCommand


class TestBaseCommand(unittest.TestCase):

    def test_run_one_command_no_options(self):
        """Hopefully this method name will inspire what other methosd you can write."""
        b = BaseCommand(['ctags'])

        # Assert that the cmd length is greater than 0
        self.assertGreater(len(b.cmd), 0)

        if shutil.which('ctags'):
            output = b.run()
            self.assertIsInstance(output, subprocess.CompletedProcess)
        # else:
            # what is the unittest.SkipTest method?


if __name__ == '__main__':
    unittest.main()
