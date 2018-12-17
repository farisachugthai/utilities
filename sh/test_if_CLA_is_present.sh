#!/usr/bin/env bash
# Test whether command-line argument is present (non-empty).

if [[ -n "$1" ]]; then
    lines="$1"
else
    echo -e "Usage: $0"  # and any necessary flags you would like to throw in

    # At this point either exit or provide some default value
    # Could check env vars as well
fi

exit 0
