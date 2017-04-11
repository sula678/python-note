# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from sympy import *


#隨便取50個點
X = [10, 13, 28, 30, 45.9, 41.3, 10.8, 48.9, 32.8, 19.6, 2.1, 2.6, 5.8, 24, 35.1, 7.6, 32.9, 39.6, 20.5, 23.9, 27.7, 5.1, 15.9, 16.9, 12.6, 3.5, 29.3, 16.7, 27.1, 16, 28.3, 17.4, 1.5, 20, 1.4, 4.1, 43.8, 49.4, 26.7, 37.7, 22.3, 33.4, 27.7, 8.4, 25.7, 22.5, 9.9, 41.5, 15.8, 11.7]
Y = [10, 13, 18, 16, 9.3, 18.5, 12.9, 7.2, 11.8, 13.2, 4.8, 10.6, 8.6, 17.4, 9.2, 9.7, 19, 24.4, 11.3, 14.6, 18, 12.5, 5.6, 15.5, 9.7, 12, 15, 15.9, 18.9, 10.5, 21.4, 11.9, 9.6, 17.4, 9.5, 12.8, 25.4, 14.7, 10.1, 21.5, 16.6, 17.1, 20.7, 12.9, 8.5, 14.9, 10.6, 23.2, 14.8, 9.7]

#https://en.wikipedia.org/wiki/Simple_linear_regression
def simple_linear_regression(X, Y):
    a, b = symbols('a b')
    residual = 0

    #residualSum 求誤差總和
    for i in range(len(X)):
        residual += (Y[i] - (a * X[i] + b)) ** 2

    #展開上面的誤差總和，expand函式來觀看方程式內容
    print expand(residual)

    #求導來得到最小個cost function
    #對a微分
    f1 = diff(residual, a)

    #對b微分
    f2 = diff(residual, b)

    #求聯立方程式的解
    res = solve([f1, f2], [a, b])

    return res[a], res[b]

#這裡所求出的a, b為最小的theta
a, b = simple_linear_regression(X,  Y)

#h就是我們求出來的hypothesis
h = lambda x: a*x + b

#將python函式轉換成numpy所認識的函式
H = np.vectorize(h)

new_X = X
new_Y = H(X)

# render green line
plt.plot(new_X, new_Y, 'b')

plt.plot(X, Y, 'ro')
plt.show()