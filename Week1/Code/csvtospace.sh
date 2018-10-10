#!/bin/bash
#Author:eva.EL1718@imperial.ac.uk
#Script:csvtospace.sh
#Desc: substitute comma seperated values to space separated file with a new name.
#Date: Oct 2018

echo "Creating a space seperated version of $1.."
filename="${1//.csv/.txt}"
#filename removes .csv from $1 and replaces it with .txt
cat $1 | tr -s "," " " >> $filename
#cat reads $1 files in chosen directory 
#tr -s substitutes commas for spaces and outputs file under new name $1.txt"

echo "Done!"
