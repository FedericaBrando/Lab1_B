#!/home/fecke/anaconda3/envs/PB/bin/python

import sys

def count_sequences(fpath):
    '''This function takes in input one value that is the filepath of fasta sequences file that we want to split.
    :type fpath: str'''
    with open(fpath) as f:
        c = 0
        for line in f:
            if line.startswith('>'):
                c += 1
        return c

def split(fp, nseq, nsplit):
    '''This function takes in input two value. the filepath and the number of splitting.
    :type fp: str
    :type nseq: int
    :type nsplit: int'''
    with open(fp) as f:
        files = []
        if nseq // nsplit != 0:
            l = nseq // nsplit
            for line in f:
                seqs = []
                c = 0
                for i in range(nsplit):
                    seq = ''
                    while l != c:
                        if not line.startswith('>'):    # se inizia con '>' allora :
                            seq += line
                        else:
                            seqs.append(seq)
                            seq = line
                            c += 1
                    files.append(seqs)

    print(len(files))
    return files


if __name__ == "__main__":
  #  try:
    filepath = sys.argv[1]
    num_splits = int(sys.argv[2])
    split(filepath, count_sequences(filepath), num_splits)
    #except:
    #    IndexError(print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nYou failed to provide inputs: \n python random_split.py [filepath] [# of splits] "))
    #    sys.exit(1)  # abort