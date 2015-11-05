#Insight Data Engineering Code Challenge
-Execute by running the script run.sh

-Main files were coded and tested in Python 3.4.3.

-Python Libraries used include standard library time, json, itertools, re and string. Networkx library 1.9 for python 3 was also used which is not in the standard library

-Code challenge feature 1 is handled by process_tweets.py and feature 2 is handled by average_degree.py. Both files read from tweet2.txt or tweet3.txt which follow the formatting specified in the code challenge summary.

-In the tweets.txt test file provided there were situations where the 'text' field or the 'created_at' field was not specified in a json dictionary. If either fields were missing, the tweets were counted to be invalid and were simply discarded. We account for these invalid json dictionaries in process_tweets.py by noting them in bottom of ft1.txt. 

-The file average_degree_version2.py runs almost identically to the original. However, it does not discard tweets with missing 'text' OR missing 'created_at' fields. It checks if the 'created_at' field exists and removes nodes from the graph based off the time stamp regardless of whether the 'text' field in the json exists. This is not the default file used in run.sh. Please modify run.sh if you choose to execute this version.



