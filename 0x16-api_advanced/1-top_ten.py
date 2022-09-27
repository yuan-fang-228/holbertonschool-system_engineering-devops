#!/usr/bin/python3
"""query REDDIT API and returns the top 10 posts of given subreddit"""
import requests


def top_ten(subreddit):
    """prints the titles of first 10 hot posts for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
               "User-Agent":
               "ubuntu4.20:0x16-api:v1.0.0 (by /u/yuan_fang_228)"
              }
    try:
        response = requests.get(url,
                                headers=headers,
                                allow_redirects=False).json()
        posts = response["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    except Exception:
        print("None")
