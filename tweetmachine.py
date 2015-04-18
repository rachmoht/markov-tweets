import os
import twitter

from markov import MarkovMachine

import sys
corpus_filenames = sys.argv[1:]

generator = MarkovMachine()
generator.read_files(corpus_filenames)

# Use Python os.environ to get at environmental variables
#
# Note: you must run `source secrets.sh` before running this file
# to make sure these environmental variables are set.

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# This will print info about credentials to make sure they're correct
print api.VerifyCredentials()

# Send a tweet
status = api.PostUpdate(generator.make_text())
print status.text