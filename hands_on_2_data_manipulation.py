# -*- coding: utf-8 -*-
"""Hands-On: 2:Data Manipulation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zIS6I88yX7z05YDQ6s8PFX01s88oQZfb
"""

#Import the required packages and read the data.
import numpy as np
import pandas as pd

data=pd.read_csv('housing.csv')
data.head()

#Analyze the shape of data.
data.shape

#Extract a subset of data using iloc.
data.iloc[:5,:]

data.iloc[2:5,:2]

data.iloc[2:4,1:2]

#Extract a subset of data using loc.
data.loc[:5,'LSTAT':'MEDV']

#Change all values in LSTAT column to 1.
data['LSTAT']=1
data.head()

#Apply function to change LSTAT value to its double (multiply by 2).
data['LSTAT']=data['LSTAT'].apply(lambda x:x*2)
data

