#!/bin/bash

# For bibtex purposes, filename removes .tex from $1.
filename="${1//.tex/}"


pdflatex $1
pdflatex $1
bibtex $filename
pdflatex $1
pdflatex $1

mv $filename.pdf ../Results
evince ../Results/$filename.pdf &
# Move filename to results and read pdf from results directory

## Clean up
rm *~
rm *.aux
rm *.dvi
rm *.log
rm *.nav
rm *.out
rm *.snm
rm *.toc
rm *.bbl
rm *.blg
