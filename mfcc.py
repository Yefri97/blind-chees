import numpy as np
import fourier_transform as ft

def mel(f):
    return 1125 * np.log(1 + f / 700)

def imel(m):
    return 700 * (np.exp(m / 1125) - 1)

def melfilterbank(nfilt, nfft, samplerate):
    lower, upper = 500, 20000
    ml = np.linspace(mel(lower), mel(upper), num=nfilt+2)
    h = imel(ml)
    f = np.floor((nfft + 1) * h / samplerate)
    H = np.zeros([nfilt,nfft // 2 + 1])
    for m in range(0, nfilt):
        for k in range(int(f[m]), int(f[m + 1])):
            H[m,k] = (k - f[m]) / (f[m + 1] - f[m])
        for k in range(int(f[m + 1]), int(f[m + 2])):
            H[m,k] = (f[m + 2] - k) / (f[m + 2] - f[m + 1])
    return H

def coeficients(rate, audio):
    """
    Get the Mel Frecuency Cepstral Coeficients from the input audio.

    Arguments:
    rate -- Sample rate of the input audio.
    audio -- A numpy array with the info of the audio.

    Return:
    coefs -- A numpy array with the mfcc from the audio.
    """

    frame_length = 0.02                           # Frame length in mili-seconds
    frame_step = 0.01                               # Frame step in mili-seconds
    nsamples_frame = int(frame_length * rate)      # Number of samples for frame
    nsamples_step = int(frame_step * rate)          # Number of samples for step

    k = nsamples_step - (audio.shape[0] - nsamples_frame) % nsamples_step
    audio = np.append(audio, np.zeros(k))                           # Fill zeros

    coefs = np.array([])

    step = 0
    while step + nsamples_frame - 1 < audio.shape[0]:           # For each frame
        frame = audio[step : step + nsamples_frame]                      # Frame
        k = int(2 ** np.ceil(np.log2(nsamples_frame)) - nsamples_frame)
        frame = np.concatenate((frame, np.zeros(k)))         # Fill power of two

        """ Fast Fourier Transform """
        s = frame * np.hamming(frame.size)          # Multiply by hamming window
        S = ft.fft(s)                                   # Fast Fourier Transform
        P = np.absolute(S) ** 2 / s.size                        # Power spectral
        """ Apply the mel filterbank """
        H = melfilterbank(26, P.size, rate)
        a = np.dot(P, H.T)
        """ Take the log """
        b = np.log(a)
        """ Discrete Cosine Transform """
        c = ft.dct(b)
        coefs = np.append(coefs, c[:c.size // 2])

        step += nsamples_step                                       # Next Frame

    return coefs
