#!/usr/bin/python3
#python script
''' Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
'''
from sys import argv
import requests

employee_id = argv[1]
r_todo = requests.get(
    'https://jsonplaceholder.typicode.com/users/1/todos?userId={}'.format(
        employee_id))
r_usr = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
r_todo.json()
count = complete = 0
complted_titles = []
for dict in r_todo.json():
    if 'completed' in dict:
        count += 1
        if dict['completed'] is True:
            complted_titles.append(dict['title'])
            complete += 1
employee_name = r_usr.json()['name']


if __name__ == '__main__':
    print('Employee {} is done with tasks({}/{}):'.format(
        employee_name, complete, count))
    for title in complted_titles:
        print('\t ', title)
