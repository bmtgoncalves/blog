#!/usr/bin/env python

import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import seaborn

# Basic implementation of Preferential Attanchment model
N = 1000000

def BarabasiAlbert(N):
    net = np.zeros(2*N, dtype='int')

    # Edges represented by sequence of nodes
    net[:6] = [0, 1, 1, 2, 2, 3]

    # Generate the network
    for i in xrange(3, N):
        pos = np.random.randint(0, i)
        net[2*i] = i
        net[2*i+1] = net[pos]

    return net

net = BarabasiAlbert(N)

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
plt.savefig('preferential.png')
plt.close()

# Statistics:
print "=== Preferential Attantchment ==="
print "Number of nodes:", N
print "Average degree:", np.mean(degrees.values())
print "Standard deviation:", np.std(degrees.values())

degrees = degrees.values()
degrees.sort()

Top = np.sum(degrees[-int(0.01*N):])/np.sum(degrees, dtype='float')
print "Fraction of connections in the the top 1% of nodes:", Top


def ErdosRenyi(N, m=N):
    net = np.zeros(2*m, dtype='int')

    for i in xrange(m):
        while True:
            node1, node2 = np.random.randint(0, N, 2)

            # No self loops allowed
            if node1 != node2:
                break

        net[2*i] = node1
        net[2*i+1] = node2

    return net

net2 = ErdosRenyi(N)
degrees2 = Counter(net2)
Pk2 = Counter(degrees2.values()).items()

# Sort values and normalize
Pk2.sort(key=lambda x: x[0])
Pk2 = np.asarray(Pk2, dtype='float')
Pk2.T[1] /= np.sum(Pk2.T[1])

# Plot on log-log scale
plt.plot(Pk2.T[0], np.log(Pk2.T[1]), 'r-')
plt.xlabel('k')
plt.ylabel('Log[P[k]]')
plt.savefig('random.png')
plt.close()

# Statistics:
print "=== Random Attatchment ==="
print "Number of nodes:", N
print "Average degree:", np.mean(degrees2.values())
print "Standard deviation:", np.std(degrees2.values())

degrees2 = degrees2.values()
degrees2.sort()

Top = np.sum(degrees2[-int(0.01*N):])/np.sum(degrees2, dtype='float')
print "Fraction of connections in the the top 1% of nodes:", Top
