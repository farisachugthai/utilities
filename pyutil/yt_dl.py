#!/usr/bin/env python
"""Embedding youtube-dl.

Dec 24, 2018: Back after an extended hiatus from this script.

.. todo::

    Open up thr API a lot. Reduce instances of hard coded values.
    Expand to playlists.
    Get everything tested.
"""
from __future__ import unicode_literals

import os
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

    parser = ArgumentParser(
        description='Wrapper for downloading YouTube videos.')

    general = parser.add_argument_group()

    general.add_argument('-u', '--url_list', nargs='+', required=True, type=str)

    mp3dir = os.path.join(
        os.path.expanduser('~'), '', 'storage', '', 'music', '')

    general.add_argument(
        '-o',
        '--output',
        default=os.path.join(mp3dir, '', '%(title)s-%(artist)s.%(ext)s'))

    postproc = parser.add_argument_group()

    postproc.add_option(
                    '-k', '--keep-video',
                            action='store_true', dest='keepvideo', default=False,
                                    help='Keep the video file on disk after the post-processing; the video is erased
                                    by defa

    ydl_opts = {
        'format':
        'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger':
        MyLogger(),
        'progress_hooks': [my_hook],
    }

    args = parser.parse_args()

    if len(argv[:]) == 1:
        parser.print_help()

    url_list = args.url_list

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url_list)
