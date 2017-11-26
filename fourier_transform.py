# --------------------------------------------------------------
# blind chees: fourier_transform.py
# --------------------------------------------------------------

import numpy as np

def dft(s):
    """
    Get the Discrete Fourier Transform from the input signal.
    Time complexity: O(n ^ 2)

    Arguments:
    s -- A numpy array representing the signal.

    Return:
    S -- A numpy array with the dft from the signal.
    """
    N = s.shape[0]
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    S = np.dot(M, x)
    return S

def fft(s):
    """
    Get the Discrete Fourier Transform using the fast
    Cooley - Tukey Algorithm from the input signal.
    Time complexity: O(n * log(n))
    note: n has to be a power of two

    Arguments:
    s -- A numpy array representing the signal.

    Return:
    S -- A numpy array with the fft from the signal.
    """
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
