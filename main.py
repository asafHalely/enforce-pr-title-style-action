import os
import re
from actions_toolkit.github import Context

context = Context()

PK = os.environ.get("INPUT_PROJECT_KEY")

def getRegex():
    if PK != None:
        return "^{PK}-\d+:? +\S"
    return "^[A-Z]+-\d+:? +\S"

def checkTitle():
    regex = getRegex()
    print(regex)
    if re.search(regex, title) == None :
        print("Bad Title")
        exit(1)
        
    print("Title is Ok")

if __name__ == "__main__":
    if context.payload.get("pull_request") == None or context.payload.get("pull_request").get("title") == None :
        print(f"This action should only be run with Pull Request Events")
        exit(1)
    print(f"Starting PR Title check for Jira Issue Key")
    title = context.payload.get("pull_request").get("title")
    print(title)



# async function run() {
#     try {
#         if (!regex.test(title)) {
#             core.debug(`Regex ${regex} failed with title ${title}`);
#             core.info("Title Failed");
#             core.setFailed("PullRequest title does not start with a Jira Issue key.");
#             return;
#         }
#         core.info("Title Passed");

#     } catch (error: any) {
#         core.setFailed(error.message);
#     }
# }

# export function getRegex() {
#     let regex = /(?<=^|[a-z]\-|[\s\p{Punct}&&[^\-]])([A-Z][A-Z0-9_]*-\d+)(?![^\W_])(\s)+(.)+/;
#     const projectKey = core.getInput("projectKey", { required: false });
#     if (projectKey && projectKey !== "") {
#         core.debug(`Project Key ${projectKey}`);
#         if (!/(?<=^|[a-z]\-|[\s\p{Punct}&&[^\-]])([A-Z][A-Z0-9_]*)/.test(projectKey)) {
#             throw new Error(`Project Key  "${projectKey}" is invalid`)
#         }
#         regex = new RegExp(`(^${projectKey}-){1}(\\d+):?(\\s+)(.+)`);
        
#     }
#     return regex;
# }

# run()