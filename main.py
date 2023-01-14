import os
from actions_toolkit.github import Context

context = Context()

# PK = os.environ["projectKey"]
# REPO = os.getenv("INPUT_REPO") or os.getenv("GITHUB_REPOSITORY")

# artifacts_url = f"https://api.github.com/repos/{REPO}/actions/artifacts"
# headers = {
#     "Authorization": f"token {TOKEN}",
#     "User-Agent": "Python",
# }

def getRegex():
    # if PK != None:
    #     return "(^${projectKey}-){1}(\\d+):?(\\s+)(.+)"
    return "/(?<=^|[a-z]\-|[\s\p{Punct}&&[^\-]])([A-Z][A-Z0-9_]*-\d+)(?![^\W_])(\s)+(.)+/"

if __name__ == "__main__":
    print(f"Starting PR Title check for Jira Issue Key")
    print(context.payload.pull_request)
    print(context.payload.pull_request.title)
    if context.payload.pull_request == None or context.payload.pull_request.title == None :
        print(f"This action should only be run with Pull Request Events")
        exit(1)
    title = context.payload.pull_request.title
    print(title)








# def get_artifact_id(branch):
#     artifacts_url = f"https://api.github.com/repos/{OWNER}/{REPO}/actions/artifacts?per_page=100"
#     r = requests.get(artifacts_url, headers=headers)
#     j = json.loads(r.content)
#     if not r.ok:
#         print(f"Faild to find artifacts. Please make sure that you have the correct tocken repo and owner")
#         exit(1)

#     for artifact in j['artifacts']:
#         if artifact["workflow_run"]["head_branch"] == branch and artifact["name"] == ARTIFACT_NAME:
#             return artifact["archive_download_url"]

#     print(f"Could not find the requested artifact: {ARTIFACT_NAME}") # TODO change error
#     exit(1)

# def get_branch_name():
#     if BRANCH == "main":
#         return BRANCH
#     else:
#         check_branch_url = f"https://api.github.com/repos/{OWNER}/{REPO}/branches/{BRANCH}"
#         r = requests.get(check_branch_url, headers=headers)

#         if r.ok:
#             return BRANCH
#         else:
#             print(f"Cant find branch: {BRANCH} falling back to main")
#             return "main"

# def download_artifact():
#     branch = get_branch_name()
    
#     archive_download_url = get_artifact_id(branch)

#     with requests.get(archive_download_url, headers=headers, stream=True) as r:
#         with open(NEW_ARTIFACT_NAME, "wb") as f:
#             shutil.copyfileobj(r.raw, f)
#             print(f"Artifact downloaded: {ARTIFACT_NAME}")















# async function run() {
#     try {
#         const regex = getRegex();

#         core.debug(title);
#         core.debug(regex.toString());

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