# -*- coding: utf-8 -*-
"""q4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-k2lmuKX1rwgkLMjgWfuiBuZIMBADbRS

QUESTION 4:
From the iris dataset, choose the ’petal length’, ’sepal width’ for setosa, versicolor and virginica flowers. Learn a decision boundary for the two features using a single perceptron and SVM. Assume that all the weights of the perceptron are initialized as 0 with the learning rate of 0.01. Draw the decision boundary.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

# Define the path to your Google Drive directory where the files are stored
path='/content/drive/MyDrive/CS21B2028/PR-ML-Lab/datasets/'

df = pd.read_csv(path+'iris.csv')
df

d = {'Petal Length':df['PetalLengthCm'], 'Sepal Width':df['SepalWidthCm'], 'Species':df['Species']}
new_df = pd.DataFrame(data = d)
new_df

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
new_df['Species'] = le.fit_transform(new_df['Species'])
new_df

X = new_df.drop('Species', axis = 1).to_numpy()
y = np.array(new_df['Species'])

"""Multi Class Perceptron Model"""

# Preprocess the data
X = X[y != 0]  # Exclude Setosa
y = y[y != 0]  # Exclude Setosa

# Initialize weights and bias for each class
n_classes = 3  # Three classes (Setosa, Versicolor, Virginica)
n_features = X.shape[1]
w = np.zeros((n_classes, n_features))
b = np.zeros(n_classes)
learning_rate = 0.01
epochs = 100

# Multi-class perceptron training
for epoch in range(epochs):
    for xi, target in zip(X, y):
        for c in range(n_classes):
            update = learning_rate * (int(target == c) - np.dot(xi, w[c]) - b[c])
            w[c] += update * xi
            b[c] += update

# Plot the decision boundaries
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], label="Versicolor")
plt.scatter(X[y == 2][:, 0], X[y == 2][:, 1], label="Virginica")
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], label="Setosa")
plt.xlabel("Sepal Width")
plt.ylabel("Petal Length")

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))

for c in range(n_classes):
    Z = np.dot(np.c_[xx.ravel(), yy.ravel()], w[c]) + b[c]
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.3)

plt.legend()
plt.title("Multi-Class Perceptron Decision Boundaries")
plt.show()

X = new_df.drop('Species', axis = 1).to_numpy()
y = np.array(new_df['Species'])

"""SVM Decision Boundary"""

# Step 3: Preprocess the data
# Assign labels 0 and 1 for the first two classes (setosa and versicolor)
X = X[y != 2]
y = y[y != 2]
y[y == 0] = -1  # Convert labels to -1 and 1

# Step 4: Initialize SVM parameters
weights = np.zeros(X.shape[1])
learning_rate = 0.01
epochs = 1000

# Step 5: Train the SVM model
for epoch in range(epochs):
    for i, x in enumerate(X):
        if y[i] * np.dot(x, weights) <= 1:
            weights = weights + learning_rate * (y[i] * x - 2 * weights)

# Step 6: Plot the decision boundary
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, marker='o', edgecolors='k')

ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 50),
                     np.linspace(ylim[0], ylim[1], 50))
Z = np.dot(np.c_[xx.ravel(), yy.ravel()], weights)
Z = Z.reshape(xx.shape)

plt.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], linestyles=['--', '-', '--'])
plt.title('SVM Decision Boundary')
plt.xlabel('Petal Length')
plt.ylabel('Sepal Width')

plt.show()