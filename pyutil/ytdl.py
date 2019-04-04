#!/usr/bin/env python3
# Maintainer: Faris Chugthai
r"""Download a video from YouTube using :mod:`youtube_dl`.

Dec 22, 2018:

    .. note::

        If you initialize with no args, then use :meth:`extract_info` with
        the URL as an arg, you get to see everything you'd need to know
        about the metadata in all the varying formats you'd want use.

This script should be called from the shell as so

.. code-block:: shell

        python ytdl.py $*

where the ``$*`` idiom can be replaced with either URLs of individual videos,
a link to a playlist, or a file containing URLs.


.. todo::

    1. Assume that the :mod:`youtube_dl` script functions.
    2. Then double check we weren't given a file ytdl knows how to handle.
    3. If we were, then scrape with bs4.
        - Possibly extend to writing prettified json (as in json.dumps("",tab=2)) to a file.
    4. Need to add support using :mod:`argparse` because this is gonna get out of hand quickly.
    5. Handle playlists.


**We got it!**
So I was reading the src and realized that almost all of the execution
happens in the :mod:`youtube_dl.__init__`_ file!!

Actually just reading any of the source is useful. :mod:`youtube_dl.options` is
also useful.


"""
import logging
import sys

try:
    import requests
except ImportError:
    logging.warning(
        "This script depends on the requests module. Falling back to urllib.")
    import urllib
else:
    REQUESTS = 1
    logging.debug("Requests was imported.")

import youtube_dl

# parseOpts should actually return this!
# from env_checks import check_xdg_config_home

LOGGER = logging.basicConfig(level=logging.WARNING)


class TermuxDL(youtube_dl.YoutubeDL, **kwargs):
    r"""Subclass :class:`youtube_dl.YoutubeDL` and see if it's easier.

    Also here's all the source code in case you think you need it.


    .. code-block:: python3

        _NUMERIC_FIELDS = set((
            'width', 'height', 'tbr', 'abr', 'asr', 'vbr', 'fps', 'filesize', 'filesize_approx',
            'timestamp', 'upload_year', 'upload_month', 'upload_day',
            'duration', 'view_count', 'like_count', 'dislike_count', 'repost_count',
            'average_rating', 'comment_count', 'age_limit',
            'start_time', 'end_time',
            'chapter_number', 'season_number', 'episode_number',
            'track_number', 'disc_number', 'release_year',
            'playlist_index',
        ))

        params = None
        _ies = []
        _pps = []
        _download_retcode = None
        _num_downloads = None
        _screen_file = None

        def __init__(self, params=None, auto_init=True):
            # Create a FileDownloader object with the given options.
            if params is None:
                params = {}
            self._ies = []
            self._ies_instances = {}
            self._pps = []
            self._progress_hooks = []
            self._download_retcode = 0
            self._num_downloads = 0
            self._screen_file = [sys.stdout, sys.stderr][params.get('logtostderr', False)]
            self._err_file = sys.stderr
            self.params = {
                # Default parameters
                'nocheckcertificate': False,
            }
            self.params.update(params)
            self.cache = Cache(self)

    So there it is!
    """

    def __init__(self, *args, **kwargs):
        """Initialize with the ytdl state."""
        super().__init__(self, *args, **kwargs)

    def parseOpts(self):
        """Return a dict of user-provided args."""
        return self.parseOpts()[1]


def ytdl(link, ytdl_opts):
    """Execute downloading a YouTube video.

    Possibly makes sense to make this a class. Playlists are a subclass,
    objects with variable sizes are others etc.

    .. todo:: Should merge the built-in options I have here with user provided ones.

    Parameters
    ----------
    link : str
        URL to a Youtube video

    Returns
    -------
    todo

    .. :returns: Request object or :class:`urllib.Response` if :mod:`requests` isn't downloaded.

    .. currently it does not.

    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'output': 'TODO:',
        'logger': LOGGER,
        'progress_hooks': [my_hook],
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    ydl.download(link)


def requests_dl(link):
    """TODO: Docstring for requests_dl.

    Parameters
    ----------
    link : str
        Download a URL using :mod:`requests`.

    Returns
    -------
    TODO

    """
    res = requests.get(link)
    res.raise_for_status()
    # might not need bs4 if all im doing is downloading.
    # could analyze at a later point
    # soup = BeautifulSoup(source, "html.parser")

    # should figure out how to parse the title of the page and save it
    # as the filename
    # should also choose a different file path then 'wherever we run this'
    file = "web_page.txt"  # fix hard coded nonsense
    with open(file, mode="ab") as f:
        for chunk in res.iter_content(100000):
            f.write(chunk)
        f.close

    logging.debug(f.closed)


def my_hook(d):
    """Hook to notify the user the download is completed."""
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


def main():
    """Execute the program.

    It's going to be necessary to implement a dict merger soon.

    Also env_checks for xdg_config_home so merge 3 dicts with config file
    options set.

    """
    dl = TermuxDL(**kwargs)

    ytdl_opts = dl.parseOpts()

    logging.debug("Options: ")
    logging.debug(ytdl_opts)

    try:  # honestly might not be the right method
        link = ytdl_opts.geturl
        logging.info(link)
    except Exception as e:
        sys.exit(e)

    if not REQUESTS:
        res = urllib.parse.urlparse(link)

        if res[2] == "/playlist":
            logging.debug(
                "This seems like a YouTube playlist. Downloading. Press Ctrl-C to stop"
            )

        elif res[1] == "youtu.be":
            print(ytdl(link))

    else:
        ytdl(link, ytdl_opts)
        # requests_dl(link)


if __name__ == "__main__":
    main()
