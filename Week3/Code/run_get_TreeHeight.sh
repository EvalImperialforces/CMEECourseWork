#!/bin/bash
#Author:eva.EL1718@imperial.ac.uk
#Script: get_TreeHeight.sh
#Desc: Running get_Treeheight python and R scripts.
#Date: Dec 2018

echo "Running get_TreeHeight.R with trees.csv"
Rscript get_TreeHeight.R ../Data/trees.csv

echo "Running get_TreeHeight.py with trees.csv"
python3 get_TreeHeight.py ../Data/trees.csv

echo "Done!"