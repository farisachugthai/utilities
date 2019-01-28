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

    :return ret: A formatted message displaying the user's IP address.
    :rtype: str

    From Kenneth Reitz:

        .. _Section: Installing packages for your project: `https://docs.python-guide.org/en/latest/dev/virtualenvs/`
    """
    res = requests.get('https://httpbin.org/ip')
    ret = 'Your IP is {0}'.format(res.json()['origin'])
    return ret


def get_hostname():
    sock = socket.gethostname()
    print('Your hostname is: ' + sock)


if '__name__' == '__main__':
    response = get_public_ip()
    print(response)
    get_hostname()
