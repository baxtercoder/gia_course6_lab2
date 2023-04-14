#!/usr/bin/env python3
import os
import requests


# capture list of files:
files = os.listdir('/data/feedback')

# function to read file lines into list:
def readlines(file):
    with open('/data/feedback/' + file) as f:
        lines = f.read().splitlines()
    return lines


# load feedback entries into dictionary:
feedback = []
keys = ["title", "name", "date", "feedback"]
for file in files:
    lines = readlines(file)
    feedback.append(dict(zip(keys, lines)))

# set host url:
url = "http://localhost/feedback/"

# post feedback entries:
for entry in feedback:
    response = requests.post(url, data=entry)
    if response.ok:
        print("loaded entry")
    else:
        print(f"load entry error: {response.status_code}")
