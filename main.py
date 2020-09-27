import urllib3
import json
import sys

def main():
    message = sys.argv[1][1:-1]
    
    file = open("artifactsTest.txt", "a")
    

    file.write(message)
    file.write("\n")
    

    file.close()

main()