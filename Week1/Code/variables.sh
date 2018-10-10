#!/bin/bash
#Author:eva.EL1718@imperial.ac.uk
#Script: variables.sh
#Desc: Variables in shell scripts.
#Date: Oct 2018

#Show the use of variables
MyVar='some string'
echo 'the current value of the string is' $MyVar
echo 'Please enter a new string'
read MyVar
echo 'the current value of the variable is' $MyVar

##Reading multiple values
echo 'Enter two numbers seperated by spaces (s)'
read a b
echo 'you entered' $a 'and' $b '. Their sum is:'
mysum=`expr $a + $b`
echo $mysum