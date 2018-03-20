from tools import cwd

import pandas as pd
import numpy as np
import time
import datetime


def relative_date(start_date, time_str):
    current_time = time.strptime(time_str, '%Y-%m-%d %H')
    current_date = datetime.date(current_time.tm_year, current_time.tm_mon, current_time.tm_mday)
    return (current_date-start_date).days+1


def hour_time(time_str):
    current_time = time.strptime(time_str, '%Y-%m-%d %H')
    return current_time.tm_hour

if __name__ == "__main__":
    log = pd.read_csv("data/log_train_user.csv")
    # log = pd.read_csv("data/log_train_user_head.csv")
    start_date = datetime.date(2014, 11, 18)
    log['date_time'] = log.time.apply(lambda time_str: relative_date(start_date, time_str))
    log['hour_time'] = log.time.apply(lambda time_str: hour_time(time_str))
    log.to_csv('data/log_train_all.csv', index=False)




