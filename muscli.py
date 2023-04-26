#!/usr/bin/python3

import os
import sys
import datetime as dt

DATA_DIRECTORY = '/home/' + os.environ.get('USER') + '/.muscli/'
DATE_FORMAT = '%Y/%m/%d'

def update_data_file(new_data_lines):
    with open(DATA_DIRECTORY + 'data', 'w') as file:
        file.writelines(new_data_lines)


with open(DATA_DIRECTORY + 'data', 'r') as file:
    data_lines = file.readlines()
number_of_workouts = int(data_lines[0][0:-1])
current_workout_index = int(data_lines[1][0:-1])
last_date_called = data_lines[2][0:-1]

if len(sys.argv) == 1:
    days_since_last_use = dt.date.today() - dt.datetime.strptime(last_date_called, DATE_FORMAT).date()
    new_current_workout_index = str((current_workout_index + days_since_last_use.days) % number_of_workouts)
    new_data_lines = [data_lines[0], new_current_workout_index +'\n', dt.date.today().strftime(DATE_FORMAT) + '\n']
    update_data_file(new_data_lines)
    with open(DATA_DIRECTORY + new_current_workout_index, 'r') as file:
        print(file.read())

elif len(sys.argv) == 4 and sys.argv[1] == 'incr':
    for i in range(number_of_workouts):
        with open(DATA_DIRECTORY + str(i), 'r') as file:
            workout_lines = file.readlines()
        for j in range(len(workout_lines)):
            words = workout_lines[j][0:-1].split(' ')
            if words[0] == sys.argv[2]:
                new_workout_lines = workout_lines[:]
                updated_exercise_line = ' '.join(words[0:-1]) + ' ' + str(float(words[-1]) + float(sys.argv[3])) + '\n'
                print('Exercise updated')
                new_workout_lines[j] = updated_exercise_line
                with open(DATA_DIRECTORY + str(i), 'w') as file:
                    file.writelines(new_workout_lines)

elif len(sys.argv) == 2 and sys.argv[1] == 'shift':
    new_data_lines = data_lines[:]
    new_data_lines[1] = str(current_workout_index - 1) + '\n'
    update_data_file(new_data_lines)

elif len(sys.argv) == 2 and sys.argv[1] == 'unshift':
    new_data_lines = data_lines[:]
    new_data_lines[1] = str(current_workout_index + 1) + '\n'
    update_data_file(new_data_lines)

