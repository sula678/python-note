# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from adalineGD import AdalineGD

#把鳶尾花讀進來並列出前五項跟後五項
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
#top = df.head()
#bottom = df.tail()
#print pd.concat([top, bottom])

#把前100項中每一項個花屬性(setosa or versicolor)指定給y
y = df.iloc[0:10, 4].values

#把setosa標示為-1，versicolor標示為1
y = np.where(y == 'Iris-setosa', -1, 1)

#取出第一個特徵花萼長跟第三個特徵花瓣長指定給x
X = df.iloc[0:10, [0, 2]].values

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
ada1 = AdalineGD(n_iter=10, eta=0.01).fit(X, y)
ax[0].plot(range(1, len(ada1.cost_) +1), np.log10(ada1.cost_), marker='o')
ax[0].set_xlabel('Epochs')
ax[0].set_ylabel('log(Sum-squared-error)')
ax[0].set_title('Adaline - Learning rate 0.01')

ada2 = AdalineGD(n_iter=10, eta=0.0001).fit(X, y)
ax[1].plot(range(1, len(ada2.cost_) +1), ada2.cost_, marker='o')
ax[1].set_xlabel('Epochs')
ax[1].set_ylabel('log(Sum-squared-error)')
ax[1].set_title('Adaline - Learning rate 0.0001')

plt.show()
