from tools import cwd
from explore import split_by_time as sp
from tools import name

import pandas as pd
import numpy as np


def ui_flag1(log_x, split_point, start_date, end_date):
    log_flag1 = log_x[(log_x.behavior_type==3) & \
                      (log_x.date_time==split_point) & \
                        (log_x.hour_time>=19) & \
                        (log_x.hour_time<=21)
    ]
    feature_flag1 = log_flag1[['user_id', 'item_id']].drop_duplicates()
    fname = name.feature_name('flag1', 'ui', start_date, end_date)
    filename = name.file_name(split_point, fname)
    feature_flag1[fname] = 1
    feature_flag1.to_csv('data/'+filename, index=False)


if __name__ == "__main__":
    cc_intervals = [
        (1, 32)
    ]
    split_point_list = [31, 30, 29, 28, 27, 26, 25, 24]

    log = pd.read_csv('data/log_train_user_o2o.csv')
    for split_point in split_point_list:
        log_x = sp.split_sample_x(log, split_point)
        for (start_date, end_date) in cc_intervals:
            ui_flag1(log_x, split_point, start_date, end_date)


