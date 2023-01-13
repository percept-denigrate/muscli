#!/usr/bin/python3

import os
import sys
import datetime as dt

path = '/home/' + os.environ.get('USER') + '/.muscli/'
date_format = '%Y/%m/%d'

with open(path + 'data', 'r') as file:    #reads data file
    lines = file.readlines()
n = int(lines[0][0:-1])
day = int(lines[1][0:-1])
last_called = lines[2][0:-1]

if len(sys.argv) == 1:
    diff = dt.date.today()-dt.datetime.strptime(last_called,date_format).date()    #number of days since last use
    day_new = str((day+diff.days) % int(lines[0][0:-1]))
    data_new = [lines[0], day_new +'\n', dt.date.today().strftime(date_format) + '\n']
    with open(path + 'data', 'w') as file:    #updates data file
        file.writelines(data_new)

    with open(path + day_new, 'r') as file:    #prints workout
        print(file.read())

elif len(sys.argv) == 4 and sys.argv[1] == 'incr':
    for i in range(n):    #search in each workout
        with open(path + str(i), 'r') as file: 
            workout = file.readlines()
        for j in range(len(workout)):    #check each line
            words = workout[j][0:-1].split(' ')
            if words[0] == sys.argv[2]:    #when exercise is found
                workout_new = workout[:]
                exercise_new = ''    #recreates the line with the new weight
                for k in range(len(words)-1):
                    exercise_new += words[k] + ' '
                exercise_new += str(float(words[-1]) + float(sys.argv[3]))
                exercise_new += '\n'
                print(exercise_new)
                workout_new[j] = exercise_new
                with open(path + str(i), 'w') as file:    #updates workout file
                    file.writelines(workout_new)

elif len(sys.argv) == 2 and sys.argv[1] == 'shift':
    data_new = lines[:]
    data_new[1] = str(day-1) + '\n'
    with open(path + 'data', 'w') as file:    #updates data file
        file.writelines(data_new)
