#!/usr/bin/env bash
# Maintainer: Faris Chugthai 

# set -euo pipefail

# Determine the number of lines in a directory.
# ag is case insensitive so you don't need the [a-zA-z] idiom
# --noheading didn't change anything

echo -e "The number of lines in this directory tree is:\n"

ag --nobreak --nocolor --nofilename --hidden --follow -- "[a-z]|[blank]" ./** | wc -l

exit 0
