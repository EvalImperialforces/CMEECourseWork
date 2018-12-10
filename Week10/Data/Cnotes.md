=================================================================================
# Day 1
=================================================================================

# printf = print format("Hello, world!");
# All executable operations in C end with ";"
# ./a.out = compiled output
# Commenting in C - single line using //
#                 - Multi-line using /* */

# C very flexible with whitespace: tabs, newlines etc.


# Any variable needs to be forward declared
# Print contents of a.out by using ./a.out
# Can't put numbers or dashes at beginning of variable name 
# Variable types; 
#    char ch;
 #   float flt;
 #   _Bool yesno;
 #   double dbl;
 # %.8d = placeholder with 8 decimals in float variable

 # Placeholders - %i is integer
 #                %d is decimal
 #                %f is float
 #                %e is double
 # 
 # When 2 types of variables are computed together, one will change the other
 # i.e integer and float uprades both or result to float.
 # Type cast operators before output

 # When compiling you really should use 'gcc -Wall file'

 ===============================================================================
 # Day 2
 ===============================================================================

 # !a is same as saying if a == 0 

 # && is logical 'and'
 # || is logical 'or'

 # for loops: (initial i ; i condition ; operation for i)
 # Should use variable a loop condition and no hard(magic) numbers
 # C is not an object-orientated language!

# Scope where variable or name had influence;
# - Program (global)
# - File
# - Function
# - "Local"

# Stack - First in and last out
# Push information onto the stack (Next bit comes up underneath it - first is last to be read)
# If you have pointer for memory in function call. Because of the way stacking works
# It will point to garbage.
# Think about order of execution.

# Recursion extremely useful.

==================================================================================
# Day 3
==================================================================================

# Bit-wise operations
# Parsimony - 1st step in evaluating ancestral states. Fitch downpass assumes no order of characters - expressed as algorithm
# Translate binary and decimal - Odd numbers always have first bit set to one/

# Pointers are to access data out of scope.
