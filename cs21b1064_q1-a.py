import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("iris.csv")
x=data.iloc[:,0:3].values
y=data.iloc[:,-1].values

test_data=x.iloc[0:4,:].values
train_data=data.iloc[4:,:].values



