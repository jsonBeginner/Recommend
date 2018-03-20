from tools import cwd

import pandas as pd
import numpy as np
import random
import scipy
from scipy import stats



def recall_up_limit():
    val_id_y = pd.read_csv('data/30_id_y.csv')
    val_id_x = pd.read_csv('data/30_id_x.csv')

    inter_id = pd.merge(val_id_x, val_id_y, how='inner')
    print 1.0*len(inter_id)/len(val_id_x)
    print 1.0*len(inter_id)/len(val_id_y)


def sold_curve():
    for split_point in [30, 29, 28, 27, 26, 25, 24]:
        id_x_pos = pd.read_csv('data/'+str(split_point)+'_id_x_pos.csv')
        print id_x_pos.count()[0]


def check_correlation():
    split_point = 29
    id_x_pos = pd.read_csv('data/'+str(split_point)+'_id_x_pos.csv')
    id_x_neg = pd.read_csv('data/'+str(split_point)+'_id_x_neg.csv')
    rate = 10

    rows = random.sample(id_x_neg.index, len(id_x_pos)*rate)
    id_x_neg_10 = id_x_neg.ix[rows]
    id = pd.concat([id_x_pos, id_x_neg_10])

    df = id
    for d in range(1, split_point+1):
        fname = u'ui_cc_'+str(d)+'_'+str(d)
        feature_df = pd.read_csv('data/'+str(split_point)+'_feature_'+fname+'.csv')
        df = pd.merge(df, feature_df, how='left')

    df = df.fillna(0)
    for d in range(1, split_point+1):
        fname = u'ui_cc_'+str(d)+'_'+str(d)
        y = df['y'].as_matrix()
        x = df[fname].as_matrix()
        print scipy.stats.pearsonr(x, y)[0]


# recall_up_limit()