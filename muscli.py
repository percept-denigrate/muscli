#!/usr/bin/python3

import os
import sys
import datetime as dt

path = '/home/' + os.environ.get('USER') + '/.muscli/data'

if len(sys.argv) == 1:
    with open(path, 'r') as file:
        lines = file.readlines()
    last_number = int(lines[1][0:-1])
    last_day = lines[2][0:-1]
    diff = dt.date.today()-dt.datetime.strptime(last_day,'%Y/%m/%d').date()
    d = diff.days
    print(d)
    data_new = [lines[0], str((last_number+d) % int(lines[0][0:-1]))+'\n', dt.date.today().strftime('%Y/%m/%d')]
    with open(path, 'w') as file:
        file.writelines(data_new)
