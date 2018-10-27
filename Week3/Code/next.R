#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Example script to demonstrate skip iterations out of loops.

#clear environments
rm(list=ls())

for (i in 1:100){
  if ((i%%2)==0)
    next # pass to next iteration of loop
  print (i)
}