#!/bin/bash

a1='Dunaev Dmitriy'
a2=$(date '+today is %D')
#read -r v
for var in "$@"
do
    if [ $1 -eq 1 ] ; then echo $a1; exit 0;
    elif [ $1 -eq 2 ] ; then echo $a2; exit 0;
    else echo "please input 1 or 2"; exit 1;
    fi;
done
