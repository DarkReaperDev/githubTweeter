import urllib3
import json

TWITTER_API_KEY = ""
GITHUB_API_KEY = ""

GITHUB_REPO_OWNER_NAME = "DarkReaperDev"
GITHUB_REPO_NAME = "Code2UML"

def main():
    http = urllib3.PoolManager()
    result = http.request("GET", "https://api.github.com/repos/" + GITHUB_REPO_OWNER_NAME + "/" + GITHUB_REPO_NAME + "/events")
    print(result.data)
    jsonResult = json.loads(result.data)
    print(jsonResult)



main()