#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
Python script to export data in the CSV format.
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
    # INCOME DATA
    """
        {
        "userId": 2,
        "id": 21,
        "title": "suscipit repellat esse quibusdam voluptatem incidunt",
        "completed": false
        },
    """
    # PRINT STATMENT FOR TASK # 0
    """
    print(f"Employee {EMP_NAME} is done with tasks({DONE_TASKS}/{TOTAL}):")

    for to_do in todo_lsit:
        if (to_do["completed"]):
            print(f"\t {to_do['title']}")
    """

    """
    Records all tasks that are owned by this employee

    Format must be:
    {
    "USER_ID":
    [
    {"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"},
    {"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, ...
    ]
    }

    File name must be: USER_ID.json
    """
    id = f"{input}"
    file_name = f"{id}.json"
    USER = {}
    TASK_LIST = []
    try:
        with open(file_name, 'w') as file:
            for tsk in todo_lsit:
                # print(tsk)
                USER_TASKS = {}
                EMP_USR_NAME = usr_data.get("username")
                USER_TASKS["task"] = (f"{tsk['title']}")
                USER_TASKS["completed"] = (f"{tsk['completed']}")
                USER_TASKS["username"] = (f"{EMP_USR_NAME}")
                TASK_LIST.append(USER_TASKS)
                # print(f"USER TASKS ======= {USER_TASKS}\n")
                # print(f"TAKS LISTS ####### {TASK_LIST}\n")
            USER[id] = TASK_LIST
            json.dump(USER, file)
    except Exception as e:
        print(f"ERRORE IN WRITE TO FILE : {e}")


if __name__ == "__main__":
    """
    """
    input = sys.argv[1]
    try:
        input = int(input)
    except Exception as e:
        print(e)
    use_rest_api(input)
