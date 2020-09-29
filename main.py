import urllib3
import json
import sys

def main():
    message = sys.argv[1][1:-1]
    TWITTER_API_KEY = sys.argv[2]
    TWITTER_API_KEY_SECRET = sys.argv[3]
    TWITTER_ACCESS_TOKEN = sys.argv[4]
    TWITTER_ACCESS_TOKEN_SECRET = sys.argv[5]
    
    file = open("artifactsTest.txt", "a")
    

    file.write(message)
    file.write("\n")    

    file.close()


    if "//tweet" in message.lower():
        

main()