#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Print a user's public IP address and hostname.

.. rubric:: Requires


:mod:`requests`


See Also
--------
From Kenneth Reitz, owner of `httpbin`_.

.. _`httpbin`: https://httpbin.org/ip

Installing packages for your project:

`<https://docs.python-guide.org/en/latest/dev/virtualenvs/>`_

"""
import logging
import socket

import requests

logger = logging.getLogger(__name__)


def get_public_ip():
    """Fetch the user's public IP address by querying `<httpbin.org>`_.

    Returns
    -------
    rt : str
        A :mod:`json` formatted message displaying the user's IP address.


    """
    response = requests.get('https://httpbin.org/ip')
    response.raise_for_status()

    logging.debug("Response object was:")
    logging.debug(response.json())
    logging.debug("response.json()['origin'] was:")
    logging.debug(response.json()['origin'])
    rt = 'Your IP is {0}'.format(response.json()['origin'])
    return rt


def get_hostname():
    """Get the user's hostname.

    Returns
    -------
    host_return_msg : str
        A formatted message displaying the user's IP address.

    Examples
    --------
    .. ipython::

        In [13]: from check_IP import get_hostname
        In [14]: h = get_hostname()
        Out[14]: 'Your hostname is: localhost'
        In [15]: h
        Out[15]: 'Your hostname is: localhost'

    Cross your fingers!

    """
    sock = socket.gethostname()
    host_return_msg = 'Your hostname is: ' + sock
    return host_return_msg


if '__name__' == '__main__':
    ip_ret_val = get_public_ip()
    print(ip_ret_val)

    user_hostname = get_hostname()
    print(user_hostname)
