import os
import requests
import json

jsonFilePath = './vuln.json'

def buildIssueBlock(issue):
    id = issue["id"]
    title = issue["title"]
    version = issue["version"]
    issueBlock = "ID: " + id + " Title: " + title + " Version: " + version
    return issueBlock

def buildSnykSummary():
    summary = ""
    with open(jsonFilePath) as file:
        data = json.load(file)

    issues = data["vulnerabilities"]

    numIssues = len(issues)
    print("number of vulnerabiilties: ", numIssues)

    if numIssues > 0: 
        for issueData in issues:
            issueBlock = buildIssueBlock(issueData)
            summary += issueBlock + "/n"

    return summary
