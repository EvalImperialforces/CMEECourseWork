# Data Exploration Notes

#hist(DF$TraitValueSI) # Values mostly 0 which explains strange dist.

####### Subset data by ID series and create plots #####

#DF2 <- DF %>% select(FinalID, OriginalTraitValue, ConTemp) 
# Dataframe containing ID, Temperature and Trait value variables

#Makeplots <- function(r){
# Won't work because you need to take several traits for each ID 
#  FinalID <- r[0]
#  Traitvalue <- r[1]
#  ConTemp <- r[2]
#  for i in r:
#    pdf("../Results/Preliminary Graphs/TempvsTrait"r[0]".pdf")
#    qplot(ConTemp ~ TraitValue, colour = FinalID)
#    dev.off()
#  print("Plot created")
#}

# Create a unique list of just IDs
# loop though from 1 to length(uniq) in which you subset  dataset, finlID == uniq[i] (this is your df2)
# variable for unique trait name
#pdf -> paste("..Resullfff", uniq[i], ".pdf", sep="")
# Then print (qplot, w and ys are just contemp and ***, data df2)

# Plotting using dplyr
#pdf("../Results/Preliminary Graphs/TempvsTrait.pdf")
#d_ply(DF, "FinalID", summarise, plot(DF$ConTemp, DF$OriginalTraitValue ~ unique(DF$FinalID), type = o)
#dev.off()

# Try subsetting to plot
#IDsubs <- subset(DF, unique(DF$FinalID, select = c("ConTemp", "OriginalTraitValue"))

# Fit models on all curves and AIC them all. Subset after that and classify.
# nlslm fit 100 times with start value close to real value - gaussian distribution.