#!/usr/bin/env python
# Maintainer: Faris Chugthai

import requests
import sys

"""
Literally just throwing this together stream of consciousness.
Usage:
    lazy_downloader url output_filename

Must be plaintext. No MP3s or PDFs.
If filename already exists on the system it will be overwritten.
"""
# TODO: Dude just use Send2Trash instead of destroying their file.

res = requests.get(sys.argv[1])
res.raise_for_status()

with open(sys.argv[2], "wt") as f:
    f.write(res.text)

# could add in a check. if the file is over a certain size use res.iter_chunk()
