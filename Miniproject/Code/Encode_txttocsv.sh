#!/bin/bash
#Author: eva.eval2496@gmail.com
#Script: tabtocsv.sh
#Desc: Change encoding and save as a .csv file
#Arguments: l-> tab delimited file
#Date: Oct 2018

echo "Check file encoding"
file -i $1

echo "Change to utf-8 encoding"
nn="../Data/$(basename "$1" .txt)_UTF8.csv"
iconv -f UTF-16LE -t UTF-8 $1 -o $nn

exit