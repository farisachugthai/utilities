#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
from pathlib import Path
import sys


def csv_to_json():
    if not Path(sys.argv[1:]).is_file():
        sys.exit("Error. Please provide a path to the file(s) to edit.\n")

    with open(sys.argv[1:]) as f:
        csv_file = list(csv.reader(f))
        return json.dumps(csv_file)


if __name__ == "__main__":
    json_file = csv_to_json()
