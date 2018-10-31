#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Wrangling the Pound Hill Dataset using dplyr and tidyr

#clear environments
rm(list=ls())

############# Load the dataset and packages ###############
# header = false because the raw data don't have real headers
MyData <- as.matrix(read.csv("../Data/PoundHillData.csv",header = F)) 

# header = true because we do have metadata headers
MyMetaData <- read.csv("../Data/PoundHillMetaData.csv",header = T, sep=";", stringsAsFactors = F)

library(tidyr)
library(dplyr)
############# Inspect the dataset ###############
head(MyData)
dplyr::glimpse(MyData)
dplyr::glimpse(MyMetaData)
utils::View(MyData)
############# Transpose ###############
# To get those species into columns and treatments into rows 

MyData <- t(MyData) # Swaps columns and rows
head(MyData)


############# Replace species absences with zeros ###############
MyData[MyData == ""] = 0

############# Convert raw matrix to data frame ###############

TempData <- as.data.frame(MyData[-1,],stringsAsFactors = F) #stringsAsFactors = F is important!
colnames(TempData) <- MyData[1,] # assign column names from original data

############# Convert from wide to long format  ###############


MyWrangledData<- TempData %>% gather(.,Species, Count, -Cultivation, -Block, -Plot, -Quadrat) %>% mutate(Cultivation = as.factor(Cultivation), Block=as.factor(Block), Plot = as.factor(Plot), Quadrat = as.factor(Quadrat))
utils::View(MyWrangledData)

############# Start exploring the data (extend the script below)!  ###############


