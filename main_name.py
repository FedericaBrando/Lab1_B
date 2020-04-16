#!/home/fecke/anaconda3/envs/Lab1_B/bin/python
import sys


if __name__ == '__main__' :
    pdbfile1 = sys.argv[1]                      # makes the program read the input
    pdbfile2 = sys.argv[2]                      # if you call it from the terminal it will execute the program,
    list1 = sys.argv[3].split(',')              # if it is imported in another file as a module
    list2 = sys.argv[4].split(",")               # then it will not be executed
    print(pdbfile1, pdbfile2, list1, list2)
