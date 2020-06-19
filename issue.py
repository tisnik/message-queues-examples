import os
import sys
import requests
import json

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = "tisnik"
TOKEN = "22ac53f5751e4c9a41835e2fa14d95272ee3412f"

# The repository to add this issue to
REPO_OWNER = "tisnik"
REPO_NAME = "message-queues-examples"

def make_github_issue(title, body=None, created_at=None, closed_at=None, updated_at=None, assignee=None, milestone=None, closed=None, labels=None):
    # Create an issue on github.com using the given parameters
    # Url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/import/issues' % (REPO_OWNER, REPO_NAME)
    
    # Headers
    headers = {
        "Authorization": "token %s" % TOKEN,
        "Accept": "application/vnd.github.golden-comet-preview+json"
    }
    
    # Create our issue
    data = {'issue': {'title': title,
                      'body': body,
                      'created_at': created_at,
                      'assignee': assignee}}

    payload = json.dumps(data)

    # Add the issue to our repository
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 202:
        print('Successfully created Issue "%s"' % title)
    else:
        print('Could not create Issue "%s"' % title)
        print('Response:', response.content)

title = 'Pretty title'
body = 'Beautiful body'
created_at = "2020-06-18T12:55:00Z"
assignee = 'tisnik'

make_github_issue(title="", body="", created_at=created_at, assignee=assignee)
