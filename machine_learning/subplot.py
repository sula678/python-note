# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

def g(t):
    return np.exp(-t) * np.sin(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

#subplot(row數量, col數量, 第幾個num)
plt.subplot(3,1,1)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(3,1,2)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.subplot(3,1,3)
plt.plot(t1, g(t1), 'g^', t2, g(t2), 'k')
plt.show()