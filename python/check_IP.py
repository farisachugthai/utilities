#!/usr/bin/env python
# from kenneth reitz
# http://docs.python-guide.org/en/latest/dev/virtualenvs/
# Section: Installing packages for your project
import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
