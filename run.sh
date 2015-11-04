start=$SECONDS
currentFldr=$(pwd)/
cd $currentFldr/src
echo "Running Feature 1" 
python3 process_tweets.py
echo "Feature 1 Complete, Now beginning Feature 2"
python3 average_degree.py
echo "Feature 2 Complete"
duration=$(( SECONDS - start ))
echo Processes took about $duration seconds
