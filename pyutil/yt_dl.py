#!/usr/bin/env python
"""Embedding youtube-dl into a script.

.. todo::

    File saved goes %(artist) - %(title) - %(url key)

    and those keys are long random strings which is annoying. How do we
    properly parse the videos title and save the filename?


Jan 25, 2019:

    Not pertinent to this specific module but useful info for debugging.


.. admonition:: Be careful and import necessary modules!

    Things keep breaking because it says Sphinx doesn't recognize youtube_dl
    So do we need to run import statements all along this thing too?


.. ipython::

    In [5]: import youtube_dl
    In [6]: len(dir(youtube_dl.extractor))
    Out[6]: 1944

Jesus Christ that's a lot! Here's some info on the extractors.


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

import sys
import warnings

import youtube_dl


class MyLogger(object):
    """Logs download for script."""

    def debug(self, msg):
        """Detailed info."""
        pass

    def info(self, msg):
        """About a 20/100."""
        pass

    def warning(self, msg):
        """Default log level."""
        pass

    def error(self, msg):
        """More serious errors."""
        print(msg)

    def critical(self, msg):
        """Most serious errors."""
        warnings.showwarning(msg, filename="sys.stderr")


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Wrapper for downloading YouTube videos.')

    parser.add_argument(url_list, type=list, nargs='+', required=True, help="List of urls to download.")

    # todo:: Should a ft argument.

    parser.add_argument('-l', '--log-level', metavar = LOGLEVEL, help="Logging verbosity from 0 to 4.")

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

    if len(sys.argv) < 2:
        parser.print_help()

    url_list = args.url_list

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url_list)

    if LOGLEVEL:  # If the user specifies a log level begin logging.
        logger = MyLogger()
    else:
        logger = ''
