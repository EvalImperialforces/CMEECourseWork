#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Example script to run a simulation that involves sampling from a population.

#clear environments
rm(list=ls())

x<-rnorm(50) #Generate population
doit<- function(x){
    x<-sample(x,replace = TRUE)
    if(length(unique(x))>30) {#only take mean if data is sufficient
        print(paste("Mean of this sample was:", as.character(mean(x))))
    }
}

## Run 100 iterations using vectorization:
result<- lapply(1:100, function(i) doit(x))

## Or using a for loop:
result<-vector("list",100) #Initialize
for(i in 1:100){
  result[[i]]<-doit(x)
}


