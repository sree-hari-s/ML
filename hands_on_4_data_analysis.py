# -*- coding: utf-8 -*-
"""Hands-On: 4 Data Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ggk0JSIBn0AHbKh7RLMbVQo-peKCgBC5
"""

#Import the required packages and read data from housing.csv in a dataframe
import pandas as pd
data=pd.read_csv('housing.csv')
data.head()

#Take a look at the shape of data.
data.shape

#Take a look at the number of cells that are null in each column.
data.isnull().sum()

#Take a look at the mean, standard deviation, minimum and maximum values is each column.

data.mean()

data.std()

data.min()

data.max()

#Use the describe method to check all statistically significant information about data.

data.describe()

