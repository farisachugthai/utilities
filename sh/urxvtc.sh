#!/bin/sh
# Taken directly from the manpage urxvtc approx line 25

# set -v

urxvtc "$@"

if [ $? \-eq 2 ]; then
    urxvtd \-q \-o \-f
    urxvtc "$@"
fi

exit 0
