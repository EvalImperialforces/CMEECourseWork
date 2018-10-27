#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Autocorrelation in weather

### Calculating the correlation of mean temperatures in Key West, Florida for successive years in the 20th century

#clear environments
rm(list=ls())

# Analyze our data
load("../Data/KeyWestAnnualMeanTemperature.RData")
head(ats) # Display first 6 rows of data
Key<-ats 
scatter.smooth(Key) # Scatter plot with line of best fit
summary(Key$Temp)
Temp<-Key$Temp
Year<-Key$Year

# Align temperature data between successive years to compare 
t1<-Key[1:99,2]
t2<-Key[2:100,2]

Corr_successive_years<-cor(t1,t2)
Corr_successive_years

# Repeat function
tf<-function(t1,t2){
  t1<-sample(t1,size = length(t1),replace = TRUE)
  t2<-sample(t2,size = length(t2),replace=TRUE)
  return(cor(t1,t2))
}
# Randomize the alignment of t1 and t2 subsets, correlate these random alignments
  
result<-sapply(1:10000, function(i) tf(t1,t2))
# Run the t1 and t2 subsets through this function 10000 times

output<-result>Corr_successive_years
# Assign output variable to the number of cases in which randomly
# permuted time series correlations were greater than that of the correlation
# between successive years.
Fraction<-1-(length(output[output==FALSE])/length(result))
# The fraction of random correlations greater than that of successive years
# Length of cases in which random correlations were greater than successive
# years compared to length of all random correlations minus 1
Fraction #print

#Few correlations greater than ours, weak correlation but significant beacuse
#compared to a distribution of randomized permeated etc.
# our value explains it better, our value is different from random

# Interpret results
library(ggplot2)
hist(result,main=NULL,xlab = "Correlation_Result") 
abline(v=Corr_successive_years, col="blue")

