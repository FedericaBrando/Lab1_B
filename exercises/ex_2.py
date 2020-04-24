#!/home/fecke/anaconda3/envs/Lab1_B/bin/python

import sys


def get_aln(alfile):
    d_aln = {}
    f = open(alfile, 'r')
    for line in f:
        if line.find('sp') != 0: continue  # if it doesn't start w/ sp go to next line
        l = line.split()
        seq = l[1]
        l_temp = l[0].split('|')
        sid = l_temp[1]
        d_aln[sid] = d_aln.get(sid, '') + seq
    return d_aln


def get_profile(d_aln):
    profile = []
    return profile


if __name__ == '__main__':
    alnfile = sys.argv[1]
    d_aln = get_aln(alnfile)
    for sid in d_aln:
        print(sid, d_aln[sid])
