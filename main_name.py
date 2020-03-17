#!/usr/bin/env python3.7
import sys




if __name__ == '__main__' :
    # if you call it from the terminal it will execute the program,
    # if it is imported in another file as a module
    # then it will not be executed
    pdbfile1 = sys.argv[1]  # makes the program read the input
    pdbfile2 = sys.argv[2]
    list1 = sys.argv[3].split(',')
    list2 = sys.argv[4].split(",")
    print(pdbfile1, pdbfile2, list1, list2)
