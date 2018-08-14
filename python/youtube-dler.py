#!/usr/bin/env python
"""Embedding youtube-dl

From the manpage:

From a Python program, you can embed youtube-dl in a more powerful fashion, like this:

    from __future__ import unicode_literals
    import youtube_dl

    ydl_opts = {}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])

    Most likely, you'll want to use various options.  For a list of options
    available, have a look at youtube_dl/YoutubeDL.py
    (https://github.com/rg3/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312).
    For a start, if you want to intercept youtube-dl's output, set a logger object.
    Here's a more complete example of a program that outputs only error (and a
    short message after the download is finished), and downloads/converts the
    video to an mp3 file:

        from __future__ import unicode_literals
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

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])

Whew!
"""
