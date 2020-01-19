# data imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from scipy.stats import normaltest
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import os

print(os.listdir())

# #loading Data
# path = 'task_data.csv' #specifies path to CSV file
# df_original = pd.read_csv(path) # loads data

# df_original.drop(['sample index'], axis = 1, inplace = True) #the column labeled - 'sample index' - was superfluous and was therefore dropped

# #separates data
# y = df_original.class_label
# X = df_original.drop(['class_label'], axis = 1)