#!/usr/bin/python3
''' Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
 and exports data in the JSON format..
'''
import json
import requests


if __name__ == '__main__':
    try:
        users_request = requests.get(
            'https://jsonplaceholder.typicode.com/users/')
        users_data = users_request.json()

        all_employees_data = {}

        for employee_id, user_info in enumerate(users_data, start=1):
            todo_request = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                    employee_id
                ))
            user_request = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}'.format(
                    employee_id
                ))

            if todo_request.status_code == 200 and \
                    user_request.status_code == 200:
                username = user_request.json()['username']
                todo_list = []

                for todo_data in todo_request.json():
                    todo_list.append({
                        'username': username,
                        'task': todo_data.get('title'),
                        'completed': todo_data.get('completed')
                    })

                employee_dict = {employee_id: todo_list}
                all_employees_data.update(employee_dict)

            else:
                print(f"Failed to retrieve data for employee ID {employee_id}")

        with open(file='todo_all_employees.json', mode='w') as jsonfile:
            json.dump(all_employees_data, jsonfile)

    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
