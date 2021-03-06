import json
import string

############################## Globals ######################################
no_escape_ascii = string.printable[:-5]

################################ File Handling ################################ 
def output_file(list_of_tweets, uni_count, non_valid_count):
    with open('../tweet_output/ft1.txt', 'w') as outfile:
        for tweet in list_of_tweets:
            outfile.write(tweet)
            outfile.write('\n')
        outfile.write(
            str(non_valid_count) +
            ' tweets did not have a text field or created_at field\n')
        outfile.write(str(uni_count) + ' tweets contained unicode\n')


def input_file(filename):
    tweets = []
    with open(filename, 'r') as tweets_file:
        tweets = [x.strip('\n') for x in tweets_file.readlines()]
    return tweets


############################## Json Handling and Cleaning ####################
def clean_tweet(tweet_text):
    r = filter(lambda x: x in no_escape_ascii, tweet_text)
    clean_tweet = ''.join(list(r))
    return{'clean_tweet': clean_tweet, 'unicode': int(clean_tweet != tweet_text)}

def clean_created_at(created_at):
    return '(timestamp: ' + created_at + ')'

############################### Main Function ###############################
def open_and_process(filename):
    tweet_list = []
    non_ascii_count = 0
    non_valid_count = 0
    tweets = input_file(filename)

    for tweet in tweets:
        tweet = json.loads(tweet)
        if 'text' in tweet and 'created_at' in tweet:
            cleaned_tweet = clean_tweet(tweet['text'])
            to_add = cleaned_tweet['clean_tweet'] + ' ' + \
                clean_created_at(tweet['created_at'])
            tweet_list.append(to_add)
            non_ascii_count = non_ascii_count + cleaned_tweet['unicode']
        else:
            non_valid_count = non_valid_count + 1

    output_file(tweet_list, non_ascii_count, non_valid_count)

if __name__ == "__main__":
    open_and_process('../tweet_input/tweets3.txt')
