# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd
from sympy import *
import matplotlib.pyplot as plt


#把鳶尾花讀進來並列出前五項跟後五項
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

#取出第一個特徵花萼長跟第三個特徵花瓣長指定給x，共取前100資料
X = df.iloc[0:100, 0].values
print X
#把前100項中每一項的第4屬性(花屬性, setosa or versicolor)指定給y
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

#x = np.array([1, 2, 2.5, 3])
#y = np.array([1.5, 3, 4.1, 2.5])
plt.scatter(X, y, color='red', marker='o', label='setosa')
plt.xlabel('test tpetal length')
plt.ylabel('test sepal length')
plt.legend(loc='upper left')
plt.show()



"""
# Code source: Jaques Grobler
# License: BSD 3 clause


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

# Load the diabetes dataset
# 讀取內建的糖尿病數據集
diabetes = datasets.load_diabetes()


# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
"""