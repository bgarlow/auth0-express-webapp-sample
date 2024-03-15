import os
import requests
import json

from snyksummary import buildSnykSummary

workingDirectory = os.environ['WORKING_DIR']
githubToken = os.environ['GITHUB_TOKEN']
githubApiUrl = "https://api.github.com/repos/bgarlow/auth0-express-webapp-sample/issues"

print("Running the python script test.py")
print("Endpoint URL: ", githubApiUrl)

jsonFilePath = workingDirectory + "/vuln.json"

with open(jsonFilePath) as file:
    data = json.load(file)

print("data: ", data)

authHeaderValue = "Bearer " + githubToken

headers = {
    "Authorization": authHeaderValue,
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}

summary = buildSnykSummary()

issueRequest = {
    "title": "This is an issue submitted by the python script",
    "body": summary,
    "assignees": ["bgarlow"],
    "labels": ["bug"]
}

print(issueRequest)

response = requests.post(githubApiUrl, headers=headers, json=issueRequest)

print(response.text)