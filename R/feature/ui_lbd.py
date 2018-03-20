from tools import cwd
from explore import split_by_time as sp
from tools import name

import pandas as pd
import numpy as np


def ui_lbd(log_x, split_point, start_date, end_date):
    log_x = log_x[(log_x.behavior_type==4) & \
                   (log_x.date_time<=split_point-start_date+1) & \
                    (log_x.date_time>=split_point-end_date+1)]
    feature_lbd = log_x.groupby(['user_id', 'item_id']).max().reset_index()
    feature_lbd = feature_lbd[['user_id', 'item_id', 'date_time']]
    feature_lbd['date_time'] = feature_lbd.apply(lambda x: split_point-x[2]+1, axis=1)
    fname = name.feature_name('lbd', 'ui', start_date, end_date)
    filename = name.file_name(split_point, fname)
    feature_lbd.columns = [u'user_id', u'item_id', fname]
    feature_lbd.to_csv('data/'+filename, index=False)


if __name__ == "__main__":
    cc_intervals = [
        (1, 32)
    ]
    split_point_list = [31, 30, 29, 28, 27, 26, 25, 24]

    log = pd.read_csv('data/log_train_user_o2o.csv')
    for split_point in split_point_list:
        log_x = sp.split_sample_x(log, split_point)
        for (start_date, end_date) in cc_intervals:
            ui_lbd(log_x, split_point, start_date, end_date)