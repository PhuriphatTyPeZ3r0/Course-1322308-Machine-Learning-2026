import numpy as np
import matplotlib.pyplot as plt

X = np.vstack((np.random.randn(15, 2),
               np.random.randn(15, 2)+np.array([3.8, 3.8]),
               np.random.randn(15, 2)+np.array([-3.8, -3.8]),))

def plot(C):
    plt.clf()
    plt.plot(X[:15,0],X[:15,1], '.r')
    plt.plot(X[15:30,0],X[15:30,1], '.g')
    plt.plot(X[30:,0],X[30:,1], '.b')
    plt.plot(C[:,0],C[:,1], 'ok')
    plt.pause(.1)

K = 3
m = 2
mu = np.random.rand(len(X),K)
D = np.zeros((len(X), K))
C = np.zeros((K, X.shape[1]))
Cold = C.copy()
told = 1.0
while True:
    s = np.sum(mu,axis=1)
    for i in range(len(mu)):
        mu[i] = mu[i] / s[i]
    for k in range(K):
        C[k] = np.dot(mu[:, k] ** m, X) / mu[:, k].sum()
        D[:, k] = np.sqrt(np.mean((X - C[k]) ** 2, axis=1))  # Euclidean distance
    plot(C)
    mu = (1 / D) ** (2 / (m-1))
    t = np.mean(np.abs(C - Cold))
    print(t)

    if np.abs(t-told) < 1e-6:
        print('finished')
        break
    told = t