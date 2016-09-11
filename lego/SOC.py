#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

N = 1000
np.random.seed(1234)


def uncorrelated(data, steps=10):
    N = len(data)

    for i in range(steps*N):
        pos = np.random.randint(N)

        data[pos] = np.random.random()

    return data


def minimum(data, steps=10):
    N = len(data)

    for i in range(steps*N):
        pos = np.argmin(data)

        data[pos] = np.random.random()

    return data


def bak_sneppen(data, steps=10):
    N = len(data)

    for i in range(steps*N):
        pos = np.argmin(data)

        data[(pos-1) % N] = np.random.random()
        data[pos] = np.random.random()
        data[(pos+1) % N] = np.random.random()

    return data


data1 = uncorrelated(np.random.random(N))
data2 = minimum(np.random.random(N))
data3 = bak_sneppen(np.random.random(N))

plt.plot(data1, 'r+')
plt.plot(data2, 'g*')
plt.xlabel('Position')
plt.ylabel('value')
plt.ylim(0, 1)
plt.legend(['Uncorrelated', 'Minimum'], loc='lower right')
plt.savefig('Fig1.png')

plt.plot(data3, 'b.')
plt.legend(['Uncorrelated', 'Minimum', 'Bak-Sneppen'], loc='lower right')
plt.savefig('Fig2.png')
plt.close()
