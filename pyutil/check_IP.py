#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Print a user's public IP address and hostname.

Requires
--------
:mod:`requests`


See Also
--------
From Kenneth Reitz, owner of httpbin.

Installing packages for your project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`<https://docs.python-guide.org/en/latest/dev/virtualenvs/>`_


.. todo:: Come up with a fallback if requests isn't installed.


"""
import socket
import sys


def get_public_ip():
    """Fetch the user's public IP address by querying `<httpbin.org>`__.

    Returns
    -------
    rt : str
        A formatted message displaying the user's IP address.


    """
    response = requests.get('https://httpbin.org/ip')
    rt = 'Your IP is {0}'.format(response.json()['origin'])
    return rt


def get_hostname():
    """Get the user's hostname."""
    sock = socket.gethostname()
    return 'Your hostname is: ' + sock


if '__name__' == '__main__':
    try:
        import requests
    except ImportError:
        sys.exit()

    response = get_public_ip()
    print(response)
    print(get_hostname())
