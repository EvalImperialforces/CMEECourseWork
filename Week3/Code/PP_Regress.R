#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Script to generate plot of changes in predator mass with prey mass across different 
# types of feeding interactions and grouped by predator lifestage.

#clear environments
rm(list=ls())

require(ggplot2)
require(plyr)
require(dplyr)

MyDF<-read.csv("../Data/EcolArchives-E089-51-D1.csv")

pp <- MyDF %>% rowwise() %>%  mutate(Prey.mass = ifelse(Prey.mass.unit == "mg", Prey.mass/1000, Prey.mass))
# Pipe function to go through data rowise and replace Prey mass in mg with g (mass/1000)

pdf("../Results//PP_Regress_Fig.pdf", 9, 11.7)
# Generating empty pdf file for figure

p <- qplot(Prey.mass, 
           Predator.mass, 
           data = MyDF,
           log = "xy", # Logs data and axes
           xlab = "Prey Mass in grams",
           ylab = "Predator Mass in grams",
           colour = Predator.lifestage, 
           shape = I(3), 
           size = I(2),
           facets = Type.of.feeding.interaction~.)
p + geom_smooth(method = "lm", fullrange = T) + theme(legend.position = "bottom")
dev.off()

# Calculating regression results
# Group and subset variables using ddply and pass to linear model 
df2 <- dlply(MyDF,.(Type.of.feeding.interaction, Predator.lifestage), function(x) lm(Predator.mass~Prey.mass, data = x))

# Extract linear model results and make a data frame of the coefficients
lmextract <- ldply(df2, function(x) {
  intercept <-summary(x)$coefficients[1]
  slope <-summary(x)$coefficients[2]
  p_val <- summary(x)$coefficients[8]
  r2 <- summary(x)$r.squared
  data.frame(slope, intercept, r2, p_val)
})

# Add the f stat seperately using the same ldply function
f_stat <- ldply(df2, function(x) summary(x)$fstat[1])

# Merge f stat and other coefficients into the final dataframe
final_table <- merge(lmextract, f_stat, by = c("Type.of.feeding.interaction",
                                        "Predator.lifestage"), all = T)

# Give F stat column a header
names(final_table)[7] = "F statistc"

write.csv(final_table,"../Results/PP_Regress_Results.csv", row.names = F)
# Write to a csv file