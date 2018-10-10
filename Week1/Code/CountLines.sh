#!/bin/bash
NumLines=`wc -l < $1`
# Numlines is the total number of lines for $1 file
echo "The file $1 has $NumLines lines"
echo
