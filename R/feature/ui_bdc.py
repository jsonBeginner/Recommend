from tools import cwd
from explore import split_by_time as sp
from tools import name

import pandas as pd
import numpy as np

def ui_bdc(log_x, split_point, start_date, end_date):
    log_bdc = log_x[(log_x.behavior_type==4) & \
               (log_x.date_time<=split_point-start_date+1) & \
                (log_x.date_time>=split_point-end_date+1)]
    feature_bdc = log_bdc.groupby(['user_id', 'item_id', 'date_time']).count().reset_index()\
        [['user_id', 'item_id', 'behavior_type']]
    fname = name.feature_name('bdc', 'ui', start_date, end_date)
    filename = name.file_name(split_point, fname)
    feature_bdc.columns = [u'user_id', u'item_id', fname]
    feature_bdc.to_csv('data/'+filename, index=False)


if __name__ == "__main__":
    bdc_intervals = [
        (1, 14),
        (15, 32)
    ]
    split_point_list = [31, 30, 29, 28, 27, 26, 25, 24]

    log = pd.read_csv('data/log_train_user_o2o.csv')
    for split_point in split_point_list:
        log_x = sp.split_sample_x(log, split_point)
        for (start_date, end_date) in bdc_intervals:
            ui_bdc(log_x, split_point, start_date, end_date)





