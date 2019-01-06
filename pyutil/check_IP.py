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
    sys.exit()


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
