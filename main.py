import urllib3
import json
import sys

TWITTER_API_KEY = ""
GITHUB_API_KEY = ""

GITHUB_REPO_OWNER_NAME = "DarkReaperDev"
GITHUB_REPO_NAME = "Code2UML"

def main():
    argv = sys.argv
    
    file = open("artifactsTest.txt", "a")
    
    for var in argv[1]:
        file.write(var)
        file.write("\n")

    file.write("end")

    file.close()

main()