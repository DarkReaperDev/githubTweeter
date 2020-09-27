import urllib3
import json
import sys

TWITTER_API_KEY = ""
GITHUB_API_KEY = ""

GITHUB_REPO_OWNER_NAME = "DarkReaperDev"
GITHUB_REPO_NAME = "Code2UML"

def main():
    message = sys.argv[1]
    
    file = open("artifactsTest.txt", "a")
    
    file.write(message)
    file.write("\n")

    file.close()

main()