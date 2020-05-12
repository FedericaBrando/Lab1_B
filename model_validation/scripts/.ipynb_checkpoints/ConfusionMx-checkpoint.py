#!/home/fecke/anaconda3/envs/Lab1_B/bin/python

import sys
import math
from tabulate import tabulate


def getCMx(file_path, threshold, pos_eval, pos_real=-1):
    '''This function computes the Confusion Matrix on a data file that has at least two columns that express the e-value
    and real positives and negatives. Inputs are: File name, threshold, evalue position and real position in the file
    :param pos_real: -1
    :type file_path: string
    :type threshold: int
    :type pos_eval: int'''
    c_mx = [[0.0, 0.0], [0.0, 0.0]]  # row1 neg-set, row2 pos-set
    f = open(file_path)
    for line in f:
        l = line.rstrip().split()    # l is a list that splits the lines
        t_f = int(l[pos_real])
        thr = float(l[pos_eval])
        if t_f == 1:    # this 'if' statements assign the indexes in the
            row = 1                  # confusion matrix
        elif t_f == 0:
            row = 0
        if thr < threshold:
            col = 1
        else:
            col = 0
        c_mx[row][col] += 1
    f.close()
    print(tabulate([['True neg', 'False pos'], ['False neg', 'True pos']], tablefmt="grid"))
    print(tabulate(c_mx, tablefmt='grid'))
    return c_mx


def compPerformance(mx):
    TP = mx[1][1]
    TN = mx[0][0]
    FP = mx[0][1]
    FN = mx[1][0]
    acc_score = (TP + TN) / (sum(mx[0]) + sum(mx[1]))
    div = math.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
    mcc_score = ((TP * TN) - (FP * FN)) / div
    prec = TP / (TP + FP)
    TPR = (TP) / (TP + FN)
    FPR = (FP) / (FP + TN)
    print(tabulate([['True Positive Rate', 'False Positive Rate', 'Accuracy', 'MCC score', 'PRECISION'], [TPR, FPR, acc_score, mcc_score, prec]], headers='firstrow', tablefmt='fancy_grid'))


if __name__ == '__main__' :
    try:
        filename = sys.argv[1]  # filename
        th = float(sys.argv[2])  # threshold
        print("Your threshold is", th)
        score_pos = 1  # position of the e-value
        cm = getCMx(filename, th, score_pos)
        compPerformance(cm)
    except:
        print(
            "You failed to provide filename as first input and threshold argument as second input on the command line!")
        sys.exit(1)  # abort
