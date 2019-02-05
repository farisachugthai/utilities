#!/usr/bin/env bash
# Maintainer: Faris Chugthai 

# Is there a better way to do this than overwriting LD_LIBRARY_PATH?
# How about we only do this if it's already empty
if [[ -z "$LD_LIBRARY_PATH" ]]; then
    export LD_LIBRARY_PATH="$HOME/src/qutebrowser/libssl"
else
    echo 'LD_LIBRARY_PATH already set. Not overwriting.'
    exit 1
fi

# -n is True if a string is not empty
# This means that we first check if we're already in a venv.
if [[ -n "$VIRTUAL_ENV" ]]; then
    
    # If we're in a venv but the wrong one deactivate
    if [[ "$VIRTUAL_ENV" != "/home/faris/src/qutebrowser/.venv" ]]; then
        deactivate;
        # shellcheck source=/home/faris/src/qutebrowser/.venv/bin/activate
        source ~/src/qutebrowser/.venv/bin/activate;
    fi
else
    # shellcheck source=/home/faris/src/qutebrowser/.venv/bin/activate
    source ~/src/qutebrowser/.venv/bin/activate;
fi

sleep 3

echo "Starting qutebrowser."

python3 ~/src/qutebrowser/qutebrowser.py

exit 0
