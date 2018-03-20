from tools import cwd

import pandas as pd
import numpy as np
import time

def split_sample_x(log, split_point):
    log = log[log['date_time']<=split_point]
    return log


def split_id_x(log, split_point):
    x_log = log[log['date_time']<=split_point]
    return x_log[['user_id','item_id']].drop_duplicates()


def split_id_y(log, split_point):
    y_log = log[(log['date_time']==split_point+1) & (log['behavior_type']==4)]
    return y_log[['user_id','item_id']].drop_duplicates()


def is_candidates(x, item_set):
    if x[1] in item_set:
        return 1
    else:
        return 0


if __name__ == "__main__":
    log = pd.read_csv('data/log_train_user_o2o.csv')
    ## test sample ids
    split_point = 31
    test_id_x = split_id_x(log, split_point)
    test_id_x.to_csv('data/31_id_x.csv', index=False)

    ## train sample ids
    for split_point in [30, 29, 28, 27, 26, 25, 24]:
        id_x = split_id_x(log, split_point)
        id_x.to_csv('data/'+str(split_point)+'_id_x.csv', index=False)
        id_y = split_id_y(log, split_point)
        id_y.to_csv('data/'+str(split_point)+'_id_y.csv', index=False)

