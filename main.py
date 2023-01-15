import os
import re
from actions_toolkit.github import Context

context = Context()

PK = os.environ.get("INPUT_PROJECT_KEY")


def getRegex():
    if PK is not None:
        return r'^{PK}-\d+:? +\S'
    return r'^[A-Z]+-\d+:? +\S'


def checkTitle(title):
    regex = getRegex()
    print(regex)
    if re.search(regex, title) is None :
        print("Bad Title")
        exit(1)

    print("Title is Ok")


if __name__ == "__main__":
    pull_request = context.payload.get("pull_request")
    if pull_request is None or pull_request.get("title") is None :
        print("This action should only be run with Pull Request Events")
        exit(1)
    print("Starting PR Title check for Jira Issue Key")
    title = pull_request.get("title")
    checkTitle(title)
