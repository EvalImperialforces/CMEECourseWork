#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: A boilerplate R script 

#clear environments
rm(list=ls())

MyFunction<- function(Arg1, Arg2){
  
  # Statements involving Arg1, Arg2: 
  print(paste("Argument", as.character(Arg1),"is a", class(Arg1)))
  print(paste("Argument", as.character(Arg2),"is a", class(Arg2)))
  
  return(c(Arg1, Arg2)) #optional but very useful
  
}

MyFunction(1,2) #Test function
MyFunction("Riki", "Tiki") #Different test

