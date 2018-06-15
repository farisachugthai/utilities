#!/usr/bin/env python3
#
# should do the encoding thing above
# From pydocs tutorials stdlib2. Reformatted.

import time
import os.path
from string import Template

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']


class BatchRename(Template):
    delimiter = '%'


fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
# Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

# img_1074.jpg --> Ashley_0.jpg
# img_1076.jpg --> Ashley_1.jpg
# img_1077.jpg --> Ashley_2.jpg
