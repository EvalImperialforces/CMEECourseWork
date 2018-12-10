#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: November 2018
# Desc: Looking at the data

#clear environments
rm(list=ls())

library(dplyr)
#library(lattice)
library(ggplot2)
library(minpack.lm)

# Read in and observe data
DF <- read.csv("../Data/BioTraits.csv", header = TRUE)
#head(DF)
#nrow(DF)

# Use DataSeries ID and citation ID to find temperature performance IDs (wonder how they can be calculated).
# Overlay indicidually made plots for seperate IDs?
# Compare Habitat/Field 
# Compare Climates
# Between trophic levels or taxa


####### Subset data by ID series and create plots #####

# For loop method
IDlist = unique(DF$FinalID)

for (i in (1:length(IDlist))){
  subset_id<- IDlist[i] # Take out the ID for each iteration
  traitstosubset = subset(DF, DF$FinalID == subset_id) # Subset (can use filter) DF to get all columns for ID[i]
  traitstosubset<- traitstosubset[!is.na(traitstosubset$OriginalTraitValue),]
  for i in traitstosubset$ConTemp{
    if i = max
  }
  if (nrow(traitstosubset) >=4){
    pdf(file = paste("../Results/Preliminary_Graphs/", IDlist[i], ".pdf", sep = ""))
    print(qplot(traitstosubset$ConTemp, traitstosubset$OriginalTraitValue, data = traitstosubset, xlab = "Temperature (Degrees Celsius)", ylab = "Trait Value"))
    dev.off()
  }
   }


###### Polynomials ########
# Linear
#fit_linear <- lm(traitstosubset$ConTemp ~ traitstosubset$OriginalTraitValue)
#ggplot(traitstosubset, aes(ConTemp, OriginalTraitValue)) + geom_point() + geom_smooth(method = "lm") + theme_bw()
# Quadratic
#fit_quad <- lm(traitstosubset$ConTemp ~ poly(traitstosubset$OriginalTraitValue, 2, raw = TRUE)
#ggplot(traitstosubset, aes(ConTemp, OriginalTraitValue)) + geom_point() + geom_smooth(method = "lm", formula = y~poly(x, 2, raw=TRUE)) + theme_bw()
# Cubic
#fit_cube <- lm(traitstosubset$ConTemp ~ poly(traitstosubset$OriginalTraitValue, 3, raw = TRUE)
#ggplot(traitstosubset, aes(ConTemp, OriginalTraitValue)) + geom_point() + geom_smooth(method = "lm", formula = y~poly(x, 3, raw=TRUE)) + theme_bw()

ggplot(data = traitstosubset) +
  geom_point(aes(x = ConTemp, y = OriginalTraitValue), size = 0.8, colour = "black") + 
  geom_smooth( data = traitstosubset, aes(ConTemp, OriginalTraitValue), size = 1, colour = "darkblue", se = FALSE, stat = "smooth", method = "lm") + 
  geom_smooth(data = traitstosubset, aes(ConTemp, OriginalTraitValue), size = 1, colour = "red", se = FALSE, stat = "smooth", method = "lm", formula = y~poly(x, 2, raw=TRUE)) + 
  geom_smooth(data = traitstosubset, aes(ConTemp, OriginalTraitValue), size = 1, colour = "purple", se = FALSE, stat = "smooth", method = "lm", formula = y~poly(x, 3, raw=TRUE))



###### EARR Model ######### 
# Must convert to Kelvin!!!!!
# DeLong log tranformed metabolic metabolic rate data and 
# fit the log- transformed EAAR model
# Must find melting temp using quadratic eqn and optimum temp using eqn 6.
#powMod <- function()
  

##### Briere's Model ########
# Scaling
#To improve the fit, you can use weighted least-squares regression where an additional scale factor (the weight) is included in the fitting process. 
# Weighted least-squares regression minimizes the error estimate.


briere<- function(Temp, T0, Tm, c){
  return(c*Temp*(Temp-T0)*(abs(Tm-Temp)^(1/2))*as.numeric(Temp<Tm)*as.numeric(Temp>T0))
}

scale<-20
bfit<-nlsLM(ConTemp/20 ~briere(Temp, T0, Tm, c), start = list(Temp=20, T0=0, Tm=40, c=0.1), data = traitstosubset)
temp<-seq(0,80, length=1000)
pred.b<-predict(bfit, newdata = list(temp=temp))*scale
plot(traitstosubset$ConTemp, traitstosubset$OriginalTraitName, xlim =c(0,100))
lines(temp, pred.b, col=2)

# Bound values in nlsLM


#### Schoofield Model #######
# 3 new parameters p25 T1/2
# Use Eqn 6 (4 model parameters)


# fit a linear model
linearfunc <- function(x, m, b) {
  return(m * x + b)
}

plot(traitstosubset$OriginalTraitValue~traitstosubset$ConTemp)

fit = nlsLM(traitstosubset$OriginalTraitValue~linearfunc(traitstosubset$ConTemp, m, b), data = traitstosubset, start = list(m = .1, b = .1))
summary(fit)
AIC(fit)
confint(fit) #

Lengths = seq(min(traitstosubset$ConTemp), max(traitstosubset$ConTemp), 1)
PF <- linearfunc(Lengths, coef(fit)["m"], coef(fit)["b"])
plot(traitstosubset$OriginalTraitValue~traitstosubset$ConTemp)
lines(Lengths, PF)

# Fit briere function

briere<- function(Temp, T0, Tm, c){
  return(c*Temp*(Temp-T0)*(abs(Tm-Temp)^(1/2))*as.numeric(Temp<Tm)*as.numeric(Temp>T0))
}

fit = nlsLM(traitstosubset$OriginalTraitValue~briere(traitstosubset$ConTemp, T0, Tm, c), data = traitstosubset, start = list(T0 = 10, Tm = 30, c = .1))
summary(fit)
AIC(fit)
confint(fit) # 95% CI

Lengths = seq(min(traitstosubset$ConTemp), max(traitstosubset$ConTemp), 1)
PF <- briere(Lengths, coef(fit)["T0"], coef(fit)["Tm"], coef(fit)["c"])
plot(traitstosubset$OriginalTraitValue~traitstosubset$ConTemp)
lines(Lengths, PF)

briere2<-function(a,T0,Tm){
  return(a*x*(x-T0)*)
}






