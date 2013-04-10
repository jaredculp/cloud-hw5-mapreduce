#!/usr/bin/env python

from operator import itemgetter
import sys

current_date = None
current_who = None
current_count = 0
date = None
who = None

for line in sys.stdin:
    line = line.strip()

    # parse the input we got from mapper.py
    date, who, count = line.split('\t', 2)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_date == date and current_who == who:
        current_count += count
    else:
        if current_date and current_who:
            print '%s\t%s\t%s' % (current_date, current_who, current_count)
        current_count = count
        current_date = date
        current_who = who

# do not forget to output the last word if needed!
if current_date == date and current_who == who:
    print '%s\t%s\t%s' % (current_date, current_who, current_count)
