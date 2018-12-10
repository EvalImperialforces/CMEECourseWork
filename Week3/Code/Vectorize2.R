#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Modifing stochastic Ricker model to increase run time.

#clear environments
rm(list=ls())

# Runs the stochastic (with gaussian fluctuations) Ricker Eqn.


stochrick<-function(p0=runif(1000,.5,1.5),r=1.2,K=1,sigma=0.2,numyears=100)
{
  #initialize
  N<-matrix(NA,numyears,length(p0))
  N[1,]<-p0
  
#  for (pop in 1:length(p0)) #loop through the populations
  #{
# Removing the loop for populations runs the function through years, column by colummn, 
# as opposed to through years and populations, cell by cell.
  
    for (yr in 2:numyears) #for each pop, loop through the years
    {
      N[yr,]<-N[yr-1,]*exp(r*(1-N[yr-1,]/K)+rnorm(1,0,sigma))
    }
  #}
 return(N)

}

# Now write another function called stochrickvect that vectorizes the above 
# to the extent possible, with improved performance: 

#print("Vectorized Stochastic Ricker takes:")
#a = Sys.time()
#Sys.sleep(stochrick())
#b = Sys.time()    
#print(paste0(round(as.numeric(difftime(time1 = b, time2 = a, units = "secs")), 3), " seconds"))

result <- as.numeric(system.time(stochrick()))
cat(paste("The execution time for Vectorize2.R was", (result[3]), "\n"))
