import numpy as np

def sigmoid(z):
    s = 1 / (1 + np.exp(-z))
    return s

def initialize_with_zeros(dim):
    w = np.zeros(dim).reshape((dim, 1))
    b = 0
    return w, b

def propagate(w, b, X, Y):
    m = Y.size
    A = sigmoid(np.dot(w.T, X) + b)
    dw = np.dot(X, (A - Y).T) / m
    db = (A - Y).sum() / m
    return dw, db

def model(X, Y, num_iterations = 2000, learning_rate = 0.5):
    w, b = initialize_with_zeros(X.shape[0])
    for i in range(num_iterations):
        dw, db = propagate(w, b, X, Y)
        w = w - learning_rate * dw
        b = b - learning_rate * db
    return w, b
"""
data = np.genfromtxt("data.txt", delimiter=",")

m = data.shape[0]
n = data.shape[1] - 1

X = data[:, :n].T
Y = data[:, n].reshape((1, m))

w, b = model(X, Y, num_iterations = 500, learning_rate = 0.1)

A = sigmoid(np.dot(w.T, X) + b)
print(A > 0.5)
cost = - (Y * np.log(A) + (1 - Y) * np.log(1 - A)).sum() / m

print("b = " + str(b))
print("w = " + str(w))
print("cost = " + str(cost))
"""
