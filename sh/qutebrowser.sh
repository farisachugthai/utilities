#!/usr/bin/env bash
# Maintainer: Faris Chugthai 

export LD_LIBRARY_PATH="$HOME/src/qutebrowser/libssl"

# check if we're already in a venv.
# If we're in a venv but the wrong one deactivate
if [[ -n "$VIRTUAL_ENV" ]]; then
    if [[ "$VIRTUAL_ENV" != "/home/faris/src/qutebrowser/.venv" ]]; then
        deactivate;
        source ~/src/qutebrowser/.venv/bin/activate;
    fi
else
    source ~/src/qutebrowser/.venv/bin/activate;
fi

sleep 3

echo "Starting qutebrowser."

python3 ~/src/qutebrowser/qutebrowser.py

exit 0
