#!/usr/bin/env bash
# Show your most frequently run commands by querying ``history``

# Script is functional even if truncated to:
# history | tr -s ' ' | cut -d ' ' -f5 | sort | uniq -c | sort -n | tail -n 20 

# The perl section simply provides the visual
history | tr -s ' ' | cut -d ' ' -f5 | sort | uniq -c | sort -n | tail -n 20 | perl -lane 'print $F[1], "\t", $F[0], " ", "-" x ($F[0] / 12)'

exit 0
