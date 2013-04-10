#!/usr/bin/env python

# Alex Hutcheson (amh4bm)
# Jared Culp (jjc4fb)
# CS 4501 - HW5 prelim

from operator import itemgetter
import sys

current_date = None
current_who = None
d_count = 0
s_count = 0
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
    if current_date == date:
        if who == "d":
            d_count += count
        if who == "s":
            s_count += count
    else:
        if current_date:
            print '%s\td\t%s' % (current_date, d_count)
            print '%s\ts\t%s' % (current_date, s_count)
        if who == "d":
            d_count = count
        if who == "s":
            s_count = count
        current_date = date
        current_who = who

# do not forget to output the last word if needed!
if current_date == date:
    if current_who == "d":
        print '%s\td\t%s' % (current_date, d_count)
    if current_who == "s":
        print '%s\ts\t%s' % (current_date, s_count)
