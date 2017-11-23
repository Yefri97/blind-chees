import numpy as np

def coeficients(r, a):
    """
    Get the Mel Frecuency Cepstral Coeficients from the input audio.

    Arguments:
    a -- An audio type wav.

    Return:
    c -- A numpy array with the mfcc from the audio.
    """

    fms = 0.02                                     # Frame time in mili-seconds
    fstp = 0.01                                     # Frame step in mili-seconds
    fsr = fms * r                                       # Sampled rate for frame
    fstpr = fstp * r                                     # Sampled rate for step

    a = np.append(a, np.zeros(fstpr - (a.shape[0] - fsr) % fstpr))  # Fill zeros

    stp = 0
    while stp + fsr - 1 < a.shape[0]:                           # For each frame
        s = a[stp : stp + fsr]                                           # Frame

        """ Fourier Transform """
        S = fft(s)                                      # Fast Fourier Transform
        P = S ** 2 / s.shape[0]                                 # Power spectral
        """ Apply the mel filterbank """
        mfb = mel_filterbank()
        c = np.dot(mfb.T, P)
        """ Take the log """
        c = np.log(c)
        """ Discrete Cosine Transform """
        c = dct(c)

        stp += fstpr                                                # Next Frame
