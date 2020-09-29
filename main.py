import sys
import tweepy

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

        auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
        )

        auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
        )

        api = tweepy.API(auth)

        message.replace("//Tweet", "")
        message.replace("//tweet", "")

        tweet = message

        status = api.update_status(status=tweet) 
        

main()