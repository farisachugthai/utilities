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
    """Fetch the user's public IP address by querying `<httpbin.org>`__.

    :return rt: A formatted message displaying the user's IP address.
    :rtype: str

    .. see also::

    From Kenneth Reitz, owner of httpbin:

        .. _Section: Installing packages for your project: `https://docs.python-guide.org/en/latest/dev/virtualenvs/`_
    """
    response = requests.get('https://httpbin.org/ip')
    rt = 'Your IP is {0}'.format(response.json()['origin'])
    return rt


def get_hostname():
    """Get the user's hostname."""
    sock = socket.gethostname()
    return ('Your hostname is: ' + sock)


if '__name__' == '__main__':
    response = get_public_ip()
    print(response)
    print(get_hostname())
