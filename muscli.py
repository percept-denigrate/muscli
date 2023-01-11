#!/usr/bin/python3

import os
import sys
import datetime as dt

path = '/home/' + os.environ.get('USER') + '/.muscli/'

if len(sys.argv) == 1:
    with open(path + 'data', 'r') as file:
        lines = file.readlines()
    last_number = int(lines[1][0:-1])
    last_day = lines[2]
    print(last_day)
    last_day_dt = dt.datetime.strptime(last_day,'%Y/%m/%d')
    print(last_day_dt)
    diff = dt.date.today()-last_day_dt.date()
    print(dt.date.today(),dt.datetime.strptime(last_day,'%Y/%m/%d').date())
    d = diff.days
    print(d)
    new_number = str((last_number+d) % int(lines[0][0:-1]))
    data_new = [lines[0], new_number +'\n', dt.date.today().strftime('%Y/%m/%d')]
    with open(path + 'data', 'w') as file:
        file.writelines(data_new)

    with open(path + new_number, 'r') as file:
        print(file.read())
