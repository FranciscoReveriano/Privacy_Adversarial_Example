import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from Models.Naive_Bayes import *

def test_noise_naive_bayes(X,Y, columns, size_of_noise):
    # Copy Dataframes
    noise_y = Y.copy()
    noise_x = X.copy()

    # Loop Through and Add Noise
    noise_mean = 0

    # Convert Panda Dataframe to Numpy Array
    noise_x = noise_x.to_numpy()

    # Loop Through To Add Noise
    for i in range(len(noise_x)):
        for j in range(len(noise_x[i])):
            noise = np.random.uniform(noise_mean, size_of_noise)
            noise_x[i][j] = noise_x[i][j] + noise

    # Convert Numpy Array Back to Dataframe
    noise_x = pd.DataFrame(noise_x)
    noise_x.columns = columns

    #Calculate Noise Difference
    L2_X = mean_squared_error(X, noise_x)

    # Split the Dataset
    X_train, X_test, Y_train, Y_test = train_test_split(noise_x, noise_y, test_size=.4)
    test_accuracy, test_precision, test_recall, test_auc =  Return_Naive_Bayes_Model(X_train, Y_train, X_test, Y_test)
    return L2_X, test_accuracy, test_precision, test_recall, test_auc

def add_noise(noise_x, noise_mean, noise):
    # Convert Panda Dataframe to Numpy Array
    noise_x = noise_x.to_numpy()
    # Loop Through To Add Noise
    for i in range(len(noise_x)):
        for j in range(len(noise_x[i])):
            add_noise = np.random.uniform(noise_mean, noise)
            noise_x[i][j] = noise_x[i][j] + add_noise
    return noise_x