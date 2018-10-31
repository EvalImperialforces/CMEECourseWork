#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: In-class plotting exercises

#clear environments
rm(list=ls())

MyDF<-read.csv("../Data/EcolArchives-E089-51-D1.csv")
dim(MyDF)

# Log plot to see actual predator prey mass regression
plot(log(MyDF$Predator.mass),log(MyDF$Prey.mass), pch=20, xlab = "Predator Mass (g)", ylab = "Prey Mass (g)")

hist(MyDF$Predator.mass)
hist(MyDF$Prey.mass)

# Histograms side by side for predator/prey distributions
par(mfrow=c(2,2))
hist(log(MyDF$Predator.mass), xlab = "Predator Mass (g)", ylab = "Count", breaks = 5)
hist(log(MyDF$Prey.mass), xlab = "Prey mass (g)", ylab = "Count", breaks = 5)

dev.off()
par(mfcol=c(2,1))
par(mfg=c(1,1))
hist(log(MyDF$Predator.mass),
     xlab = "Predator Mass (g)", ylab = "Count",
     col = "blue", border = "lightblue",
     main = "Predator")
hist(log(MyDF$Prey.mass), 
     xlab = "Prey mass (g)", ylab = "Count",
     col="green", border = "lightgreen",
     main = "Prey")

# Overlapping Histograms
dev.off()
hist(log(MyDF$Predator.mass), # Predator histogram
     xlab="Body Mass (kg)", ylab="Count", 
     col = rgb(1, 0, 0, 0.5), # Note 'rgb', fourth value is transparency
     main = "Predator-prey size Overlap") 
hist(log(MyDF$Prey.mass), col = rgb(0, 0, 1, 0.5), add = T) # Plot prey
legend('topleft',c('Predators','Prey'),   # Add legend
       fill=c(rgb(1, 0, 0, 0.5), rgb(0, 0, 1, 0.5))) # Define legend colors

# Boxplots

# Distribution of predator mass across all locations
boxplot(log(MyDF$Predator.mass), xlab = "Location", ylab = "Predator Mass", main = "Predator mass")

# Distribution of predator mass split into each location
boxplot(log(MyDF$Predator.mass) ~ MyDF$Location,
        xlab = "Location", ylab = "Predator Mass",
        main = "Predator mass by location")

boxplot(log(MyDF$Predator.mass) ~ MyDF$Type.of.feeding.interaction,
        xlab = "Feeding Type", ylab = "Predator Mass",
        main = "Predator mass by feeding interaction type")

# Combining plots
par(fig=c(0,0.8,0,0.8)) # Specifying figure size as proportion
plot(log(MyDF$Predator.mass), log(MyDF$Prey.mass),
     xlab = "Predator Mass (kg)", ylab = "Prey Mass (kg)")
par(fig=c(0,0.8,0.4,1), new=TRUE)
boxplot(log(MyDF$Predator.mass), 
        horizontal=TRUE, axes=FALSE)
par(fig=c(0.55,1,0,0.8),new=TRUE)
boxplot(log(MyDF$Prey.mass), axes=FALSE)
mtext("Fancy Predator-prey scatterplot", side=3, outer=TRUE, line=-3)

# Lattice
library(lattice)
densityplot(~log(Predator.mass) | Type.of.feeding.interaction, data = MyDF)
# Finds the log Pred.mass for each feedying type in different graphs

pdf("../Results/Pred_Prey_Overlay.pdf", # Open blank pdf page using a relative path
    11.7, 8.3) # These numbers are page dimensions in inches
hist(log(MyDF$Predator.mass), # Plot predator histogram (note 'rgb')
     xlab="Body Mass (kg)", ylab="Count", col = rgb(1, 0, 0, 0.5), main = "Predator-Prey Size Overlap") 
hist(log(MyDF$Prey.mass), # Plot prey weights
     col = rgb(0, 0, 1, 0.5), 
     add = T)  # Add to same plot = TRUE
legend('topleft',c('Predators','Prey'), # Add legend
       fill=c(rgb(1, 0, 0, 0.5), rgb(0, 0, 1, 0.5))) 
dev.off()
