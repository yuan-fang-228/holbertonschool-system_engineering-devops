#!/usr/bin/python3
"""Export data of all employees in JSON format"""
import json
import requests
import sys
import urllib


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users/").json()
    dic = {}
    with open("todo_all_employees.json", "w") as alljsonfile:
        for user in users:
            todos = requests.get(url + "/users/{}/todos/".format(user.get("id"))).json()
            username = user.get("username")
            userId = user.get("id")
            tasks = []
            for task in todos:
                task_dic = {}
                task_dic["task"] = task.get("title")
                task_dic["completed"] = task.get("completed")
                task_dic["username"] = username
                tasks.append(task_dic)
            dic[userId] = tasks
        json.dump(dic, alljsonfile)
