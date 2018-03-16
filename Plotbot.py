
# coding: utf-8

# 
# The bot receives tweets via mentions and in turn performs sentiment analysis on the most recent twitter account specified in the mention
# 
# For example, when a user tweets, "@PlotBot Analyze: @CNN," it will trigger a sentiment analysis on the CNN twitter feed.
# 
# A plot from the sentiment analysis is then tweeted to the PlotBot5 twitter feed.
# 
# Hints, requirements, and considerations:
# 
# Your bot should scan your account every five minutes for mentions.
# Your bot should pull 500 most recent tweets to analyze for each incoming request.
# Your script should prevent abuse by analyzing only Twitter accounts that have not previously been analyzed.
# Your plot should include meaningful legend and labels.
# It should also mention the Twitter account name of the requesting user.
# When submitting your assignment, be sure to have at least three analyses tweeted out from your account (enlist the help of classmates, friends, or family, if necessary!).
# Notable libraries used to complete this application include: Matplotlib, Pandas, Tweepy, TextBlob, and Seaborn.

# In[1]:


# Dependencies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import seaborn as sns
import tweepy
import time
import datetime

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
chirp = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Deal with sentiments
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


# In[2]:


def pull_tweets(account):
    '''
    INPUT: String: Twitter Account Name
    OUTPUT: Panda's DataFrame: "Ago" tweets ago "Compound" vader compound score
    '''
    sentiments = []
    counter = -1
    for x in range(25):
        public_tweets = chirp.user_timeline(account, page=x)
        for tweet in public_tweets:
            result = analyzer.polarity_scores(tweet["text"])
            sentiments.append({
                "Ago": counter,
                "Compound": result["compound"],
                "User": account
            })
            counter -= 1
    df = pd.DataFrame(sentiments)
    return(df)


# In[18]:


def the_work(analyzed=[], last_check=None, own_account="GunmaKuma"):
    now = datetime.datetime.now()
    str_now = str(now)
    str_now = str_now[:10]
    sweep = chirp.home_timeline(since_id=last_check)
    users = []
    for tweet in sweep:
        request_user = tweet["user"]["screen_name"]
        last_check = int(tweet["id_str"])
        try:
            first_at = tweet["entities"]["user_mentions"][0]["screen_name"]
            second_at = tweet["entities"]["user_mentions"][1]["screen_name"]
            if((first_at == own_account) and (second_at not in analyzed)):
                df = pull_tweets(second_at)
                plt.figure(figsize=(10,7))
                sns.set()
                plt.plot(df["Ago"], df["Compound"], "bo-", label=f"@{df['User'][0]}", alpha=0.7)
                plt.legend(loc=(1,.95))
                plt.xlabel("Tweets Ago")
                plt.ylabel("Tweet Polarity")
                plt.xlim(-len(df["Ago"]) - 5, 5)
                plt.ylim(-1.01, 1.01)
                plt.title(f"Sentiment Analysis of Tweets ({str_now})")
                plt.savefig(f"{second_at}.png")
                plt.close()
                chirp.update_with_media(f"{second_at}.png", f"Tweet Analysis of @{second_at} (You're welcome, @{request_user})")
                analyzed.append(second_at)
                print("Tweeted, sir!")
        except tweepy.TweepError:
            print("Something's up with twitter..." + e.reason)
        except:
            print("Nothing to do")


# In[ ]:


analyzed = []
while True:
    try:
        the_work(analyzed)
    except tweepy.RateLimitError:
        time.sleep(60 * 15)
        continue
    time.sleep(60 * 5)

