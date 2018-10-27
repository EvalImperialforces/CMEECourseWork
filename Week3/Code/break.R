#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Example script to demonstrate breaking out of loops.

#clear environments
rm(list=ls())
i <- 0 #Initialize i
  while(i < Inf) {
    if (i == 20) {
      break 
  } # Break out of the while loop! 
  else { 
    cat("i equals " , i , " \n")
    i <- i + 1 # Update i
  }
}
