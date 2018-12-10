#!/bin/bash
#!/bin/bash
#Author:eva.EL1718@imperial.ac.uk
#Script: tiff2png.sh
#Desc: Convert *.tif to *.png
#Date: Oct 2018

for f in *.tif;
do
echo "Converting $f";
convert "$f" "$(basename "$f" .tif).jpg";
done