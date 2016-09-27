#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


filename = "celegans.txt"
N = 297
m = 0.15
iter = 1000

# Read the adjacency matrix from file
A = np.zeros((N, N))

for line in open(filename):
    node_i, node_j = line.strip().split()

    node_i = int(node_i)
    node_j = int(node_j)

    A[node_i, node_j] = 1

v = np.ones(N)


# Compute the "Google" Matrix from the adjacency matrix.
def Google_Matrix(A, m):
    N = A.shape[0]
    v = np.ones(N)

    KT = np.dot(A.T, v)

    for i in range(N):
        A.T[i] = A.T[i]/KT[i]

    S = np.ones((N, N))/N
    G = (1-m)*A+m*S

    return G


# Perform the power method for "iter" iterations
def Power_Method(G, iter):
    N = G.shape[0]
    x0 = np.ones(N)/N

    for i in range(iter):
        x0 = np.dot(G, x0)

    return x0

G = Google_Matrix(A, m)
x0 = Power_Method(G, iter)

# in-degree
deg = A.sum(axis=1)

plt.plot(deg, x0, 'b*')
plt.xlabel('in-degree')
plt.ylabel('PageRank')
plt.savefig('PageRank.png')
plt.close()
