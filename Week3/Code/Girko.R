#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Script to plot Girko's Law simulation and save as pdf.

#clear environments
rm(list=ls())

build_ellipse <- function(hradius, vradius){ 
  npoints = 250
  a <- seq(0, 2 * pi, length = npoints + 1)
  x <- hradius * cos(a)
  y <- vradius * sin(a)  
  return(data.frame(x = x, y = y))}

require(ggplot2)

N <- 250 # Size of the matrix
  
M <- matrix(rnorm(N * N), N, N) # Build the matrix
  
eigvals <- eigen(M)$values 
  
eigDF <- data.frame("Real" = Re(eigvals), "Imaginary" = Im(eigvals)) # Build a dataframe
  
my_radius <- sqrt(N) # The radius of the circle is sqrt(N)
  
ellDF <- build_ellipse(my_radius, my_radius) # Dataframe to plot the ellipse
  
names(ellDF) <- c("Real", "Imaginary") # rename the columns
  
p <- ggplot(eigDF, aes(x = Real, y = Imaginary))
p <- p +
  geom_point(shape = I(3)) +
  theme(legend.position = "none")

# Add the vertical and horizontal line
p <- p + geom_hline(aes(yintercept = 0))
p <- p + geom_vline(aes(xintercept = 0))

# Add ellipse and save to pdf
p <- p + geom_polygon(data = ellDF, aes(x = Real, y = Imaginary, alpha = 1/20, fill = "red"))
pdf("../Results/Girko.pdf", 
   11.7, 8.3)
p
dev.off()
