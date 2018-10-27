#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: This function calculates heights of trees given distance of each tree 
# from its base and angle to its top, using  the trigonometric formula 


#clear environments
rm(list=ls())

# height = distance * tan(radians)
#
# ARGUMENTS
# degrees:   The angle of elevation of tree
# distance:  The distance from base of tree (e.g., meters)
#
# OUTPUT
# The heights of the tree, same units as "distance"

Data<-read.csv("../Data/trees.csv", header = TRUE)
Data<- read.table("../Data/trees.csv", sep = ",", header = TRUE)

TreeHeight <- function(degrees,distance) {
  radians<-degrees*pi/180
  height<-distance*tan(radians)
  
}

Tree.Height.m<-TreeHeight(Data$Angle.degrees,Data$Distance.m)
OutputData<- cbind(Data, Tree.Height.m)
write.csv(OutputData, "../Results/TreeHts.csv", row.names=TRUE) # write row names


