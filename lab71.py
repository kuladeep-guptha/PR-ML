# Find and plot the decision boundary between class ω1 and ω2. Assume P(ω1) = P(ω2).

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

w1 = [(1,6),(3,4),(3,8),(5,6)]
w2 = [(3,0),(1,-2),(3,-4),(5,-2)]

l1=[x[0] for x in w1]
l2=[x[1] for x in w1]

l3=[x[0] for x in w2]
l4=[x[1] for x in w2]

mean1=[sum(l1)/len(l1),sum(l2)/len(l2)]
mean2=[sum(l3)/len(l3),sum(l4)/len(l4)]

mat1=np.stack((l1, l2), axis = 0)
mat2=np.stack((l3, l4), axis = 0)
cov1=np.cov(mat1)
cov2=np.cov(mat2)

print(cov1)
print(cov2)

#case1: g(x)=w^T*x+w0
#w=mean/sigma^2
#w0=-mean^T*mean/2*sigma^2+ln(p(w))
mean1=np.array(mean1)
mean2=np.array(mean2)
mean1=mean1.reshape(-1,1)
mean2=mean2.reshape(-1,1)

a=1/(cov1[0][0])
w1=a*mean1
b=-1/2*(cov1[0][0])
c=np.dot(mean1.T,mean1)
w10=b*c

dict1={'x1':0,'x2':0}

dict1['x1']=mean1[0][0]
dict1['x2']=mean1[1][0]


a=1/(cov2[0][0])
w2=a*mean2
b=-1/2*(cov2[0][0])
c=np.dot(mean2.T,mean2)
w20=b*c

dict2={'x1':0,'x2':0}

dict2['x1']=mean2[0][0]
dict2['x2']=mean2[1][0]

dict3={'x1':0,'x2':0,'c':0}

dict3['x1']=dict1['x1']-dict2['x1']
dict3['x2']=dict1['x2']-dict2['x2']
dict3['c']=w10-w20








    
    
    
    
    













