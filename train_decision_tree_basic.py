#load in packages
import pandas as pd
import numpy as np
import seaborn as sns
import time
import math

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

#Models
from sklearn import tree
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier

#use sklearn.metrics.mean_squared_error() AND math.sqrt() to get RMSE
from sklearn.metrics import mean_squared_error

#set a random_state to be used in the notebook
random_state = 7
#load in the data:
#source path 
path = '../input/'

#Get the metadata (the .csv data) and put it into DataFrames
train_df = pd.read_csv(path + 'train.csv')

#show the dimensions of the train metadata.
print('train_df dimensions: ', train_df.shape)
y = train_df['label']
X = train_df['Feature']

#now make the train-test splits
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=random_state)
print('Dimensions: \n x_train:{} \n x_test{} \n y_train{} \n y_test{}'.format(x_train.shape, x_test.shape, y_train.shape, y_test.shape))

#create the Classifier
tree_clf = DecisionTreeClassifier(max_depth = 3, min_samples_split = 10)

#train the model
start = time.time()
tree_clf.fit(x_train, y_train)
stop = time.time()

#predict the response for the test data
tree_clf_pred = tree_clf.predict(x_test)

#print the RMSE
print(f'Training time: {round((stop - start),3)} seconds')
tree_clf_RMSE = math.sqrt(mean_squared_error(y_test, tree_clf_pred))
print(f'tree_clf_RMSE: {round(tree_clf_RMSE,3)}')
print('Done....')
