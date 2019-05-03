#!/usr/bin/env/bash
# Maintainer: Faris Chugthai 

# set -euo pipefail

# Use fd to clean a directory of python cache files.
# A useful example of fd

clean() {
    fd -H -t f -I .*pyc -exec rm {}
}

exit 0
