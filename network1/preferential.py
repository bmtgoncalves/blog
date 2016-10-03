#!/usr/bin/env python

import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

# Basic implementation of Preferential Attanchment model
N = 1000000
net = np.zeros(2*N, dtype='int')

# Edges represented by sequence of nodes
net[:6] = [0, 1, 1, 2, 2, 3]

# Generate the network
for i in xrange(3, N):
    pos = np.random.randint(0, i)
    net[2*i] = i
    net[2*i+1] = net[pos]

# Calculate the degree distribution
# Degree of each node is the number of times it occurs
degrees = Counter(net)
Pk = Counter(degrees.values()).items()

# Sort values and normalize
Pk.sort(key=lambda x: x[0])
Pk = np.asarray(Pk, dtype='float')
Pk.T[1] /= np.sum(Pk.T[1])

# Plot on log-log scale
plt.loglog(Pk.T[0], Pk.T[1], 'r-')
plt.xlabel('k')
plt.ylabel('P[k]')
plt.show()
