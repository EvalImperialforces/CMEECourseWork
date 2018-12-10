#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Vectorization example to compare the process time of vectors in comparison to loops.


#clear environments
rm(list=ls())

M <- matrix(runif(1000000),1000,1000)

SumALLELEMENTS <- function(M) {
  Dimensions <- dim(M)
  Tot<-0
  for (i in 1:Dimensions[1]){
    for (j in 1:Dimensions[2]){
      Tot <- Tot+ M[i,j]
    }
  }
  return(Tot)
}

## This on my computer takes about 1 sec
result <- as.numeric(system.time(SumALLELEMENTS(M)))
cat(paste("The execution time for Vectorize.1 R was", result[3], "\n"))

#a = Sys.time()
#Sys.sleep(SumALLELEMENTS(M))
#b = Sys.time()    
#print(paste0(round(as.numeric(difftime(time1 = b, time2 = a, units = "secs")), 3), " seconds"))
## While this takes about 0.01 sec
#print(system.time(sum(M)))
