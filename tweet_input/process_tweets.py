import json
import string

def clean_tweet(tweet_text):
    r=filter(lambda x: x in string.printable and x!='\n', tweet_text)
    clean_tweet=''.join(list(r))
    return{'clean_tweet':clean_tweet,'unicode':int(clean_tweet!=tweet_text)}

def clean_created_at(created_at):
    return '(timestamp: '+ created_at +')'

def output_file(list_of_tweets, count):
    with open('ft1.txt','w') as outfile:
        for tweet in list_of_tweets:
            outfile.write(tweet)
            outfile.write('\n')

        outfile.write(str(count)+' tweets contained unicode')


def open_and_process(filename):
    tweet_list=[]
    non_ascii_count=0

    with open(filename,'r') as tweets_file:
        tweets=json.load(tweets_file)
    
    for tweet in tweets:
        cleaned_tweet=clean_tweet(tweet['text'])
        tweet_list.append(cleaned_tweet['clean_tweet']+' '+clean_created_at(tweet['created_at']))
        non_ascii_count=non_ascii_count+cleaned_tweet['unicode']

    output_file(tweet_list,non_ascii_count)
    



if __name__ == "__main__":
    open_and_process('tweets.txt')
