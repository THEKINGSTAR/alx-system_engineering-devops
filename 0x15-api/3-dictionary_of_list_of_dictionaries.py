#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""

import sys
import urllib
import urllib.request


def fetch_all_tasks():
    """
    Python script to export data in the JSON format.
    Requirements:
    Records all tasks from all employees
    Format must be:
    {
    "USER_ID":
    [ {"username": "USERNAME",
    "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS},
    {"username": "USERNAME",
    "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, ... ],
    "USER_ID":
    [ {"username": "USERNAME",
    "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS},
    {"username": "USERNAME",
    "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, ...
    ]
    }

    File name must be: todo_all_employees.json
    """
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"

    all_users_data = []

    # Fetch data for all users
    users_response = requests.get(users_url)
    users_data = users_response.json()

    for user_data in users_data:
        user_id = user_data["id"]
        username = user_data["username"]

        tasks_url = f"{base_url}/todos?userId={user_id}"
        tasks_response = requests.get(tasks_url)
        tasks_data = tasks_response.json()

        user_tasks = []

        for task_data in tasks_data:
            task_title = task_data["title"]
            task_completed = task_data["completed"]
            user_task = {
                "username": username,
                "task": task_title,
                "completed": task_completed
            }
            user_tasks.append(user_task)

        all_users_data.append({str(user_id): user_tasks})

    #  Create a dictionary with user data
    all_data = {}
    for user_data in all_users_data:
        all_data.update(user_data)

    #  Write the data to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)  # ,indent=4)


if __name__ == "__main__":
    """
    RUN THE APP
    """
    fetch_all_tasks()
