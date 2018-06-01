#!/usr/bin/env python

# 05/21/18
# method 1
# honestly not a great example. better when you're not using strings.
# this is great for wjen you have 0 user interaction and you're usinf 
# the output of other OOP apps to interact with your filesystem

# but cjange how usr_dir was obtained and this is a good examole
# look at mv_to_repo.py as of 05/21/18
from pathlib import Path
cwd = Path.cwd()
usr_dir = input("Print the name of the directory you want below your current\
        working directory.")
new_dir = Path.joinpath(cwd, usr_dir)

# important to note. call mkdir on the new path you want not on an old path and extend it.
# EAFP man always remember
cwd.mkdir(new_dir)

print(new_dir.absolute())

# method 2
import os
# os.makedirs()
# os.mkdir()

chtos = os.getcwd()
# '/storage/emulated/0/Android/data/com.dropbox.android/files/u730416625/scratch/.cheat'

newdir = os.path.join(chtos, "new-rclone")
# Out[109]: '/storage/emulated/0/Android/data/com.dropbox.android/files/u730416625/scratch/.cheat/new-rclone'

os.mkdir(newdir)
