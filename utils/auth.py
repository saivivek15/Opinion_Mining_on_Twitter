import twitter

''' authentication to access twitter api'''

def access():
    consumer_key=''
    consumer_secret=''
    access_key =''
    access_secret=''
    my_auth = twitter.oauth.OAuth(access_key,access_secret,consumer_key,consumer_secret)
    twitter_api = twitter.Twitter(auth=my_auth)
    return twitter_api

