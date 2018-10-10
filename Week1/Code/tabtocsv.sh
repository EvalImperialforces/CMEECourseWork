#!/bin/bash
#Author: eva.eval2496@gmail.com
#Script: tabtocsv.sh
#Desc: substitute the tabs in the files with commas saves the output into a .csv file
#Arguments: l-> tab delimited file
#Date: Oct 2018
echo "Creating a comma delimited version of $1..."
cat $1 | tr -s "\t""," >> $1.csv
echo "Done!"
exit