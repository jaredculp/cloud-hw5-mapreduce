#!/usr/bin/env python

# Alex Hutcheson (amh4bm)
# Jared Culp (jjc4fb)
# CS 4501 - HW5 prelim

import sys
import json

# set up a dictionary of sentiment words
lookup_words = {
    'pos': {},
    'neg': {}
}

counts_pos = 0
counts_neg = 0

# read in positive words
positive_file = open('positive.txt', 'r')
for line in positive_file:
    lookup_words['pos'][line.strip()] = 1
positive_file.close

# read in negative words
negative_file = open('negative.txt', 'r')
for line in negative_file:
    lookup_words['neg'][line.strip()] = 1
negative_file.close

# we only need the tweet and the date
raw = json.load(sys.stdin)
date = raw["created_at"]
date = date.split()
date = date[1] + " " + date[2]
tweet = raw["text"].encode('utf-8') # remove unicode warning

words = tweet.split()

# keep track of who is mentioned more in this tweet
is_sully = 0
is_dragas = 0

for word in words:
    word = word.lower()
    if word == 'sullivan':
        is_sully = is_sully + 1
    elif word == 'dragas':
        is_dragas = is_dragas + 1

    if word in lookup_words['pos']:
        counts_pos = counts_pos + 1
    elif word in lookup_words['neg']:
        counts_neg = counts_neg + 1
if (counts_pos - counts_neg) == 0:
    pass
elif (is_dragas + is_sully) == 0: # do nothing if neither are mentioned
    pass
elif is_dragas > is_sully:
    print '%s\td\t%d' % (date, counts_pos - counts_neg)
else:
    print '%s\ts\t%d' % (date, counts_pos - counts_neg)
