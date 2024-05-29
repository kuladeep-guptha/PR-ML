# Consider the 128- dimensional feature 
# vectors given in the “face feature vectors.csv” file.

# Use the following information to design and implement a Bayes Classifier.

# Dataset Specifications:

# Total number of samples = 800

# Number of classes = 2 ( labeled as “male” and “female”)

# Samples from “1 to 400” belongs to class “male”

# Samples from “401 to 800” belongs to class “female”

# Number of samples per class = 400


# Use the following information to design classifier:

# Number of test samples ( first 5 in each class) = 5

# Number of training samples ( remaining 395 in each class) = 395

# Number of dimensions = 128

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('face feature vectors.csv')
d=128
train_data=pd.DataFrame()
test_data=pd.DataFrame()

d1=data[0:5]
d2=data[400:405]
test_data=pd.concat([d1,d2])

d3=data[5:400]
d4=data[405:800]
train_data=pd.concat([d1,d2])

mean1=[]
for i in range(128):
    a=str(i)
    mean1.append(np.mean(d3[a]))
mean1=np.array(mean1)

mean2=[]
for i in range(128):
    a=str(i)
    mean2.append(np.mean(d4[a]))
mean2=np.array(mean2)

d6=pd.DataFrame()
d7=pd.DataFrame()

d6=d3.iloc[:,2:130]
d7=d4.iloc[:,2:130]

cov1=d6.cov()
cov2=d7.cov()

def discriminant(x,mean,cov):
    a=1/((2*math.pi)**(d/2))
    b=1/((np.linalg.det(cov))**(1/2))
    c=-1/2*(np.dot(np.dot((x-mean).T,np.linalg.inv(cov)),(x-mean)))
    return a*b*math.exp(c)  

k=[]
for i in range(len(test_data)):
    x=test_data.iloc[i][0:130]
    x=np.array(x)
    X=x[2:128]
    X=np.array(X)
    g1=discriminant(x,mean1,cov1)
    g2=discriminant(x,mean2,cov2)
    if g1>g2:
        k.append([x[0],'male'])
    else:
        k.append([x[0],'female'])



    





