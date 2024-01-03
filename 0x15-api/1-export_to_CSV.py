#!/usr/bin/python3
''' Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
 and export data in the CSV format.
'''
import csv
import requests
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    r_todo = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            employee_id))
    r_usr = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    
    with open(file='{}.csv'.format(employee_id),
              mode='w', newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        for data in r_todo.json():
            csv_writer.writerow([int(employee_id),
                                 data.get('completed'),
                                 data.get('title')])

    
