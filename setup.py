#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create an installable package for the utilities repository.

Largely based off of the work done by @kennethreitz in his setup.py repository.

_`Kenneth Reitz setup.py template <https://raw.githubusercontent.com/kennethreitz/setup.py/master/setup.py>`

"""
import codecs
import os
import sys
from shutil import rmtree

from setuptools import setup, find_packages, Command

if sys.version_info[:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")

# Metadata: {{{1

NAME = 'utilities'
AUTHOR = "Faris Chugthai",
EMAIL = "farischugthai@gmail.com",
DESCRIPTION = "Utiities for maintaining platform agnostic workstations.",
LICENSE = "MIT",
KEYWORDS = "linux math science",
URL = "https://github.com/farisachugthai/utilities",
REQUIRES_PYTHON = '>=3.6.0'  # actually could be as bad as 3.7+ only.
VERSION = None

REQUIRED = [
        'pynvim', 'IPython',
        # Project uses reStructuredText, so ensure that the docutils get
        # installed or upgraded on the target machine
        'docutils>=0.3',
        'requests', 'sphinx', 'flake8'
]

EXTRAS = {
}

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    try:
        with open(os.path.join(here, NAME, '__version__.py')) as f:
            exec(f.read(), about)
    except IOError:  # the file doesn't exist
        about['__version__'] = None


# }}}}
class UploadCommand(Command):  # {{{1
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold using ANSI escape sequences."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        """Initialize upload options."""
        pass

    def finalize_options(self):
        """Finalize upload options."""
        pass

    def run(self):
        """Upload package."""
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        # self.status('Uploading the package to PyPI via Twine…')
        # os.system('twine upload dist/*')

        # self.status('Pushing git tags…')
        # os.system('git tag v{0}'.format(about['__version__']))
        # os.system('git push --tags')

        sys.exit()


# }}}
# Where the magic happens: {{{1
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },
    license='MIT',

    #  https://www.python.org/dev/peps/pep-0345/#platform-multiple-use
    # A Platform specification describing an operating system supported by the
    # distribution which is not listed in the "Operating System" Trove
    # classifiers. See "Classifier" below.#
    # Platform='Linux',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
    # project home page, if any
    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # }
    # could also include long_description, download_url, classifiers, etc.
)
