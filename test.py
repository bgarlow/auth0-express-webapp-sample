import os
import requests
import json

githubToken = os.environ['GITHUB_TOKEN']
githubApiUrl = "https://api.github.com/repos/bgarlow/auth0-express-webapp-sample/issues"

print("Running the python script test.py")
print("Endpoint URL: ", githubApiUrl)

with open("./vuln.json") as file:
    data = json.load(file)

print("data: ", data)

authHeaderValue = "Bearer " + githubToken

headers = {
    "Authorization": authHeaderValue,
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

issueBody = {
    "title": "This is an issue submitted by the python script",
    "body": "this is the body",
    "assignees": ["bgarlow"],
    "labels": ["bug"]
}

response = requests.post(githubApiUrl, headers=headers, json=issueBody)

print(response.text)