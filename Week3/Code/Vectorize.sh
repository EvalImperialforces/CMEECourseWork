#!/bin/bash
#Author:eva.EL1718@imperial.ac.uk
#Script: get_TreeHeight.sh
#Desc: Compare computational speed of Vectorize 1.py/ .R and Vectorize 2.py/.R.
#Date: Dec 2018


Rscript Vectorize1.R 
Rscript Vectorize2.R 
python3 Vectorize1.py
python3 Vectorize2.py