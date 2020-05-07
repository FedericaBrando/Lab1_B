#!/home/fecke/anaconda3/envs/PB/bin/python

import sys

def seq_list(f1):
    '''Function that returns a list of sequences that can be printed. :type f1:str'''
    file = open(f1, "r")
    f = file.read()

    files = []
    f_o = ''
    for line in f :
        if line.startswith('>') :
            files.append(f_o)
            f_o = ""
            f_o += line
        else :
            f_o += line
    files.append(f_o)
    files.remove("")
    return files



if __name__ == '__main__' :
    file1 = seq_list(sys.argv[1])
    file2 = seq_list(sys.argv[2])

    nr_file = set(file2).difference(file1)

    c = 0
    for line in nr_file:
        if line.startswith('>'):
            c += 1
    print(len(nr_file))
    
    nr = "nr_" + sys.argv[1]

    for a in nr_file:
        f = open(nr, "a")
        s = "".join(a)
        f.write(s)
