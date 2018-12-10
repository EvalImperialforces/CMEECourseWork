#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Practical to create 3 lattice graphs by feeding interaction type
# on predator mass, prey mass and ratio of prey mass/predator mass.
# Mean and median of the above exported to csv.

# clear environments
rm(list=ls())
#dev.off()

require(dplyr)

MyDF<-read.csv("../Data/EcolArchives-E089-51-D1.csv")

# Creating and saving feeding interaction type by Predator mass
pdf("../Results/Pred_Lattice.pdf", # Open blank pdf to add lattice
    11.7, 8.3)
densityplot(~log(Predator.mass) | Type.of.feeding.interaction, data = MyDF,
  xlab= "Predator Mass (kg)", 
  col = rgb(1,0,0,0.5))
dev.off() # Adds lattice to pdf

# Creating and saving feeding interaction type by Prey mass
pdf("../Results/Prey_Lattice.pdf", 
    11.7, 8.3)
densityplot(~log(Prey.mass) | Type.of.feeding.interaction, data = MyDF,
            xlab= "Prey Mass (kg)", 
            col = rgb(1,0,0,0.5))
dev.off()

# Creating and saving feeding interaction type by Prey Mass/ Predator Mass ratio
ratio<-transform(MyDF, Prey_Predator_mass_ratio = Prey.mass/Predator.mass)
# Create variable 
plot(log(ratio$Prey_Predator_mass_ratio))
pdf("../Results/SizeRatio_Lattice.pdf", 
    11.7, 8.3)
densityplot(~log(Prey_Predator_mass_ratio) | Type.of.feeding.interaction, data = ratio,
            xlab= "Predator_Prey_mass_ratio",
            col= rgb(1,0,0,0.5))
dev.off()

# Calculating mean and median log predator mass, prey mass, 
# and predator-prey size ratio by feeding type.


pp_results <- MyDF %>% 
  group_by(Type.of.feeding.interaction) %>%
  summarise(
    Predator_mass_mean = mean(log(Predator.mass)),
    Predator_mass_median = median(log(Predator.mass)),
    Prey_mass_mean = mean(log(Prey.mass)),
    Prey_mass_median = median(log(Prey.mass)),
    Prey_prey_ratio_mean = mean(log(Prey.mass/Predator.mass)),
    Prey_prey_ratio_median = median(log(Prey.mass/Predator.mass))
    )
# Group by feeding type and summarise the mean and median of all specified variables
print(pp_results)
write.csv(pp_results, file= "../Results/PP_Results.csv", row.names = F)
# Write output to csv file

