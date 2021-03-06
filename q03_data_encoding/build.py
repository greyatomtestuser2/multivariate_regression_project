from greyatomlib.multivariate_regression_project.q01_load_data.build import load_data
from greyatomlib.multivariate_regression_project.q02_data_split.build import split_dataset
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
df = load_data('data/student-mat.csv')
 
x_train, x_test, y_train, y_test =  split_dataset(df)

def label_encode(X_train,X_test):
    """encodes the non-numeric values to numeric"""
    le = LabelEncoder()

    for i in range(0, X_train.shape[1]):
        # i=0
        if not np.isreal(X_train.iloc[1, i]):
            X_train.iloc[:, i] = le.fit_transform(X_train.iloc[:, i])
            X_test.iloc[:, i] = le.transform(X_test.iloc[:, i])
    return X_train, X_test
    


