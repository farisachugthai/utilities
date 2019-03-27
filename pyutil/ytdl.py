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


We got it!
----------
So I was reading the src and realized that almost all of the execution
happens in the :mod:`youtube_dl.__init__`_ file!!

This is a long copy and paste but read this::

        #!/usr/bin/env python
        # coding: utf-8

        from __future__ import unicode_literals

        __license__ = 'Public Domain'

        import codecs
        import io
        import os
        import random
        import sys


        from youtube_dl.options import (
            parseOpts,
        )
        from youtube_dl.compat import (
            compat_getpass,
            compat_shlex_split,
            workaround_optparse_bug9161,
        )
        from youtube_dl.utils import (
            DateRange,
            decodeOption,
            DEFAULT_OUTTMPL,
            DownloadError,
            expand_path,
            match_filter_func,
            MaxDownloadsReached,
            preferredencoding,
            read_batch_urls,
            SameFileError,
            setproctitle,
            std_headers,
            write_string,
            render_table,
        )
        from youtube_dl.update import update_self
        from youtube_dl.downloader import (
            FileDownloader,
        )
        from youtube_dl.extractor import gen_extractors, list_extractors
        from youtube_dl.extractor.adobepass import MSO_INFO
        from youtube_dl.YoutubeDL import YoutubeDL


        def _real_main(argv=None):
            # Compatibility fixes for Windows
            if sys.platform == 'win32':
                # https://github.com/rg3/youtube-dl/issues/820
                codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

            workaround_optparse_bug9161()

            setproctitle('youtube-dl')

            parser, opts, args = parseOpts(argv)

            # Set user agent
            if opts.user_agent is not None:
                std_headers['User-Agent'] = opts.user_agent

            # Set referer
            if opts.referer is not None:
                std_headers['Referer'] = opts.referer

            # Custom HTTP headers
            if opts.headers is not None:
                for h in opts.headers:
                    if ':' not in h:
                        parser.error('wrong header formatting, it should be key:value, not "%s"' % h)
                    key, value = h.split(':', 1)
                    if opts.verbose:
                        write_string('[debug] Adding header from command line option %s:%s\n' % (key, value))
                    std_headers[key] = value

            # Dump user agent
            if opts.dump_user_agent:
                write_string(std_headers['User-Agent'] + '\n', out=sys.stdout)
                sys.exit(0)

            # Batch file verification
            batch_urls = []
            if opts.batchfile is not None:
                try:
                    if opts.batchfile == '-':
                        batchfd = sys.stdin
                    else:
                        batchfd = io.open(
                            expand_path(opts.batchfile),
                            'r', encoding='utf-8', errors='ignore')
                    batch_urls = read_batch_urls(batchfd)
                    if opts.verbose:
                        write_string('[debug] Batch file urls: ' + repr(batch_urls) + '\n')
                except IOError:
                    sys.exit('ERROR: batch file could not be read')
            all_urls = batch_urls + [url.strip() for url in args]  # batch_urls are already striped in read_batch_urls
            _enc = preferredencoding()
            all_urls = [url.decode(_enc, 'ignore') if isinstance(url, bytes) else url for url in all_urls]

            if opts.list_extractors:
                for ie in list_extractors(opts.age_limit):
                    write_string(ie.IE_NAME + (' (CURRENTLY BROKEN)' if not ie._WORKING else '') + '\n', out=sys.stdout)
                    matchedUrls = [url for url in all_urls if ie.suitable(url)]
                    for mu in matchedUrls:
                        write_string('  ' + mu + '\n', out=sys.stdout)
                sys.exit(0)
            if opts.list_extractor_descriptions:
                for ie in list_extractors(opts.age_limit):
                    if not ie._WORKING:
                        continue
                    desc = getattr(ie, 'IE_DESC', ie.IE_NAME)
                    if desc is False:
                        continue
                    if hasattr(ie, 'SEARCH_KEY'):
                        _SEARCHES = ('cute kittens', 'slithering pythons',
                        'falling cat', 'angry poodle', 'purple fish',
                        'running tortoise', 'sleeping bunny', 'burping cow')

                        _COUNTS = ('', '5', '10', 'all')
                        desc += ' (Example: "%s%s:%s" )'
                        % (ie.SEARCH_KEY, random.choice(_COUNTS), random.choice(_SEARCHES))

                    write_string(desc + '\n', out=sys.stdout)
                sys.exit(0)
            if opts.ap_list_mso:
                table = [[mso_id, mso_info['name']] for mso_id, mso_info in MSO_INFO.items()]
                write_string('Supported TV Providers:\n'
                + render_table(['mso', 'mso name'], table)
                + '\n', out=sys.stdout)

                sys.exit(0)

            # Conflicting, missing and erroneous options
            if opts.usenetrc and (opts.username is not None or opts.password is not None):
                parser.error('using .netrc conflicts with giving username/password')
            if opts.password is not None and opts.username is None:
                parser.error('account username missing\n')
            if opts.ap_password is not None and opts.ap_username is None:
                parser.error('TV Provider account username missing\n')
            if opts.outtmpl is not None and (opts.usetitle or opts.autonumber or opts.useid):
                parser.error('using output template conflicts with using title, video ID or auto number')
            if opts.autonumber_size is not None:
                if opts.autonumber_size <= 0:
                    parser.error('auto number size must be positive')
            if opts.autonumber_start is not None:
                if opts.autonumber_start < 0:
                    parser.error('auto number start must be positive or 0')
            if opts.usetitle and opts.useid:
                parser.error('using title conflicts with using video ID')
            if opts.username is not None and opts.password is None:
                opts.password = compat_getpass('Type account password and press [Return]: ')
            if opts.ap_username is not None and opts.ap_password is None:
                opts.ap_password = compat_getpass('Type TV provider account password and press [Return]: ')
            if opts.ratelimit is not None:
                numeric_limit = FileDownloader.parse_bytes(opts.ratelimit)
                if numeric_limit is None:
                    parser.error('invalid rate limit specified')
                opts.ratelimit = numeric_limit
            if opts.min_filesize is not None:
                numeric_limit = FileDownloader.parse_bytes(opts.min_filesize)
                if numeric_limit is None:
                    parser.error('invalid min_filesize specified')
                opts.min_filesize = numeric_limit
            if opts.max_filesize is not None:
                numeric_limit = FileDownloader.parse_bytes(opts.max_filesize)
                if numeric_limit is None:
                    parser.error('invalid max_filesize specified')
                opts.max_filesize = numeric_limit
            if opts.sleep_interval is not None:
                if opts.sleep_interval < 0:
                    parser.error('sleep interval must be positive or 0')
            if opts.max_sleep_interval is not None:
                if opts.max_sleep_interval < 0:
                    parser.error('max sleep interval must be positive or 0')
                if opts.max_sleep_interval < opts.sleep_interval:
                    parser.error('max sleep interval must be greater than or equal to min sleep interval')
            else:
                opts.max_sleep_interval = opts.sleep_interval
            if opts.ap_mso and opts.ap_mso not in MSO_INFO:
                parser.error('Unsupported TV Provider, use --ap-list-mso to get a list of supported TV Providers')

            def parse_retries(retries):
                if retries in ('inf', 'infinite'):
                    parsed_retries = float('inf')
                else:
                    try:
                        parsed_retries = int(retries)
                    except (TypeError, ValueError):
                        parser.error('invalid retry count specified')
                return parsed_retries
            if opts.retries is not None:
                opts.retries = parse_retries(opts.retries)
            if opts.fragment_retries is not None:
                opts.fragment_retries = parse_retries(opts.fragment_retries)
            if opts.buffersize is not None:
                numeric_buffersize = FileDownloader.parse_bytes(opts.buffersize)
                if numeric_buffersize is None:
                    parser.error('invalid buffer size specified')
                opts.buffersize = numeric_buffersize
            if opts.http_chunk_size is not None:
                numeric_chunksize = FileDownloader.parse_bytes(opts.http_chunk_size)
                if not numeric_chunksize:
                    parser.error('invalid http chunk size specified')
                opts.http_chunk_size = numeric_chunksize
            if opts.playliststart <= 0:
                raise ValueError('Playlist start must be positive')
            if opts.playlistend not in (-1, None) and opts.playlistend < opts.playliststart:
                raise ValueError('Playlist end must be greater than playlist start')
            if opts.extractaudio:
                if opts.audioformat not in ['best', 'aac', 'flac', 'mp3', 'm4a', 'opus', 'vorbis', 'wav']:
                    parser.error('invalid audio format specified')
            if opts.audioquality:
                opts.audioquality = opts.audioquality.strip('k').strip('K')
                if not opts.audioquality.isdigit():
                    parser.error('invalid audio quality specified')
            if opts.recodevideo is not None:
                if opts.recodevideo not in ['mp4', 'flv', 'webm', 'ogg', 'mkv', 'avi']:
                    parser.error('invalid video recode format specified')
            if opts.convertsubtitles is not None:
                if opts.convertsubtitles not in ['srt', 'vtt', 'ass', 'lrc']:
                    parser.error('invalid subtitle format specified')

            if opts.date is not None:
                date = DateRange.day(opts.date)
            else:
                date = DateRange(opts.dateafter, opts.datebefore)

            # Do not download videos when there are audio-only formats
            if opts.extractaudio and not opts.keepvideo and opts.format is None:
                opts.format = 'bestaudio/best'

            # --all-sub automatically sets --write-sub if --write-auto-sub is not given
            # this was the old behaviour if only --all-sub was given.
            if opts.allsubtitles and not opts.writeautomaticsub:
                opts.writesubtitles = True

            outtmpl = ((opts.outtmpl is not None and opts.outtmpl) or
                       (opts.format == '-1' and opts.usetitle and '%(title)s-%(id)s-%(format)s.%(ext)s') or
                       (opts.format == '-1' and '%(id)s-%(format)s.%(ext)s') or
                       (opts.usetitle and opts.autonumber and '%(autonumber)s-%(title)s-%(id)s.%(ext)s') or
                       (opts.usetitle and '%(title)s-%(id)s.%(ext)s') or
                       (opts.useid and '%(id)s.%(ext)s') or
                       (opts.autonumber and '%(autonumber)s-%(id)s.%(ext)s') or
                       DEFAULT_OUTTMPL)
            if not os.path.splitext(outtmpl)[1] and opts.extractaudio:
                parser.error('Cannot download a video and extract audio into the same'
                             ' file! Use "{0}.%(ext)s" instead of "{0}" as the output'
                             ' template'.format(outtmpl))

            any_getting = opts.geturl or opts.gettitle or opts.getid or
                          opts.getthumbnail or opts.getdescription or
                          opts.getfilename or opts.getformat or
                          opts.getduration or opts.dumpjson or opts.dump_single_json
            any_printing = opts.print_json
            download_archive_fn =
                expand_path(opts.download_archive)
                if opts.download_archive is not None else opts.download_archive

            # PostProcessors
            postprocessors = []
            if opts.metafromtitle:
                postprocessors.append({
                    'key': 'MetadataFromTitle',
                    'titleformat': opts.metafromtitle
                })
            if opts.extractaudio:
                postprocessors.append({
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': opts.audioformat,
                    'preferredquality': opts.audioquality,
                    'nopostoverwrites': opts.nopostoverwrites,
                })
            if opts.recodevideo:
                postprocessors.append({
                    'key': 'FFmpegVideoConvertor',
                    'preferedformat': opts.recodevideo,
                })
            # FFmpegMetadataPP should be run after FFmpegVideoConvertorPP and
            # FFmpegExtractAudioPP as containers before conversion may not support
            # metadata (3gp, webm, etc.)
            # And this post-processor should be placed before other metadata
            # manipulating post-processors (FFmpegEmbedSubtitle) to prevent loss of
            # extra metadata. By default ffmpeg preserves metadata applicable for both
            # source and target containers. From this point the container won't change,
            # so metadata can be added here.
            if opts.addmetadata:
                postprocessors.append({'key': 'FFmpegMetadata'})
            if opts.convertsubtitles:
                postprocessors.append({
                    'key': 'FFmpegSubtitlesConvertor',
                    'format': opts.convertsubtitles,
                })
            if opts.embedsubtitles:
                postprocessors.append({
                    'key': 'FFmpegEmbedSubtitle',
                })
            if opts.embedthumbnail:
                already_have_thumbnail = opts.writethumbnail or opts.write_all_thumbnails
                postprocessors.append({
                    'key': 'EmbedThumbnail',
                    'already_have_thumbnail': already_have_thumbnail
                })
                if not already_have_thumbnail:
                    opts.writethumbnail = True

           # XAttrMetadataPP should be run after post-processors that may change file
            # contents

           if opts.xattrs:
                postprocessors.append({'key': 'XAttrMetadata'})

            # Please keep ExecAfterDownload towards the bottom as it allows
            # the user to modify the final file in any way.
            # So if the user is able to remove the file before your
            # postprocessor runs it might cause a few problems.

            if opts.exec_cmd:
                postprocessors.append({
                    'key': 'ExecAfterDownload',
                    'exec_cmd': opts.exec_cmd,
                })
            external_downloader_args = None
            if opts.external_downloader_args:
                external_downloader_args = compat_shlex_split(opts.external_downloader_args)
            postprocessor_args = None
            if opts.postprocessor_args:
                postprocessor_args = compat_shlex_split(opts.postprocessor_args)
            match_filter = (
                None if opts.match_filter is None
                else match_filter_func(opts.match_filter))

            ydl_opts = {
                'usenetrc': opts.usenetrc,
                'username': opts.username,
                'password': opts.password,
                'twofactor': opts.twofactor,
                'videopassword': opts.videopassword,
                'ap_mso': opts.ap_mso,
                'ap_username': opts.ap_username,
                'ap_password': opts.ap_password,
                'quiet': (opts.quiet or any_getting or any_printing),
                'no_warnings': opts.no_warnings,
                'forceurl': opts.geturl,
                'forcetitle': opts.gettitle,
                'forceid': opts.getid,
                'forcethumbnail': opts.getthumbnail,
                'forcedescription': opts.getdescription,
                'forceduration': opts.getduration,
                'forcefilename': opts.getfilename,
                'forceformat': opts.getformat,
                'forcejson': opts.dumpjson or opts.print_json,
                'dump_single_json': opts.dump_single_json,
                'simulate': opts.simulate or any_getting,
                'skip_download': opts.skip_download,
                'format': opts.format,
                'listformats': opts.listformats,
                'outtmpl': outtmpl,
                'autonumber_size': opts.autonumber_size,
                'autonumber_start': opts.autonumber_start,
                'restrictfilenames': opts.restrictfilenames,
                'ignoreerrors': opts.ignoreerrors,
                'force_generic_extractor': opts.force_generic_extractor,
                'ratelimit': opts.ratelimit,
                'nooverwrites': opts.nooverwrites,
                'retries': opts.retries,
                'fragment_retries': opts.fragment_retries,
                'skip_unavailable_fragments': opts.skip_unavailable_fragments,
                'keep_fragments': opts.keep_fragments,
                'buffersize': opts.buffersize,
                'noresizebuffer': opts.noresizebuffer,
                'http_chunk_size': opts.http_chunk_size,
                'continuedl': opts.continue_dl,
                'noprogress': opts.noprogress,
                'progress_with_newline': opts.progress_with_newline,
                'playliststart': opts.playliststart,
                'playlistend': opts.playlistend,
                'playlistreverse': opts.playlist_reverse,
                'playlistrandom': opts.playlist_random,
                'noplaylist': opts.noplaylist,
                'logtostderr': opts.outtmpl == '-',
                'consoletitle': opts.consoletitle,
                'nopart': opts.nopart,
                'updatetime': opts.updatetime,
                'writedescription': opts.writedescription,
                'writeannotations': opts.writeannotations,
                'writeinfojson': opts.writeinfojson,
                'writethumbnail': opts.writethumbnail,
                'write_all_thumbnails': opts.write_all_thumbnails,
                'writesubtitles': opts.writesubtitles,
                'writeautomaticsub': opts.writeautomaticsub,
                'allsubtitles': opts.allsubtitles,
                'listsubtitles': opts.listsubtitles,
                'subtitlesformat': opts.subtitlesformat,
                'subtitleslangs': opts.subtitleslangs,
                'matchtitle': decodeOption(opts.matchtitle),
                'rejecttitle': decodeOption(opts.rejecttitle),
                'max_downloads': opts.max_downloads,
                'prefer_free_formats': opts.prefer_free_formats,
                'verbose': opts.verbose,
                'dump_intermediate_pages': opts.dump_intermediate_pages,
                'write_pages': opts.write_pages,
                'test': opts.test,
                'keepvideo': opts.keepvideo,
                'min_filesize': opts.min_filesize,
                'max_filesize': opts.max_filesize,
                'min_views': opts.min_views,
                'max_views': opts.max_views,
                'daterange': date,
                'cachedir': opts.cachedir,
                'youtube_print_sig_code': opts.youtube_print_sig_code,
                'age_limit': opts.age_limit,
                'download_archive': download_archive_fn,
                'cookiefile': opts.cookiefile,
                'nocheckcertificate': opts.no_check_certificate,
                'prefer_insecure': opts.prefer_insecure,
                'proxy': opts.proxy,
                'socket_timeout': opts.socket_timeout,
                'bidi_workaround': opts.bidi_workaround,
                'debug_printtraffic': opts.debug_printtraffic,
                'prefer_ffmpeg': opts.prefer_ffmpeg,
                'include_ads': opts.include_ads,
                'default_search': opts.default_search,
                'youtube_include_dash_manifest': opts.youtube_include_dash_manifest,
                'encoding': opts.encoding,
                'extract_flat': opts.extract_flat,
                'mark_watched': opts.mark_watched,
                'merge_output_format': opts.merge_output_format,
                'postprocessors': postprocessors,
                'fixup': opts.fixup,
                'source_address': opts.source_address,
                'call_home': opts.call_home,
                'sleep_interval': opts.sleep_interval,
                'max_sleep_interval': opts.max_sleep_interval,
                'external_downloader': opts.external_downloader,
                'list_thumbnails': opts.list_thumbnails,
                'playlist_items': opts.playlist_items,
                'xattr_set_filesize': opts.xattr_set_filesize,
                'match_filter': match_filter,
                'no_color': opts.no_color,
                'ffmpeg_location': opts.ffmpeg_location,
                'hls_prefer_native': opts.hls_prefer_native,
                'hls_use_mpegts': opts.hls_use_mpegts,
                'external_downloader_args': external_downloader_args,
                'postprocessor_args': postprocessor_args,
                'cn_verification_proxy': opts.cn_verification_proxy,
                'geo_verification_proxy': opts.geo_verification_proxy,
                'config_location': opts.config_location,
                'geo_bypass': opts.geo_bypass,
                'geo_bypass_country': opts.geo_bypass_country,
                'geo_bypass_ip_block': opts.geo_bypass_ip_block,
                # just for deprecation check
                'autonumber': opts.autonumber if opts.autonumber is True else None,
                'usetitle': opts.usetitle if opts.usetitle is True else None,
            }

            with YoutubeDL(ydl_opts) as ydl:
                # Update version
                if opts.update_self:
                    update_self(ydl.to_screen, opts.verbose, ydl._opener)

                # Remove cache dir
                if opts.rm_cachedir:
                    ydl.cache.remove()

                # Maybe do nothing
                if (len(all_urls) < 1) and (opts.load_info_filename is None):
                    if opts.update_self or opts.rm_cachedir:
                        sys.exit()

                    ydl.warn_if_short_id(sys.argv[1:] if argv is None else argv)
                    parser.error(
                        'You must provide at least one URL.\n'
                        'Type youtube-dl --help to see a list of all options.')

                try:
                    if opts.load_info_filename is not None:
                        retcode = ydl.download_with_info_file(expand_path(opts.load_info_filename))
                    else:
                        retcode = ydl.download(all_urls)
                except MaxDownloadsReached:
                    ydl.to_screen('--max-download limit reached, aborting.')
                    retcode = 101

            sys.exit(retcode)


        def main(argv=None):
            try:
                _real_main(argv)
            except DownloadError:
                sys.exit(1)
            except SameFileError:
                sys.exit('ERROR: fixed output name but more than one file to download')
            except KeyboardInterrupt:
                sys.exit('\nERROR: Interrupted by user')


        __all__ = ['main', 'YoutubeDL', 'gen_extractors', 'list_extractors']


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

LOGGER = logging.basicConfig(level=logging.WARNING)


class TermuxDL(youtube_dl.YoutubeDL, *args, **kwargs):
    r"""Try subclassing :class:`youtube_dl.YoutubeDL` and see if it's easier.

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
        'format':
        'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'output':
        'TODO:',
        'logger':
        logger,
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
    """Execute the program."""
    dl = TermuxDL(*args, **kwargs)

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
