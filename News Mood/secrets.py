import tweepy
power="AIzaSyDkw4qkSMPli1e_GO_l9FkvgngqreYM1SQ" #Google
lies="caa905e0f8b4acf6e690ad1876cbb8f7d98a94f9" #Census
future="544242d01c1bead586e510ac748fc6ca" #Openweathermap

#twitter
#consumer api key EdyWCQNqsi6DDuK0Y1wNVo33P
#consumer secret AcCJin1QVDsqlFN3PkR4eDoHunefZHaU5OZFSCo1vxQNSIxNnf
#access token 	773260063-eur6RZrpPdxnaazFOUEbdacKaWbY1Hq1whJUX80m
#access token secret Y5AuEVz2cI0HUwaH08q0aPJe1tHSwJkH7S9Gf4Cb2xkMh
consumer_key = "EdyWCQNqsi6DDuK0Y1wNVo33P"
consumer_secret = "AcCJin1QVDsqlFN3PkR4eDoHunefZHaU5OZFSCo1vxQNSIxNnf"
access_token = "773260063-eur6RZrpPdxnaazFOUEbdacKaWbY1Hq1whJUX80m"
access_token_secret = "Y5AuEVz2cI0HUwaH08q0aPJe1tHSwJkH7S9Gf4Cb2xkMh"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
chirp = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) #chirp is the var I want for twittering

def human(tweet):
    # "Real Person" Filters
    min_tweets = 5
    max_tweets = 10000
    max_followers = 2500
    max_following = 2500
    lang = "en"
    return(tweet["user"]["followers_count"] < max_followers and
        tweet["user"]["statuses_count"] > min_tweets and
        tweet["user"]["statuses_count"] < max_tweets and
        tweet["user"]["friends_count"] < max_following and
        tweet["user"]["lang"] == lang)