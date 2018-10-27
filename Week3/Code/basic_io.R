#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: A simple script to illustrate R input - output.

#clear environments
rm(list=ls())
# Run line by line and check inputs/outputs to understand what is happening

MyData <- read.csv("../Data/trees.csv", header = TRUE) # Import with headers

write.csv(MyData, "../Results/MyData.csv") # Write it out as a new file

write.table(MyData[1,],file = "../Results/MyData.csv", append=TRUE) # Append to file

write.csv(MyData, "../Results/MyData.csv", row.names=TRUE) # write row names

write.table(MyData, "../Results/MyData.csv", col.names=FALSE) # ignore column names
