#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Script to calculate height of trees from a given .csv file and output
# the result in the following format; "InputFileName_treeheights.csv"

#clear environments
rm(list=ls())

# The height is calculated bu using the given distance of each tree from its base 
# and angle to its top, using  the trigonometric formula;
#
# height = distance * tan(radians)
#

directory <- "../Data/"
filenames <- list.files(directory, pattern = "*.csv", full.names = TRUE)
Data<-read.csv(filenames, header = TRUE)
Data<- read.table(filenames, sep = ",", header = TRUE)

TreeHeight <- function(degrees,distance) {
  radians<-degrees*pi/180
  height<-distance*tan(radians)
  print(paste("Tree height is:",height))
  
  return (height)
}

Height.m<-TreeHeight(Data$Angle.degrees,Data$Distance.m)
OutputData<- cbind(Data, Height.m)
write.csv(OutputData, "../Results/TreeHts2.csv", row.names=TRUE) # write row names
