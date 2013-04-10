#!/bin/bash

cat ./tmp/* > ./tmp/concat.txt
./reducer.py < ./tmp/concat.txt > ./output.txt
