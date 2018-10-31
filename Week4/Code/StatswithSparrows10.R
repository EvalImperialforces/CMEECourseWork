#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Generating linear models using the sparrow data set

#clear environments
rm(list=ls())

d<-read.table("~/Documents/Week4_Stats/HandOutsandData'18/SparrowSize.txt", header=TRUE)

plot(d$Mass~d$Tarsus, ylab="Mass (g)", xlab="Tarsus Length (mm)", pch=18, cex=0.6)

# Plotting a line
x<-c(1:100)
b<-0.5
m<-1.5
y<-m*x+b
plot(x,y,xlim=c(0,100), ylim = c(0,100), pch=16, cex=0.5)

plot(d$Mass~d$Tarsus, ylab="Mass  (g)",  xlab="Tarsus  (mm)",  pch=19,  cex=0.4, ylim=c(-5,38),  xlim=c(0,22))
plot(d$Mass~d$Tarsus,  ylab="Mass  (g)",  xlab="Tarsus  (mm)",  pch=19,  cex=0.4) 	

d1<-subset(d,  d$Mass!="NA") 	
d2<-subset(d1,  d1$Tarsus!="NA") 	
length(d2$Tarsus) 	

model1<-lm(Mass~Tarsus, data=d2)
summary(model1)
hist(model1$residuals) 	
head(model1$residuals)
