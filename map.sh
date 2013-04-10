rm -f ./tmp/*
num=1

for i in $(ls ./tweets/ );
do
    ((num++))
    if [ $((num % 100)) -eq 0 ]
    then
        echo $num
    fi
    cat ./tweets/$i | ./mapper.py > ./tmp/mapper-$i.txt ;
    if [ ! -s ./tmp/mapper-$i.txt ]
    then
        rm -f ./tmp/mapper-$i.txt
    fi
done
