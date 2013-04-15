rm -f ./tmp/*
num=1

for i in $(ls ./tweets/ );
do
    ((num++))
    if [ $((num % 100)) -eq 0 ]
    then
        echo $num
    fi
    cat ./tweets/$i | ./$1 > ./tmp/$1-$i.txt ;
    if [ ! -s ./tmp/$1-$i.txt ]
    then
        rm -f ./tmp/$1-$i.txt
    fi
done
