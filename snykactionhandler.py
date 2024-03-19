import os
import sys

action_handler_directory = os.environ['ACTION_HANDLER_DIR']
sys.path.append('../../snyk-github')
from snykgithubissue import create_github_issue

working_directory = os.environ['WORKING_DIR']
github_token = os.environ['GITHUB_TOKEN']
github_repo = os.environ['GITHUB_REPOSITORY']
github_api_url = 'https://api.github.com/repos/' + github_repo
snyk_file_name = '/vuln.json'

def main():
    create_github_issue
    
if __name__ == "__main__":
    main()