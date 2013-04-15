#!/bin/bash

rm -f ./dragas.dat
rm -f ./sullivan.dat

while IFS=$'\t': read date who count
do
    if [ $who == "d" ];
    then
        echo -n `date -d "$date" +%Y%m%d` >> ./dragas.dat
        echo -n -e " $count\n" >> ./dragas.dat
    fi
    if [ $who == "s" ];
    then
        echo -n `date -d "$date" +%Y%m%d` >> ./sullivan.dat
        echo -n -e " $count\n" >> ./sullivan.dat
    fi
done < ./output.txt
