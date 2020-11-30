import base64
import os
from github import Github
from pprint import pprint
username = "amfoss"
g = Github()
user = g.get_organization(username)
for repo in user.get_repos():
    os.system("perceval git --json-line https://github.com/{} >> commits.json".format(repo.full_name))
