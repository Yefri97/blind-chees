import numpy as np

def dft(x):
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def fft(x):
    n = x.shape[0]
    if n == 1:
        return x
    wi = np.exp(-2j * np.pi * np.arange(n) / n)
    x_even = fft(x[::2])
    x_odd = fft(x[1::2])
    y0 = x_even + wi[:n//2] * x_odd
    y1 = x_even + wi[n//2:] * x_odd
    y = np.concatenate((y0, y1))
    return y

def dct(x):
    N = x.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.cos(-2 * np.pi * k * n / N)
    return np.dot(M, x)
