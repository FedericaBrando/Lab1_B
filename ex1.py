#!/usr/bin/env python3.7
import sys
from Bio.SVDSuperimposer import SVDSuperimposer
import numpy as np

def get_ca_atoms(pdbfile,chain,rlist,atom='CA'):
    l_coords = []
    f_pdb = open(pdbfile, 'r')
    for line in f_pdb:
        if line[:4] != 'ATOM' : continue
        if line[21] != chain : continue
        if line[22:26].strip() not in rlist : continue
        if atom not in line : continue
        x = float(line[30:38])
        y = float(line[38:46])
        z = float(line[46:54])
        l_coords.append([x,y,z])
    return l_coords

def rmsd(lcoord1, lcoord2):
    if len(lcoord1) != len(lcoord2):
        print(sys.stderr.write("error: number of coords are different\n"))
        sys.exit()
    else:
        svd = SVDSuperimposer()
        svd.set(np.array(lcoord1), np.array(lcoord2))
        svd.run()
        rmsd = svd.get_rms()
        rot, tran = svd.get_rotran()
        print('R', rot)
        print('T', tran)
        return rmsd





if __name__ == '__main__' :
    # if you call it from the terminal it will execute the program,
    # if it is imported in another file as a module
    # then it will not be executed
    pdbfile1 = sys.argv[1]
    chain1 = sys.argv[2] # sys.argv[#] makes the program read the input
    pdbfile2 = sys.argv[3]
    chain2 = sys.argv[4]
    list1 = sys.argv[5].split(',')
    list2 = sys.argv[6].split(",")
    coord1 = get_ca_atoms(pdbfile1, chain1, list1)
    coord2 = get_ca_atoms(pdbfile2, chain2, list2)
    print(coord1, '\n', coord2)
    print(rmsd(coord1, coord2))
