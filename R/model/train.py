from tools import cwd
from tools import name
from explore import split_by_time as sp
from model import combine

import pandas as pd
import numpy as np


feature_list = [
    # [name.feature_name('cc', 'ui', 1, 1), 0],
    # [name.feature_name('cc', 'ui', 2, 2), 0],
    # [name.feature_name('cc', 'ui', 3, 3), 0],
    # [name.feature_name('cc', 'ui', 4, 4), 0],

    # [name.feature_name('f3c', 'ui', 1, 1), 0],
    # [name.feature_name('f3c', 'ui', 2, 2), 0],
    # [name.feature_name('f3c', 'ui', 3, 3), 0],
    # [name.feature_name('f3c', 'ui', 4, 4), 0],

    # [name.feature_name('f2c', 'ui', 1, 1), 0],

    # (name.feature_name('flag1', 'ui', 1, 32), 0),
    #
    (name.feature_name('lbd', 'ui', 1, 32), 99),
    (name.feature_name('lcd', 'ui', 1, 32), 99),
    (name.feature_name('lf2d', 'ui', 1, 32), 99),
    (name.feature_name('lf3d', 'ui', 1, 32), 99),
]



offline = True
# offline = False


if offline:
    split_point_list = [29]
    split_point = 30
else:
    split_point_list = [30]
    split_point = 31

epochs = 5

rate = 10

test_limit_count = 800




df_test = combine.combine_test(feature_list, split_point)

def train_and_predict():
    df_train_list = [
        combine.combine_train(feature_list, split_point, rate)
            for split_point in split_point_list
    ]
    df_train = pd.concat(df_train_list)

    features = [ f for (f,n) in feature_list]
    X_train = df_train[features].as_matrix()
    Y_train = df_train['y'].as_matrix()
    X_test = df_test[features].as_matrix()

    # from sklearn.linear_model import LogisticRegression, LinearRegression
    # clf = LogisticRegression(C=1.0, penalty='l2', tol=1e-6)

    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier(n_estimators=100)

    clf.fit(X_train, Y_train)
    pred_arr = clf.predict_proba(X_test)
    return pred_arr

pred_arr_list = [train_and_predict() for i in range(epochs)]
pred_arr = pred_arr_list[0]
for i in range(1, epochs):
    pred_arr = pred_arr + pred_arr_list[i]


df_test['prob'] = pred_arr[:, 1]
df_test = df_test.sort(columns='prob', ascending=False).reset_index(drop=True)
df_pred = df_test[df_test.index < test_limit_count][['user_id', 'item_id']]
if offline:
    df_val = pd.read_csv('data/'+str(split_point)+'_id_y.csv')
    inter_count = len(pd.merge(df_val, df_pred, how='inner'))
    P = 1.0*inter_count/len(df_pred)
    R = 1.0*inter_count/len(df_val)
    F1 = 2*P*R/(P+R)
    print 'hits:', inter_count
    print 'P=',P
    print 'R=',R
    print 'F1=',F1
else:
    df_pred.to_csv('data/'+str(split_point)+'_id_y_predict.csv', index=False)



