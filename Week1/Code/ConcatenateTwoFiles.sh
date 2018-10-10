#!/bin/bash
cat $1 > $3
# Display contents of $1 in $3
cat $2 >> $3
# Add contents of $2 to $3
echo "Merged File is"
cat $3
# Display $3 to show added contents
