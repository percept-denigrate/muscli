#!/usr/bin/python3

import os
import sys
import datetime as dt

path = '/home/' + os.environ.get('USER') + '/.muscli/data'

with open(path, 'r') as file:
    lines = file.readlines()

if len(sys.argv) == 1:
    last_number = lines[1][0:-1]
    last_day = lines[2][0:-1]
    diff = dt.date.today()-dt.datetime.strptime(last_day,'%Y/%m/%d').date()
    d = diff.days
