#!/usr/bin/python3
"""Export data in CSV format"""
import urllib
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/users/{}/todos/".format(sys.argv[1])).json()
    username = user.get("name")
    with open("{}.csv".format(sys.argv[1]), "w", encoding="UTF8",
              newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            task_status = task.get("completed")
            task_title = task.get("title")
            writer.writerow([sys.argv[1], username, task_status, task_title])
