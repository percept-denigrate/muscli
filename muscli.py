#!/usr/bin/python3

import os
import sys
import datetime as dt

path = '/home/' + os.environ.get('USER') + '/.muscli/'
date_format = '%Y/%m/%d'

if len(sys.argv) == 1:
    with open(path + 'data', 'r') as file: #reads data file
        lines = file.readlines()
    last_number = int(lines[1][0:-1])
    last_day = lines[2][0:-1]

    diff = dt.date.today()-dt.datetime.strptime(last_day,date_format).date() #number of days since last use
    new_number = str((last_number+diff.days) % int(lines[0][0:-1]))
    data_new = [lines[0], new_number +'\n', dt.date.today().strftime(date_format) + '\n']
    with open(path + 'data', 'w') as file: #updates data file
        file.writelines(data_new)

    with open(path + new_number, 'r') as file: #prints workout
        print(file.read())
