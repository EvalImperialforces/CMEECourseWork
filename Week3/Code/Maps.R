#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Mapping practical

### Mapping the 

#clear environments
rm(list=ls())

load("../Data/GPDDFiltered.RData")
head(gpdd)
library(maps)

map(database = "world")
points(y=gpdd$lat, x = gpdd$long, cex=1.9, col="red")

# Biases will appear in the data due to the nature of species being measured 
# which all appear to be based primarily in Europe and the USA. This could be due to species
# range or where time series data was collected. Outlying time series data in North East Asia and 
# South Africa will bias results if analysis involves compring species abundance and
# distribution on a global scale.