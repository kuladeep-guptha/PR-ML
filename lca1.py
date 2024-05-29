# # Consider the 128- dimensional feature vectors (d=128) given in the “gender.csv” file. (2 classes, male and female)

# # a) Use PCA to reduce the dimension from d to d‟. (Here d=128).

# # b) Display the eigenvalue based on increasing order, select the d‟ of the corresponding eigenvector which is the appropriate dimension d‟ ( select d‟ S.T first 95% of λ values of the covariance matrix are considered).

# # c) Use d‟ features to classify the test cases (use any classification algorithm taught in class like Bayes classifier, minimum distance classifier, and so on).


# # Dataset Specifications:

# # Total number of samples = 800

# # Number of classes = 2 (labeled as “male” and “female”)

# # Samples from “1 to 400” belongs to class “male”

# # Samples from “401 to 800” belongs to class “female”

# # Number of samples per class = 400

# # Number of dimensions = 128

# # Use the following information to design classifier:

# # Number of test cases (first 10 in each class) = 20

# # Number of training feature vectors ( remaining 390 in each class) = 390

# # Number of reduced dimensions = d‟ (map 128 to d‟ features vector)


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # Importing the dataset
# data=pd.read_csv('gender.csv')
# x=data.iloc[:10,:].values
# y=data.iloc[400:410,:].values
# test_data=pd.DataFrame()
# train_data=pd.DataFrame()
# test_data=pd.concat([x,y])
# x=data.iloc[10:400,:].values
# y=data.iloc[410:800,:].values
# train_data=pd.concat([x,y])

# #calculating mean vector
# mean1=[]
# for i in range(128):
#     a=str(i)
#     mean1.append(np.mean(x.iloc[:,i]))
# mean1=np.array(mean1)

# #calculate covariance matrix





import numpy as np
import pandas as pd
dataset = pd.read_csv('gender.csv')
mean = np.mean(dataset.iloc[:, 2:], axis=0)

cov_matrix = dataset.iloc[:, 2:].cov()

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort eigenvalues in descending order
indices = np.argsort(eigenvalues)[::-1]
eigenvalues_sorted = eigenvalues[indices]
eigenvectors_sorted = eigenvectors[:, indices]

total_variance = np.sum(eigenvalues_sorted)

variance_threshold = 0.95
cumulative_variance = np.cumsum(eigenvalues_sorted) / total_variance
k = np.argmax(cumulative_variance >= variance_threshold) + 1  # Add 1 because indexing starts from 0

selected_eigenvectors = eigenvectors_sorted[:, :k]
selected_eigenvalues = eigenvalues_sorted[:k]

data_reduced = np.dot(dataset.iloc[:, 2:]-mean, selected_eigenvectors)
# data_reduced.shape
test = data_reduced[390:400]
test = np.concatenate([test, data_reduced[790:800]])

train = data_reduced[0:390]
train = np.concatenate([train, data_reduced[400:790]])
means = [np.mean(train[0:390], axis=0), np.mean(train[390:], axis=0)]

predictions = []

for i in range(test.shape[0]):
    min_dist = float('inf')
    prediction = -1

    for j in range(2):
        dist = np.linalg.norm(test[i] - means[j])

        if dist < min_dist:
            min_dist = dist
            prediction = j

    predictions.append(prediction)

correct = 0

for i in range(len(predictions)):
    if i<10 and predictions[i] == 0:
        correct += 1
    elif i>10 and predictions[i] == 1:
        correct += 1
    else:
        correct -= 1

print('Accuracy : ', correct/test.shape[0])
