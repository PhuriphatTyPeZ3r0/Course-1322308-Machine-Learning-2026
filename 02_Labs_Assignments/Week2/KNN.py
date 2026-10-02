
import numpy as np

def knn(X, y, z, k=1):
    d = np.sum((X - z) ** 2, axis=1)
    idx = np.argsort(d)[:k]
    cls, votes = np.unique(y[idx], return_counts=True)
    return cls[np.argmax(votes)]  