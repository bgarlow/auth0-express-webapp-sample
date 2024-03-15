def buildIssueBlock(issue):
    #TODO: add introduced through and fix lines to body of issue?
    #TODO: add module info to body of issue
    id = issue["id"]
    title = issue["title"]
    version = issue["version"]
    module = issue["module"]
    issueBlock = "ID: " + id + " Title: " + title + " Version: " + version
    return issueBlock

def buildSnykSummary(data):
    summary = ""
    issues = data["vulnerabilities"]
    numIssues = len(issues)
    print("number of vulnerabiilties: ", numIssues)

    if numIssues > 0: 
        for issueData in issues:
            issueBlock = buildIssueBlock(issueData)
            summary += issueBlock + "\n"       
    
    #summary = summary[0:-2]
    return summary
