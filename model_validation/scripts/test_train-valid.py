#!/home/fecke/anaconda3/envs/Lab1_B/bin/python

import pandas as pd
from pandas import read_csv
import seaborn as sn
from matplotlib import pyplot as plt
from matplotlib.colors import *
from sklearn.metrics import confusion_matrix, matthews_corrcoef, accuracy_score, auc
from tabulate import tabulate
from sklearn.metrics import precision_recall_curve
from sklearn.model_selection import StratifiedKFold
from statistics import mean, stdev


def get_eval(x):
    '''Given a pandas object it returns a list'''
    evalues = []
    for i in x:
        evalues.append(i)
    return evalues


def mcc_acc_index(Y_true, x):
    '''This function takes in input Y_true --> data class and x --> feature.
    Given a set of thresholds, it evaluates the thresholds and computes the
    mcc for each y_predicted with a given threshold. It returns the max MCC
    and max Accuracy, and the best threshold'''
    ACC_list = []
    MCC_list = []
    th = []
    z = 0
    for j in range(-10, 1, 1) :
        Y_predict = []
        threshold = 10 ** j
        for k in x:
            if k < threshold:
                c = 1
            else :
                c = 0
            Y_predict.append(c)
        y_predict = np.array(Y_predict)
        th.append(threshold)
        MCC_list.append([matthews_corrcoef(Y_true, y_predict), z])
        ACC_list.append([accuracy_score(Y_true, y_predict), z])
        z += 1
    max_mcc, index = max(MCC_list)
    acc = ACC_list[index][0]
    return max_mcc, th[index], acc


def get_cfmx(threshold, x_true, y_true):
    '''This function takes in input the threshold, the feature (in this case evalue)
    and the class. It returns a list of classes predicted with the given threshold
    and a confusion matrix between the y_true and the predicted'''
    y_predict = []

    for k in x_true:
        if k <= threshold:
            c = 1
        else:
            c = 0
        y_predict.append(c)
    return y_predict, confusion_matrix(y_true, y_predict)


def plot_cm(Y_true, Y_pred, title):
    '''This function takes in input 3 arguments:
    Y_true --> class from data
    Y_pred --> class predicted
    title ---> plot title'''
    data = {'y_Actual' : Y_true,
            'y_Predicted' : Y_pred
            }
    df = pd.DataFrame(data, columns=['y_Actual', 'y_Predicted'])
    cmx = pd.crosstab(df['y_Actual'], df['y_Predicted'], rownames=['Actual'], colnames=['Predicted'])
    ax = plt.axes()
    sn.set()
    sn.heatmap(cmx,
               annot=True,
               linewidths=1,
               color=sn.color_palette("Blues"),
               square=True,
               robust=True,
               fmt='.1f',
               ax=ax
               )
    ax.set_title(title)
    plt.show()


def get_PR(yy, xx):
    '''This function takes in input all data in the form of y-->classes
    and x--->features, it returns the PR curve plotted and also precision, r
    ecall and the thresholds used for the plotting.'''

    xx = xx / max(xx)
    yscore = [values for values in xx]
    precision, recall, thresholds = precision_recall_curve(yy,  # pos_label = 0 so th works reverse
                                                           yscore,  # so that whatever is > th is labelled
                                                           pos_label=0)  # as 0 so negative.

    ap = auc(recall.tolist(), precision)
    print('Area under PR curve: ', ap)

    sn.set()
    sn.set_context("paper")

    plt.plot(recall,
             precision,
             color='orange',
             lw=4,
             label='PR curve'
             )
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('PR Curve. Area: %.2f' % ap)
    plt.legend(loc="lower left")
    plt.savefig('../outputs/PR_curve')
    plt.show()

    return precision, recall, thresholds


def get_scatterplot(x_data, y_data, th_l):
    '''This function gets in input x_data and y_data that are alla data, y for 'class'
    type data and x for 'features' type data. the third value is a list of e-value thresholds. '''
    data_y = []
    data_x = []

    # reformatting data
    for i, j in zip(y_data, x_data):
        if i == 0:                      # 0 --> negatives so, it doesn't present kunitz domain
            data_y.append('Not Kunitz')
        else :                          # 1 --> positives so, it presents kunitz domain
            data_y.append('Kunitz')
        data_x.append(float(j))

    # data to be plotted
    plot_data = {'e-value' : data_x,
                 'class' : data_y}

    # data exploration - how many positives?
    y_data.value_counts()

    sn.set()
    sn.set_context("paper")

    #----data visualization-----
    # countplot
    sn.countplot(x='class',
                 hue='class',
                 dodge=False,
                 data=plot_data,
                 palette='hls',
                 linewidth=0.7
                 )
    plt.yscale('log')
    plt.ylabel('count')
    plt.savefig('../outputs/domain_barplot.png')
    plt.show()

    # scatter plot
    alldataplot = sn.stripplot(y='e-value',
                               x='class',
                               hue='class',
                               data=plot_data,
                               linewidth=0.7,
                               palette='hls',
                               jitter=0.15,
                               dodge=False,
                               )

    alldataplot.set(yscale='log', ylim=(1e-32, 5))
    plt.title('Domain e-value and thresholds')

    # adding an horizontal line for each valid threshold found
    prov_th = list(set(th_l))
    colors = ['green', 'orange', 'pink', 'red', 'yellow']
    for th, color in zip(prov_th, colors):
        th_title = 'threshold: ' + str(th)
        alldataplot.axhline(th, c=color, label=th_title)
    plt.ylabel('e-value')
    plt.legend(loc='lower right', fontsize='small')
    plt.savefig('../outputs/Domain_scatterplot.png')
    plt.show()


def main(f):
    names = ['e-value', 'attribute']
    data = read_csv(f, names=names)

    X = data['e-value']
    y = data['attribute']
    print(sum(y))

    get_PR(y, X)


    skf = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=4)
    skf.get_n_splits(X, y)

    mcc_l = []
    acc_l = []
    th_l = []
    fp_l = []
    fn_l = []
    tn_l = []
    tp_l = []

    for train_index, test_index in skf.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        print('Real positives in my testing set', sum(y_test))

        max_mcc, th, acc = mcc_acc_index(y_train, get_eval(X_train))
        max_pred_ytrain, cm = get_cfmx(th, get_eval(X_train), y_train)
        title1 = 'ConfMx - Training set ' + str(th)
        # plot_cm(y_train, max_pred_ytrain, title1)
        print('BEST PERFORMANCE ON TESTING - ConfMx')
        max_pred_ytest, cm = get_cfmx(th, get_eval(X_test), y_test)
        mcc_test = matthews_corrcoef(y_test, max_pred_ytest)
        acc_test = accuracy_score(y_test, max_pred_ytest)
        tn_fp, fn_tp = cm
        print(cm)
        title2 = 'ConfMx - Testing set ' + str(th)
        # plot_cm(y_test, max_pred_ytest, title2)
        mcc_l.append(mcc_test)
        acc_l.append(acc_test)
        th_l.append(th)
        fp_l.append(tn_fp[1])
        tn_l.append(tn_fp[0])
        fn_l.append(fn_tp[0])
        tp_l.append(fn_tp[1])

    print(
        'True negative',
        'True positive',
        'False positive',
        'False negative',
        'threshold',
        'mcc_score',
        'accuracy_score',
        sep='\t')
    for i in range(len(th_l)) :
        print(tn_l[i], tp_l[i], fp_l[i], fn_l[i], th_l[i], mcc_l[i], acc_l[i], sep='\t\t')

    print(tabulate([['mcc_score mean', 'mcc_stdev', 'acc_score mean', 'acc_stdev'],
                    [mean(mcc_l), stdev(mcc_l), mean(acc_l), stdev(acc_l)]],
                   headers='firstrow',
                   tablefmt='fancy_grid'))
    get_scatterplot(X, y, th_l)


filename = '../alldata.csv'

main(filename)
