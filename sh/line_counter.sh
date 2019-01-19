#!/usr/bin/env bash
# Maintainer: Faris Chugthai

# set -euo pipefail

# Determine the number of lines in a directory.
# ag is case insensitive so you don't need the [a-zA-z] idiom
# --noheading didn't change anything

if [[ $(command -v ag) ]]; then
    echo -e "The number of lines in this directory tree is:\n"

    ag --nobreak --nocolor --nofilename --hidden --follow -- "[a-z]|[blank]" ./** | wc -l

elif [[ $(command -v fd) ]]; then
    # Didn't fully realize how much simpler this is.
    echo -e "The number of lines in this directory tree is:\n"

    fd | wc -l

else
    # TODO.
    exit 127

fi

exit 0
