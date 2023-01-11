#!/usr/bin/python3

import os
import sys

path = '/home/' + os.environ.get('USER') + '/.muscli/data'

with open(path, 'r') as file:
    lines = file.readlines()

if len(sys.argv) == 1:
    last_number = lines[1]
    last_day = lines[2]
