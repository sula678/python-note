# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#把鳶尾花資料從檔案中讀進來
SCRIPT_PATH = os.path.dirname(os.path.abspath( __file__ ))
df = pd.read_csv(SCRIPT_PATH + "/iris_dataset.csv", header=None)

"""
#列出前五項跟後五項
top = df.head()
bottom = df.tail()
print pd.concat([top, bottom])
"""

#把前100項中每一項的第4屬性(花屬性, setosa or versicolor)指定給y
y = df.iloc[:100, 4].values

#把setosa標示為-1，versicolor標示為1
y = np.where(y == 'Iris-setosa', -1, 1)

#取出第一個特徵花萼長跟第三個特徵花瓣長指定給x，共取前100資料
X = df.iloc[:100, [0, 2]].values

#畫圖
plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')
plt.show()