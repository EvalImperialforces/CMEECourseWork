##!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Allometry in-class exercise

#clear environments
rm(list=ls())
graphics.off()
library("ggplot2")
library(repr)
require("minpack.lm")

powMod<-function(x,a,b) {
  return(a*x^b)
}
MyData<-read.csv("../Data/GenomeSize.csv")
head(MyData)

Data2Fit<- subset(MyData, Suborder == "Anisoptera")
Data2Fit<- Data2Fit[!is.na(Data2Fit$TotalLength),]
plot(Data2Fit$TotalLength, Data2Fit$BodyWeight)
ggplot(Data2Fit, aes(x=TotalLength,y=BodyWeight))+geom_point()

PowFit<-nlsLM(BodyWeight~powMod(TotalLength, a, b), data= Data2Fit, start = list(a=.1, b=.1))
summary(PowFit)
anova(PowFit)

Lengths<-seq(min(Data2Fit$TotalLength),max(Data2Fit$TotalLength),len=200)
coef(PowFit)["a"]
coef(PowFit)["b"]

Predic2PlotPow<-powMod(Lengths,coef(PowFit)["a"],coef(PowFit)["b"])
plot(Data2Fit$TotalLength,Data2Fit$BodyWeight)
lines(Lengths, Predic2PlotPow, col="blue", lwd=2.5)

confint(PowFit)
