import urllib3
import json
import sys

TWITTER_API_KEY = ""

def main():
    message = sys.argv[1][1:-1]
    
    file = open("artifactsTest.txt", "a")
    

    file.write(message)
    file.write("\n")

    file.close()

main()