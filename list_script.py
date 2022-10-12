#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 10:25:47 2022

@author: quinnjohnson
"""

#opens silm_chr2_seq.fasta in read mode
infile = open("chr2_seq.fasta","rt")

#read the first line
ref_info = infile.readline()

#read the second line
ref_sequence = infile.readline()

#create a list with the carets-identifers
ID = []

#create a list without the caret-sequences
seqdata = []

#creates a for loop to read the sequence data and put in the two lists
for line in infile:
    #if there is a caret
    if ('>' == line[0:1]):
        #place it in the identifers list
        ID.append(line)
    #if there isn't a caret
    else:
        #place it in the seqdata list
        seqdata.append(line)

#to find the number of individuals in the data set
numindvi = len(ID)
print(numindvi)

# Close the input file 
infile.close();

