#!usr/bin/env bash

# change the value after tail to see a different number
# TODO: run a check to see if theres an argument given.
# if so give it to tail
history | tr -s ' ' | cut -d ' ' -f5 | sort | uniq -c | sort -n | tail -n 20 | perl -lane 'print $F[1], "\t", $F[0], " ", "▄" x ($F[0] / 12)'
