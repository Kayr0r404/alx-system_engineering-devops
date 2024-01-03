#!/usr/bin/python3
''' Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
'''
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    r_todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id))
    r_usr = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    count = 0
    complted_titles = []
    for dict in r_todo.json():
        if 'completed' in dict:
            count += 1
            if dict.get("completed") is True:
                complted_titles.append(dict['title'])
    employee_name = r_usr.json()['name']

    print('Employee {} is done with tasks({}/{}):'.format(
        employee_name, len(complted_titles), count))
    for title in complted_titles:
        print('\t {}'.format(title))
