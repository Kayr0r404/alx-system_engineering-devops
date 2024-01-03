#!/usr/bin/python3
''' Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
 and export data in the JSON format.
'''
import json
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]

    r_todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id))
    r_usr = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))

    usrname = r_usr.json()['username']
    dict = {}
    list = []
    for data in r_todo.json():
        list.append(
            {
                'task': data.get('title'),
                'completed': data.get('completed'),
                'username': usrname
            }
        )
    dict[employee_id] = list
    with open(file='{}.json'.format(employee_id), mode='w') as jsonfile:
        json.dump(dict, jsonfile)
