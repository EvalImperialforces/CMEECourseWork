""" List comprehension and loop exercise for bird species """
""" Author: Eva Linehan """

birds = ( ('Passerculus sandwichensis','Savannah sparrow',18.7),
          ('Delichon urbica','House martin',19),
          ('Junco phaeonotus','Yellow-eyed junco',19.5),
          ('Junco hyemalis','Dark-eyed junco',19.6),
          ('Tachycineata bicolor','Tree swallow',20.2),)


#(1) Write three separate list comprehensions that create three different
# lists containing the latin names, common names and mean body masses for
# each species in birds, respectively.

latin_names, common_names, body_mass = ([] for i in range (3))
# Three lists defined together
for name in birds:
    latin_names.append(name[0])
    common_names.append(name[1])
    body_mass.append(name[2])
#for each list, the selected element in each subset (0th,1st,2nd) is added
print (latin_names)
print (common_names)
print (body_mass)

# (2) Now do the same using conventional loops (you can shoose to do this
# before 1 !).

latin_names = [name[0] for name in birds]
print (latin_names)

common_names = [name[1] for name in birds]
print (common_names)

body_mass = [name[2] for name in birds]
print (body_mass)


# ANNOTATE WHAT EVERY BLOCK OR IF NECESSARY, LINE IS DOING!

# ALSO, PLEASE INCLUDE A DOCSTRING AT THE BEGINNING OF THIS FILE THAT
# SAYS WHAT THE SCRIPT DOES AND WHO THE AUTHOR IS.