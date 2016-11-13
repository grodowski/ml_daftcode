import pandas as pd
import os
import numpy as np

import xgboost as xgb


xtrain = pd.read_pickle(os.path.join('data', 'xtrain.pkl'))
ytrain = pd.read_pickle(os.path.join('data', 'ytrain.pkl'))
xtest = pd.read_pickle(os.path.join('data', 'xtest.pkl'))

dMatrix_param = {
    'bst:eta': [0.002, 0.02],
    'bst:subsample': [0.5, 1],
    'bst:mim_child_weight': [0.4, 1],
    'bst:max_depth': [2, 30],
    'bst:maxgamma': [0, 1],
    'objective': 'binary_logistic',
}
