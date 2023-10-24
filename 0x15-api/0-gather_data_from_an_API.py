#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""

import json
import sys
import urllib
import urllib.request


def use_rest_api(input):
    """
    The script must accept an integer as a parameter,
    which is the employee ID
    The script must display on the standard output the employee
    TODO list progress in this exact format:
    First line:
    Employee EMPLOYEE_NAME is done with tasks(DONE_TASKS/TOTAL_TASKS):
    """

    rest_url = f"https://jsonplaceholder.typicode.com/users/{input}"

    request_url = urllib.request.urlopen(rest_url)
    rest_api_data = request_url.read()
    # print(rest_api_data)

    usr_data = json.loads(rest_api_data)
    """
    {
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
    }
    """
    EMP_NAME = usr_data.get("name")

    """
    Second and N next lines display the title of completed tasks:
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
    """
    to_do_url = f"https://jsonplaceholder.typicode.com/todos?userId={input}"
    to_do_request_url = urllib.request.urlopen(to_do_url)
    to_do_lst = to_do_request_url.read()
    todo_lsit = json.loads(to_do_lst)

    DONE_TASKS = sum(1 for todo in todo_lsit if todo["completed"])
    TOTAL = len(todo_lsit)
    print(f"Employee {EMP_NAME} is done with tasks({DONE_TASKS}/{TOTAL}):")

    for to_do in todo_lsit:
        if (to_do["completed"]):
            print(f"\t {to_do['title']}")


if __name__ == "__main__":
    """
    """
    input = sys.argv[1]
    try:
        input = int(input)
    except Exception as e:
        print(e)
    use_rest_api(input)
