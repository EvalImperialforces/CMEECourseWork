#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: his script calculates heights of trees from a given .csv file and outputs
# the result in the following format; "InputFileName_treeheights.csv"


#clear environments
rm(list=ls())

# The height is calculated bu using the given distance of each tree from its base 
# and angle to its top, using  the trigonometric formula;
#
# height = distance * tan(radians)


args<-commandArgs(trailingOnly = TRUE) # Defines command line arguments as vector "args"
# By trailingOnly = TRUE, only input file in command line is called
Data<-read.csv(args[1]) # Read csv file
filename <- tools::file_path_sans_ext(args[1]) # establishes a file path without the file extention using tools package
filewithoutext <- basename(filename) # Stores the file without the pathway

#Alternative to commandArgs = would extract any *.csv but difficult to alter extention for output

#directory <- "../Data/"
#filenames <- list.files(directory, pattern = "*.csv", full.names = TRUE)
#Data<-read.csv(filenames, header = TRUE)
#Data<- read.table(filenames, sep = ",", header = TRUE)


TreeHeight <- function(degrees,distance) {
  radians<-degrees*pi/180
  height<-distance*tan(radians)
  print(paste("Tree height is:",height))
  
  return (height)
}

Height.m<-TreeHeight(Data$Angle.degrees,Data$Distance.m)

OutputData<- cbind(Data, Height.m) #adds column tree height to output file
new.file.name <- paste0("../Results/", filewithoutext, "_treeheights.csv")
# paste0 allows you to combine things without a seperator automatically 
write.csv(OutputData, file = new.file.name) # write row names

