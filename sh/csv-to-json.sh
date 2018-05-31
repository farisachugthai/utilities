#!/bin/bash

# TODO: yes you are putting a TODO in a one-liner
# Find the original python wiki article and give credit where credit is due
python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"
