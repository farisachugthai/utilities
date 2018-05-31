#!/usr/bin/env/ python3
# https://pymotw.com/3/os/index.html
# Replacing or renaming an existing file is not idempotent and may expose
# applications to race conditions. The rename() and replace() functions
# implement safe algorithms for these actions, using atomic operations on
# POSIX-compliant systems when possible.

# os_rename_replace.py

import glob
import os


with open('rename_start.txt', 'w') as f:
    f.write('starting as rename_start.txt')

print('Starting:', glob.glob('rename*.txt'))

os.rename('rename_start.txt', 'rename_finish.txt')

print('After rename:', glob.glob('rename*.txt'))

with open('rename_finish.txt', 'r') as f:
    print('Contents:', repr(f.read()))

with open('rename_new_contents.txt', 'w') as f:
    f.write('ending with contents of rename_new_contents.txt')

os.replace('rename_new_contents.txt', 'rename_finish.txt')

with open('rename_finish.txt', 'r') as f:
    print('After replace:', repr(f.read()))

for name in glob.glob('rename*.txt'):
    os.unlink(name)

# Renaming a file may fail if it is being moved to a new fileystem or if the destination already exists.

# $ python3 os_rename_replace.py

# Starting: ['rename_start.txt']
# After rename: ['rename_finish.txt']
# Contents: 'starting as rename_start.txt'
# After replace: 'ending with contents of rename_new_contents.txt'
