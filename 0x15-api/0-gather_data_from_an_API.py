#!/usr/bin/python3
"""
Get a randomly created to-do list from an API
"""


import requests
import json
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee = requests.get(url).json()

    tasks = requests.get(f'{url}/todos').json()

    completed = [task for task in tasks if task.get('completed') is True]
    print('Employee {} is done with tasks({}/{}:'
          .format(employee.get('name'), len(completed), len(tasks)))
    for task in completed:
        print('\t {}'.format(task.get('title')))
