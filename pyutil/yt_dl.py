#!/usr/bin/env python
"""Embedding youtube-dl into a script.

Dec 24, 2018: Back after an extended hiatus from working on this.

Jan 25, 2019:

    Not pertinent to this specific module but useful background info for
    debugging.

.. ipython::

    In [6]: len(dir(youtube_dl.extractor))
    Out[6]: 1944

    Jesus Christ that's a lot!
    Here's some info on the extractors.abs

.. ipython::

    In [8]: youtube_dl.extractor.AdultSwimIE?
    Init signature: youtube_dl.extractor.AdultSwimIE(downloader=None)
    Docstring:
    Information Extractor class.

    Information extractors are the classes that, given a URL, extract
    information about the video (or videos) the URL refers to. This
    information includes the real video URL, the video title, author and
    others. The information is stored in a dictionary which is then
    passed to the YoutubeDL. The YoutubeDL processes this
    information possibly downloading the video to the file system, among
    other possible outcomes.

    The type field determines the type of the result.
    By far the most common value (and the default if _type is missing) is
    "video", which indicates a single video.

    For a video, the dictionaries must include the following fields:

    id:             Video identifier.
    title:          Video title, unescaped.
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
