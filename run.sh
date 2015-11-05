#!/bin/bash
# This script runs the Insight Data Engineering Code Challenge
# Outputs are found in the tweet_output file in ft1.txt and ft2.txt
  
#Preliminary prepartion- start timer, remove old txt files

start=$SECONDS
currentFldr=$(pwd)/
cd $currentFldr/tweet_output
rm ft2.txt
cd $currentFldr/src


# Run Feature 1
echo "Running Feature 1" 
python3 process_tweets.py

#Run Feature 2
echo "Feature 1 Complete, Now beginning Feature 2"
python3 average_degree.py
echo "Feature 2 Complete"

# Calculation of duration of processes 
duration=$(( SECONDS - start ))
echo Processes took about $duration seconds
