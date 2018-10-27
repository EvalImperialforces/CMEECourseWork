#!/usr/bin/env Rscript
# Author: Eva Linehan
# Date: October 2018
# Desc: Testing apply function using a built function

#clear environments
rm(list=ls())

SomeOperation <- function(v){ # (What does this function do?)
  if (sum(v) > 0){
    return (v * 100)
  }
  return (v)
}

M <- matrix(rnorm(100), 10, 10)
print (apply(M, 1, SomeOperation))

