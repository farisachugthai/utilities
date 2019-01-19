#!/usr/bin/env python
"""Embedding youtube-dl.

Dec 24, 2018: Back after an extended hiatus from this script.

.. todo::

    File saved goes %(artist) - %(title) - %(url key)

    and those keys are long random strings which is annoying. How do we
    properly parse the videos title and save the filename?

"""
from __future__ import unicode_literals

from sys import argv

import youtube_dl


class MyLogger(object):

    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Wrapper for downloading YouTube videos.')

    parser.add_argument('-u', '--url_list', nargs='+', required=True, type=str)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
           }],
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

    args = parser.parse_args()

    if len(argv[:]) == 1:
        parser.print_help()

    url_list = args.url_list

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url_list)
