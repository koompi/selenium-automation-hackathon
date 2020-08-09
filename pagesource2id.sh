#!/bin/bash

#!/bin/bash

echo "Parse the location of the page source"
read pagesource

echo "Parse the location of the output"
read output

rm -rf ~/tmptxt
rm -rf $output

while read -n1 char;
do

    printf "$char" >> ~/tmptxt

    if [[ "$char" == "," ]];
    then
        echo " " >> ~/tmptxt
    fi

done <<< $(cat $pagesource)


while read -r line;
do
        if [[ "${line:0:9}" == '"kwEntId"' ]];
        then
            var=$(echo "$line" | awk -F':' '{printf $2}' | sed s/.$// )
            echo $var >> $output
        fi
done <<< $(cat ~/tmptxt)