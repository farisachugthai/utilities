#!/usr/bin/env bash

# generate installed package list
dpkg --get-selections | cut -f1 > mypackages.txt

echo -e 'Placing dpkg get-selections output into the file `mypackages.txt`.'

# install packages
if [[ $EUID == 0 ]]; then
    echo -e 'Installing now!'
    xargs -0 apt install -y < <(tr \\n \\0 < mypackages.txt)
else
    echo -e 'ERR: You must be root to run this.'
    exit 127  # still never learned exit codes
fi

exit 0
