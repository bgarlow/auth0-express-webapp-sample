import os
import requests
import json

from localSnykSummary import buildSnykSummary

jsonFilePath = './vuln.json'

with open(jsonFilePath) as file:
        data = json.load(file)

summary = buildSnykSummary(data)

print(summary)

