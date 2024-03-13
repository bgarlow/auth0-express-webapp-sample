import os
import requests 

print("Running the python script");

githubToken = os.environ['GITHUB_TOKEN']
githubApiUrl = "https://api.github.com/repos/bgarlow/auth0-express-webapp-sample/issues"

issueBody = {
    "title": "This is an issue submitted by the python script",
    "body": "this is the body",
    "assignees": ["bgarlow"],
    "labels": ["bug"]
}

response = requests.post(githubApiUrl, issueBody)

print(response.text)