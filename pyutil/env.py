<<<<<<< .merge_file_AwRWlP
#!/usr/bin/env python
# Maintainer: Faris Chugthai
"""Simple module that handles the user's environment variables.

This file can be either executed directly or sourced in a startup file.
"""
import os
import pprint


def to_console():
    """Print env vars to console."""
    pprint.pprint(sorted(os.environ.items()))


def env_ns():
    """Save the env vars for use in a REPL namespace."""
    env = os.environ.copy()
    return env


if __name__ == "__main__":
    to_console()
||||||| .merge_file_IHSLRT
=======
#!/usr/bin/env python
# Maintainer: Faris Chugthai
"""Simple module that pretty prints the user's environment variables.

This is actually implemented as an IPython magic but to make it easier
to use in a typical Python REPL it's also implemented here.

The if name == '__main__' is left off so that it can be run directly
or sourced.
"""
import os
import pprint

pprint.pprint(sorted(os.environ.items()))
>>>>>>> .merge_file_T1C1t5
