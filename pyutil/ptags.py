<<<<<<< .merge_file_An8MzH
#!/usr/bin/python3.6
"""Create a tags file for Python programs, usable with vi.

Tagged are:
    - functions (even inside other defs or classes)
    - classes
    - filenames

Warns about files it cannot open.

No warnings about duplicate tags.

Snagged from the scripts dir in python3.6-examples.

TODO::
    Add docstrings.
    Use ipdb and step through while watching the tags var.
    Initially it was defined outside the ifmain loop.

    I moved it, but without the global keyword I don't get how any changes
    to tags in treat_file will propogate back to main.

Otherwise add in pep257 compliant params. Try different styles and see what you like.
"""
import os
import re
import sys


def main():
    args = sys.argv[1:]
    for filename in args:
        treat_file(filename)
    if tags:
        fp = open('tags', 'w')
        tags.sort()
        for s in tags:
            fp.write(s)


def treat_file(filename):
    try:
        fp = open(filename, 'r')
    except Exception:
        sys.stderr.write('Cannot open %s\n' % filename)
        return
    base = os.path.basename(filename)
    if base[-3:] == '.py':
        base = base[:-3]
    s = base + '\t' + filename + '\t' + '1\n'
    tags.append(s)
    while 1:
        line = fp.readline()
        if not line:
            break
        m = matcher.match(line)
        if m:
            content = m.group(0)
            name = m.group(2)
            s = name + '\t' + filename + '\t/^' + content + '/\n'
            tags.append(s)


if __name__ == '__main__':
    tags = []
    expr = r'^[ \t]*(def|class)[ \t]+([a-zA-Z0-9_]+)[ \t]*[:\(]'
    matcher = re.compile(expr)
    main()
||||||| .merge_file_uZpniB
=======
#!/usr/bin/python3.6
"""Create a tags file for Python programs, usable with vi.

Tagged are:
    - functions (even inside other defs or classes)
    - classes
    - filenames

Warns about files it cannot open.

No warnings about duplicate tags.

Snagged from the scripts dir in python3.6-examples.

TODO::
    Add docstrings.
    Use ipdb and step through while watching the tags var.
    Initially it was defined outside the ifmain loop.

    I moved it, but without the global keyword I don't get how any changes
    to tags in treat_file will propogate back to main.

Otherwise add in pep257 compliant params. Try different styles and see what you like.
"""
import os
import re
import sys


def main():
    """Handle CLAs and work with writing the tags file."""
    args = sys.argv[1:]
    for filename in args:
        treat_file(filename)
    if tags:
        fp = open('tags', 'w')
        tags.sort()
        for s in tags:
            fp.write(s)


def treat_file(filename):
    """Find usable matches for tags file."""
    try:
        fp = open(filename, 'r')
    except Exception:
        sys.stderr.write('Cannot open %s\n' % filename)
        return
    base = os.path.basename(filename)
    if base[-3:] == '.py':
        base = base[:-3]
    s = base + '\t' + filename + '\t' + '1\n'
    tags.append(s)
    while 1:
        line = fp.readline()
        if not line:
            break
        m = matcher.match(line)
        if m:
            content = m.group(0)
            name = m.group(2)
            s = name + '\t' + filename + '\t/^' + content + '/\n'
            tags.append(s)


if __name__ == '__main__':
    tags = []
    expr = r'^[ \t]*(def|class)[ \t]+([a-zA-Z0-9_]+)[ \t]*[:\(]'
    matcher = re.compile(expr)
    main()
>>>>>>> .merge_file_pB6Knx
