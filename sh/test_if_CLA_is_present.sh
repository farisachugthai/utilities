#!/bin/bash
# Test whether command-line argument is present (non-empty).

if [-n "$1" ]
then
    lines=$1
else
    lines=$LINES # Default, if not specified on command-line.
fi
