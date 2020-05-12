#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:39:56 2020

@author: danielelucarelli

take a fasta file and split into n fasta files 
has to be called as: python3 split-fasta.py <file to split> <n of times has to be splitted>
"""


import sys

def count_seq(f):

    with open(f,'r') as file:
        c=0
        for line in file:
            if '>' in line:
                c+=1
        return c

def cr_f(n):

    files=[]
    n=int(n)
    for i in range(1,n+1):
        if sys.argv[3]=="":
            files.append(sys.argv[1]+ str(i))
        else:
            files.append(sys.argv[3]+ sys.argv[1]+ str(i))
    return files
    
    

def split (f1,n,l):

     file=open(f1,"r")   
     f=file.read()
     c=0
     files=[]
     f_o=''
     l=l//int(n)
     for line in f:
         if c!=l and not line.startswith('>'):
             f_o+=line
         elif c!=l and line.startswith('>'):
             f_o+=line
             c+=1                   
         else:
             if c==l and line.startswith('>'):
                 files.append(f_o)
                 f_o=''
                 f_o+=line
                 c=1
             elif c==l and not line.startswith('>'):                                    
                 f_o+=line                                               
     files.append(f_o)
     return files
 
    
    
if __name__=='__main__':
    files=split(sys.argv[1],sys.argv[2],count_seq(sys.argv[1]))
    create=cr_f(sys.argv[2])
    for a,b in zip(files,create):
        f=open(b,'w')
        f.write(a)