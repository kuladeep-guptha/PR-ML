# NOTE :- You can make use of the built in command to find the covariance matrix, where normalization is
# done using 1/ n-1. No need to plot the decision boundary for this lab, it can be done for the next lab.

# Implement Bayes Classifier for Iris Dataset.

# Dataset Specifications:

# Total number of samples = 150

# Number of classes = 3 (Iris setosa, Iris virginica, and Iris versicolor)

# Number of samples in each class = 50

# Use the following information to design classifier:

# Number of training feature vectors ( first 40 in each class) = 40

# Number of test feature vectors ( remaining 10 in each class) = 10

# Number of dimensions = 4

# Feature vector = <sepal length, sepal width, petal length, petal width>

# If the samples follow a multivariate normal density, find the accuracy of
# classification for the test feature vectors.
#find the mean vector
#find the covariance matrix
#find the discriminant function
#plot the accuracy for separate classes overall performance

import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('iris.csv')
d=4
train_data=pd.DataFrame()
test_data=pd.DataFrame()
d1=data[data['Species']=='Iris-setosa'][0:40]
d2=data[data['Species']=='Iris-versicolor'][0:40]
d3=data[data['Species']=='Iris-virginica'][0:40]
train_data=train_data.concat([d1,d2,d3])
test_data=data.loc[list(set(data.index)-set(train_data.index))]

d4=d1['SepalLengthCm']
d5=d1['SepalWidthCm']
d6=d1['PetalLengthCm']
d7=d1['PetalWidthCm']

mean1=np.array([np.mean(d4),np.mean(d5),np.mean(d6),np.mean(d7)])
d1.drop(['Id','Species'],axis=1,inplace=True)
cov1=d1.cov()
print(cov1)

d4=d2['SepalLengthCm']
d5=d2['SepalWidthCm']
d6=d2['PetalLengthCm']
d7=d2['PetalWidthCm']

mean2=np.array([np.mean(d4),np.mean(d5),np.mean(d6),np.mean(d7)])
d2.drop(['Id','Species'],axis=1,inplace=True)
cov2=d2.cov()
print(cov2)

d4=d3['SepalLengthCm']
d5=d3['SepalWidthCm']
d6=d3['PetalLengthCm']
d7=d3['PetalWidthCm']

mean3=np.array([np.mean(d4),np.mean(d5),np.mean(d6),np.mean(d7)])
d3.drop(['Id','Species'],axis=1,inplace=True)
cov3=d3.cov()
print(cov3)

#find apriori probability for each class
p1=len(d1)/len(train_data)
p2=len(d2)/len(train_data)
p3=len(d3)/len(train_data)








#bayes classifier






#discriminant function
def g(x,mean,cov):
    a=1/((2*math.pi)**(d/2))
    b=1/((np.linalg.det(cov))**(1/2))
    c=-1/2*(np.dot(np.dot((x-mean).T,np.linalg.inv(cov)),(x-mean)))
    return a*b*math.exp(c)

    


k=[]
for i in range(len(test_data)):
    x=test_data.iloc[i][0:5]
    X=np.array(x.SepalLengthCm,x.SepalWidthCm,x.PetalLengthCm,x.PetalWidthCm)
    if(g(X,mean1,cov1)>g(X,mean2,cov2) and g(X,mean1,cov1)>g(X,mean3,cov3)):
        k.append([x.Id,'Iris-setosa'])
        print("Iris-setosa")
    elif(g(X,mean2,cov2)>g(X,mean1,cov1) and g(X,mean2,cov2)>g(X,mean3,cov3)):
        k.append([x.Id,'Iris-versicolor'])
        print("Iris-versicolor")
    else:
        k.append([x.Id,'Iris-virginica'])
        print("Iris-virginica")
        
k=pd.DataFrame(k,columns=['Id','Species'])
k.to_csv('output.csv',index=False)

#accuracy
count=0
for i in range(len(test_data)):
    if(test_data.iloc[i]['Species']==k.iloc[i]['Species']):
        count=count+1
print("Accuracy is ",count/len(test_data))




            








    
    



