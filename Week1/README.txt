# Title: CMEE Coursework Week 1
# Author: Eva Linehan
# Date: Oct 2018

This folder contains CMEE coursework from week 1 arranged in the 'Data', 'Code' and 'Sandbox' folders. The 'Data' folder comprises of data files used in practical exercises and assessments during the week. 'Code' contains code used to execute commands as part of in-class examples and weekly assessments. The 'Sandbox'folder is primarily for storing output files from practical examples.

This week's coursework comprises of the following chapters of the "Multilingual Quantitative Biologist!" notebook;
Chapter 2: Unix
Chapter 3: Shell Scripting
Chapter 4: Version Control with Git
Chapter 5: Scientific documents with LATEX


'Code' contains the following; 

'boilerplate.sh'file
- This shell script prints "This is a shell script".

'CompileLaTeX.sh'file
- This shell script compiles LaTeX with bibtex and cleans up by removing additional files generated (*~, *.aux, *.dvi, *.log, *.nav, *.out, *.snm, *.toc, *.bbl, *.blg).

'ConcatenateTwoFiles.sh'file 
- Shell script to merge contents of 2 files into a new file.

'CountLines.sh'file
- Shell script to count the number of lines in a file and print output in a sentence.

'csvtospace.sh'file
- Practical assessment shell script that converts comma seperated value files (Temperature files in this case) to space separated value files with a new name.

'FirstBiblio.bib' file
- BibTex export of 'Does the inertia of a body depend upon its energy-content' by Albert Einstein from Google Scholar.

'FirstExample.pdf' file
- First LaTeX example titled "A Simple Document" with Abstract, Introduction, Materials & Methods and References.

'FirstExample.tex' file
- .tex version of first LaTeX example titled "A Simple Document".

'MyExampleScript.sh' file
- Shell script to say hello and incorporate username into hello message.

'tabtocsv.sh' file
- This shell script substitutes all tabs with commas.

'tiff2png.sh' file
- Shell script to convert .tiff files to .png files.

'UnixPrac1.txt'file
- Text file with UNIX shell commands to count lines in each fasta file, print E.coli genome, count sequence length of E.coli genome, count the matches of the 'ATGC' sequence in the genome and compute the AT/GC ratio.

'variables.sh'file
- Shell script to show the assignment and insertion of variables and read two numerical values to compute the sum.


'Data' contains the following;

'fasta' folder
- Three fasta files used in the fasta exercise as part of UnixPrac1.txt

'Temperatures' folder
- Three .csv folders used as part of the shell scripting practical and three .txt files generated from the script 'csvtospace.sh'.

'Spawannxs.txt' file
- List of protected species from the UN website to explore the grep command.


'Sandbox' contains the following;

'TestFind' folder
- Contains three directories and subdirectories to explore the find command.

'TestWild' folder
- Contains five .csv files and five.txt files to explore wildcard functions.

'Countlinestest.txt' file
- Text file output from 'Countlines.sh' shell script.

'ListRootDir.txt' file
- Text file listing root directories on seperate lines.

'Merge1.txt' file
- Text file created for 'ConcatenateTwoFiles.sh' shell script example.

'Merge2.txt' file
- Text file created for 'ConcatenateTwoFiles.sh' shell script example.

'Mergedfiles.txt' file
- Text file generated from 'ConcatenateTwoFiles.sh' shell script example.

'test.txt' file
- Text file generated from redirection and pipe example.

'test.txt.csv' file 
- 'test.txt' file converted to comma seperated values.


A 'Results' folder will be generated when scripts in code are run.



 
