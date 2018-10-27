# Pre-allocation exercise 
# The process time of loops is compared to loops with pre-allocated vectors.

a <- NA
for (i in 1:100000) {
  a <- c(a, i)
}
print(a)
# For loop that resizes and stores each vector with each iteration

b <- rep(NA, 1000000)
for (i in 1:1000000) {
  a[i] <- i
}
print(b)
# Pre-allocated vector in for loop that does not re-allocate memory with each iteration


print(system.time(a))
print(system.time(b))
