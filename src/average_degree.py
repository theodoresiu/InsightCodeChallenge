from time import strptime, mktime
from itertools import combinations
from re import findall
import networkx as nx
import json
import timeit


########################### File Handling #################################
def input_file(in_filename):
    with open(in_filename, 'r') as tweets_file:
        tweets = [x.strip('\n') for x in tweets_file.readlines()]
    return tweets


def output_file(out_filename):
    with open(out_filename, 'a') as outfile:
        avg_degree = round(get_average_degree(G), 2)
        outfile.write(str(avg_degree) + '\n')

##########################Json Handling ###################################

def extract_hashtags(text):
    hashtags = findall(r'#\w*', text.lower())
    return list(combinations(hashtags, 2))

def extract_time(ti):
    return mktime(strptime(ti, "%a %b %d %H:%M:%S +0000 %Y"))

######################### Graph Functions ################################
def remove_outdated(G, current_time):
    for edge in G.edges(data=True):
        if (current_time - edge[2]['created_at']) > 60:
            G.remove_edge(*edge[:2])

    return G

def get_average_degree(G):
    if len(G) == 0:
        return 0
    else:
        s = sum(G.degree(G.nodes()).values())
        return s / len(G)

########################## Main Functions ###################################

def update_graph(G, hash_bundle):
    for tweet in hash_bundle:
        G.add_edges_from(
            tweet['hashtags'], {
                'created_at': tweet['created_at']})
        G = remove_outdated(G, tweet['created_at'])
        output_file('../tweet_output/ft2.txt')
    return G

def read_file(filename):
    hash_bundle = []
    tweets = input_file(filename)

    for tweet in tweets:
        tweet = json.loads(tweet)
        if 'text' in tweet and 'created_at' in tweet:
            tweet_dic = {}
            tweet_dic['hashtags'] = extract_hashtags(tweet['text'])
            tweet_dic['created_at'] = extract_time(tweet['created_at'])
            hash_bundle.append(tweet_dic)

    return hash_bundle

if __name__ == "__main__":
    G = nx.Graph()
    hash_bundle=read_file('../tweet_input/tweets3.txt')
    G = update_graph(G, hash_bundle)
