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
    plt.pause(1)


k = 3
C = X[np.random.permutation(len(X))[:k]]
Cold = C.copy()
while True:
    plot(C)
    D = np.zeros((len(X), k))
    for i in range(k):
        D[:, i] = np.mean((X - C[i])**2, axis=1)
    idx = np.argmin(D, axis=1)
    Cold = C.copy()
    for i in range(k):
        C[i] = np.mean(X[idx == i])
    if np.sum(np.abs(Cold - C)) == 0:
        print('finished')
        break
