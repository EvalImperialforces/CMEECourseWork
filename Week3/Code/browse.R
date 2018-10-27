#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Exampe script to demonstrate debugging using browser() function.

#clear environments
rm(list=ls())

Exponential<-function(N0=1,r=1, generations=10){
  # Runs a simulation of exponential growth
  # Returns a vector of generation length
  
  N<-rep(NA, generations)
  
  N[1]<-N0
  for(t in 2:generations){
    N[t]<-N[t-1]*exp(r)
    browser()
  }
  return(N)
}

plot(Exponential(), type = "l", main = "Exponential growth")
