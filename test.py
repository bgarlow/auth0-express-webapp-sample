import os
import requests 

githubToken = os.environ['GITHUB_TOKEN']
githubApiUrl = "https://api.github.com/repos/bgarlow/auth0-express-webapp-sample/issues"

print("Running the python script test.py")
print("Endpoint URL: ", githubApiUrl)

issueBody = {
    "title": "This is an issue submitted by the python script",
    "body": "this is the body",
    "assignees": ["bgarlow"],
    "labels": ["bug"]
}

response = requests.post(githubApiUrl, issueBody)

print(response.text)