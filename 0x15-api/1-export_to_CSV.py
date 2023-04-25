#!/usr/bin/python3
"""Fetch employee data from an API"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    employee = requests.get(url).json()

    tasks = requests.get(f'{url}/todos').json()

    filename = f'{employee_id}.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
        for task in tasks:
            data = (employee_id, employee.get('username'),
                    task.get('completed'), task.get('title'))
            writer.writerow(data)
