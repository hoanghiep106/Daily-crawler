# Dependencies
install Redis: https://redis.io/topics/quickstart

sudo pip install -r requirements.txt

# How to run the project

1. Bootstrap tweetf0rm

    $ ./bootstrap.sh -c config.json -p proxies.json

2. Start redis server

    $ redis-server
3. Run script the first time

    sh client.sh -c config.json -cmd SEARCH -q="Gold Coast" -si=[LAST_TWEET_ID]

4. Activate daily crawler

    $ python shedule.py