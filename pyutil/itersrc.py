<<<<<<< .merge_file_vdWUlZ
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys


def iter_source_code(paths):
    """Iterate over all Python source files in C{paths}.

    Taken with almost no modifications from pyflakes.
    This would be a great function to call with os.listdir('root') output.

    :param paths: A list of paths.  Directories will be recursed into and
                  any .py files found will be yielded.  Any non-directories
                  will be yielded as-is.
    """
    for path in paths:
        if os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    full_path = os.path.join(dirpath, filename)
                    yield full_path
        else:
            yield path


if __name__ == "__main__":
    paths = sys.argv[:]
    iter_source_code(paths)
||||||| .merge_file_MqTVg0
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys


def iter_source_code(paths):
    """Iterate over all Python source files in C{paths}.

    Taken with almost no modifications from pyflakes.
    This would be a great function to call with os.listdir('root') output.

    @param paths: A list of paths.  Directories will be recursed into and
        any .py files found will be yielded.  Any non-directories will be
        yielded as-is.

        :param paths:
    """
    for path in paths:
        if os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(path):
                for filename in filenames:
                    full_path = os.path.join(dirpath, filename)
                    yield full_path
        else:
            yield path


if __name__ == "__main__":
    paths = sys.argv[:]
    iter_source_code(paths)
>>>>>>> .merge_file_9uMkkL
