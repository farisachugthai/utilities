#!/usr/bin/env python
# Maintainer: Faris Chugthai

import requests
import sys

"""
Usage:
    lazy_downloader url output_filename

Must be plaintext. No MP3s or PDFs.
If filename already exists on the system it will be overwritten.
"""

res = requests.get(sys.argv[1])
res.raise_for_status()

if res.headers['Content-Type']:
    pass
# TODO: figure out how to check that the file is plain text and not hit constant false positives

with open(sys.argv[1], "wt") as f:
    f.write(res.text)

# could add in a check. if the file is over a certain size use res.iter_chunk()
