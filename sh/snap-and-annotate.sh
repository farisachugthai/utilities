#!/bin/bash
# found on http://www.linux-magazine.com/Issues/2016/193/Workspace-Termux#article_l1
# this script utilizes the termux api to take a picture and then annotate it in a csv file
# i then modified the value of dir
# 03/30/18

# TODO: save the old dir

dir="/data/data/com.termux/files/home/storage/pictures"
dt="$(date +%Y%m%d-%H%M%S)"

if [[ ! -d "$dir" ]]; then
        mkdir -pv "$dir"
fi

cd "$dir"  || exit 128

if [[ -n "$(command -v termux-toast)" ]]; then
        echo "Hold camera still..." | termux-toast
else
        echo 'No command named termux-toast found.'
        exit 127
fi

termux-camera-photo "$dt.jpg"

echo "Done!" | termux-toast

if [[ -z "$(command -v jq)" ]]; then
        echo 'jq not found'
        exit 127
fi

lat="$(termux-location | jq '.latitude')"

lon="$(termux-location | jq '.longitude')"

echo "Coordinates: $lat, $lon" | termux-toast

comment="$(termux-dialog -m -t "Comment")"

osm="http://www.openstreetmap.org/index.html?mlat=$lat&mlon=$lon&zoom=18"

echo "Photo: $dt.jpg Latitude: $lat, Longitude: $lon, OSM: $osm, Comment: $comment" >> annotations.csv
echo "All done!" | termux-toast

termux-vibrate

exit 0
