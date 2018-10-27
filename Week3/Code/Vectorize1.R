#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Vectorization example to compare the process time of vectors in comparison to loops.


#clear environments
rm(list=ls())

M<- matrix(runif(1000000),1000,1000)

SumALLELEMENTS <- function(M) {
  Dimensions <- dim(M)
  Tot<-0
  for (i in 1:Dimensions[1]){
    for (j in 1:Dimensions[2]){
      Tot<- Tot+M[i,j]
    }
  }
  return(Tot)
}

## This on my computer takes about 1 sec
print(system.time(SumALLELEMENTS(M)))
## While this takes about 0.01 sec
print(system.time(sum(M)))
