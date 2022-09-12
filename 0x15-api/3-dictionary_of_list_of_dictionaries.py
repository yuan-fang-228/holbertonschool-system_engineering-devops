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
            userId = user.get("id")
            todo = requests.get(url + "/users/{}/todos/".format(userId)).json()
            username = user.get("username")
            tasks = []
            for task in todo:
                task_dic = {}
                task_dic["task"] = task.get("title")
                task_dic["completed"] = task.get("completed")
                task_dic["username"] = username
                tasks.append(task_dic)
            dic[userId] = tasks
        json.dump(dic, alljsonfile)
