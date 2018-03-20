from tools import cwd
from explore import split_by_time as sp
from tools import name

import pandas as pd
import numpy as np


def ui_cc(log_x, split_point, start_date, end_date):
    log_cc = log_x[(log_x.behavior_type==1) & \
                   (log_x.date_time<=split_point-start_date+1) & \
                    (log_x.date_time>=split_point-end_date+1)]
    feature_cc = log_cc.groupby(['user_id', 'item_id']).count().reset_index()
    feature_cc = feature_cc[['user_id', 'item_id', 'time']]
    fname = name.feature_name('cc', 'ui', start_date, end_date)
    filename = name.file_name(split_point, fname)
    feature_cc.columns = [u'user_id', u'item_id', fname]
    feature_cc.to_csv('data/'+filename, index=False)


if __name__ == "__main__":
    cc_intervals = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 6),
        (7, 8),
        (9, 15),
        (16, 32)
    ]
    split_point_list = [31, 30, 29, 28, 27, 26, 25, 24]

    log = pd.read_csv('data/log_train_user_o2o.csv')
    for split_point in split_point_list:
        log_x = sp.split_sample_x(log, split_point)
        for (start_date, end_date) in cc_intervals:
            ui_cc(log_x, split_point, start_date, end_date)


