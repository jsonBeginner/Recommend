from tools import cwd
from tools import name
from explore import split_by_time as sp

import pandas as pd
import random


def __combine(feature_list, split_point, ids):
    df = ids
    for (fname, nval) in feature_list:
        filename = name.file_name(split_point, fname)
        feature_df = pd.read_csv('data/'+filename)
        df = pd.merge(df, feature_df, how='left')
        df = df.fillna(nval)
    return df


def combine_test(feature_list, split_point):
    ids = pd.read_csv('data/'+str(split_point)+'_id_x.csv')
    df = __combine(feature_list, split_point, ids)
    return df


def combine_train(feature_list, split_point, rate):
    id_x_pos = pd.read_csv('data/'+str(split_point)+'_id_x_pos.csv')
    id_x_neg = pd.read_csv('data/'+str(split_point)+'_id_x_neg.csv')
    rows = random.sample(id_x_neg.index, len(id_x_pos)*rate)
    id_x_neg_10 = id_x_neg.ix[rows]
    ids = pd.concat([id_x_pos, id_x_neg_10])

    df = __combine(feature_list, split_point, ids)
    return df


if __name__ == "__main__":
    split_point = 30
    feature_list = [
        'ui_cc_1_1',
        'u_bc_1_32',
        'i_bc_1_32'
    ]
    rate = 10
    df_train = combine_train(feature_list, split_point, rate)
    df_test = combine_test(feature_list, split_point)


