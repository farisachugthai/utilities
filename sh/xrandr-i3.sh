#!/usr/bin/env bash
# Maintainer: Faris Chugthai

# set -euo pipefail
# Very minimal script for the time being

# xrandr does have it's bash completion set up on this computer so whoo

xrandr

sleep 3

echo -e "There's your display output. We're going to disable the laptop."
echo -e "This should be display LVDS-1."

sleep 3

xrandr --output LVDS-1 --off

exit 0
