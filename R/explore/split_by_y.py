from tools import cwd

import pandas as pd
import numpy as np


def split_and_label(id_x, id_y):
    id_y['y'] = 1
    id_x_pos = pd.merge(id_x, id_y, how='inner')

    id_x_neg = pd.merge(id_x, id_y, how='left')
    id_x_neg = id_x_neg[id_x_neg.y.isnull()]
    id_x_neg['y'] = 0

    return id_x_pos, id_x_neg



if __name__ == "__main__":
    for split_point in [30, 29, 28, 27, 26, 25, 24]:
        id_y = pd.read_csv('data/'+str(split_point)+'_id_y.csv')
        id_x = pd.read_csv('data/'+str(split_point)+'_id_x.csv')
        id_x_pos, id_x_neg = split_and_label(id_x, id_y)
        id_x_pos.to_csv('data/'+str(split_point)+'_id_x_pos.csv', index=False)
        id_x_neg.to_csv('data/'+str(split_point)+'_id_x_neg.csv', index=False)





