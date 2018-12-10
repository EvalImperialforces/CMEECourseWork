#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Annotating plots using geom text.

#clear environments
rm(list=ls())
#dev.off()

a<-read.table("../Data/Results.txt", header = T)
head(a)

a$ymin<- rep(0, dim(a)[1]) # append column of 0s

# Print first linerange
p <- ggplot(a)
p <- p + geom_linerange(data = a, aes(
  x = x,
  ymin = ymin,
  ymax = y1,
  size = (0.5)
),
colour = "#E69F00",
alpha = 1/2, show.legend = FALSE)
p

# Second linerange
p <- p + geom_linerange(data = a, aes(
  x = x,
  ymin = ymin,
  ymax = y2,
  size = (0.5)
),
colour = "#56B4E9",
alpha = 1/2, show.legend = FALSE)
p

# Print third linerange
p <- p + geom_linerange(data = a, aes(
  x = x,
  ymin = ymin,
  ymax = y3,
  size = (0.5)
),
colour = "#D55E00",
alpha = 1/2, show.legend = FALSE)
p

# Annotate plot with labels
p <- p + geom_text(data = a, aes(x = x, y = -500, label = Label))
p

# Axis labels, remove legend, prepare for bw print
p <- p + scale_x_continuous("My x axis",
                            breaks = seq(3, 5, by = 0.05)) + 
  scale_y_continuous("My y axis") + 
  theme_bw() + 
  theme(legend.position = "none") 

# Saving plot as .pdf file
pdf("../Results/MyBars.pdf", 
    11.7, 8.3)
p
dev.off()
