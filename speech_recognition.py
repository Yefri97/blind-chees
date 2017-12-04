# ------------------------------------------------------------------------------
#
# blind chees: speech_recognition.py
#
# ------------------------------------------------------------------------------

import numpy as np
# import speech_features as sf
import python_speech_features as sf
import neuralnetwork

class SpeechRecognition():

    def __init__(self, signals, tags):
        """
        """
        m_train = signals.shape[0]

        X = np.zeros(m_train * 1287).reshape(m_train, 1287)

        for i in range(m_train):
            coefs = sf.mfcc(signals[i])
            coefs = coefs.reshape(-1)
            coefs = coefs / 20
            X[i] = coefs

        k_tags = len(tags)
        m = m_train // k_tags
        n_features = X.shape[1]

        self.W = np.zeros(k_tags * n_features).reshape(k_tags, n_features)
        self.B = np.zeros(k_tags).reshape((1, k_tags))
        self.tags = tags
        for i in range(k_tags):
            a, b, c = np.zeros(m * i), np.ones(m), np.zeros(m * (k_tags-i-1))
            Y = np.concatenate((a, b, c))
            w, b = neuralnetwork.train(X.T, Y, 50000, 0.2)
            self.W[i] = w.T
            self.B[0][i] = b

    def predict(self, signal):
        """
        """
        coefs = sf.mfcc(signal)
        coefs = coefs.reshape(-1)
        coefs = coefs / 20

        p = neuralnetwork.sigmoid(np.dot(self.W, coefs.T) + self.B)
        return self.tags[np.argmax(p)]
