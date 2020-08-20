#!/bin/bash
echo "Parse the location of the page source"
read pagesource

echo "Parse the location of the output"
read output

rm -rf ~/tmptxt
rm -rf ~/tmpmacro 
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
            echo "$var" >> $output
        fi
done <<< $(cat ~/tmptxt)

var=$(sed -n "1{p;q}" $output)
printf "VERSION BUILD=10021450\nSET !VAR1 EVAL(\"[" >> ~/tmpmacro

while read -r line;
do
    var="$var, $line"
done <<< $(cat "$output")
printf "$var" >> ~/tmpmacro

echo -e "][{{!LOOP}} - 1];\")\nWAIT SECONDS=3\nURL GOTO=https://m.facebook.com/{{!VAR1}}\nWAIT SECONDS=4\
\nTAG POS=1 TYPE=TEXTAREA FORM=ID:mbasic-composer-form ATTR=NAME:xc_message CONTENT=Hello<SP>I<SP>am<SP>\
200%<SP>not<SP>a<SP>robot\nWAIT SECONDS=3\nTAG POS=1 TYPE=INPUT:SUBMIT FORM=ID:mbasic-composer-form ATTR=\
NAME:view_post\nWAIT SECONDS=1" >> ~/tmpmacro

echo -e "\n'SET !LOOP {{!VAR1}}" >> ~/tmpmacro

rm -rf $output

mv ~/tmpmacro $output

