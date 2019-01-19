<<<<<<< .merge_file_v3ivrB
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://github.com/farisachugthai

All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = 'Faris Chugthai'
__copyright__ = 'Copyright (C) 2018 Faris Chugthai'
__license__ = 'MIT'
__email__ = 'farischugthai@gmail.com'

import socket
import requests


def get_public_ip():
    """
    From Kenneth Reitz
    https://docs.python-guide.org/en/latest/dev/virtualenvs/
    Section: Installing packages for your project
    """
    response = requests.get('https://httpbin.org/ip')
    print('Your IP is {0}'.format(response.json()['origin']))


def get_private_ip():
    pass
    # TODO:    sock = socket.something


def get_hostname():
    sock = socket.gethostname()
    print('Your hostname is: ' + sock)


if '__name__' = '__main__':
    get_public_ip()
    # get_private_ip()
    get_hostname()
||||||| .merge_file_OmvpEA
=======
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Print a user's public IP address and hostname.

.. todo::

    Come up with a fallback if requests isn't installed.
"""
import socket
import sys

try:
    import requests
except ImportError:
    from urllib.request import urlopen  # sigh


def get_public_ip():
    """Fetches the user's public IP address by querying httpbin.org

    :return rt: A formatted message displaying the user's IP address.
    :rtype: str

    From Kenneth Reitz:

        .. _Section: Installing packages for your project: `https://docs.python-guide.org/en/latest/dev/virtualenvs/`
    """
    response = requests.get('https://httpbin.org/ip')
    rt = 'Your IP is {0}'.format(response.json()['origin'])
    return rt


def get_hostname():
    sock = socket.gethostname()
    print('Your hostname is: ' + sock)


if '__name__' == '__main__':
    response = get_public_ip()
    print(response)
    get_hostname()
>>>>>>> .merge_file_YUYO2D
