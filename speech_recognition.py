# ------------------------------------------------------------------------------
#
# blind chees: speech_recognition.py
#
# ------------------------------------------------------------------------------

# import speech_features as sf
import neuralnetwork
import numpy as np
import python_speech_features as sf
import sounddevice as sd
import scipy.io.wavfile

class SpeechRecognition():

    def __init__(self):
        print("Creating the Speech Recognition...")
        self.m = 5 # 10
        self.k_tags = 3 # 22
        self.n_features = 1287
        self.m_train = self.k_tags * self.m # 220
        self.tags = ["caballo", "torre", "alfil"]

        X = np.zeros(self.m_train * 16000).reshape(self.m_train, 16000)

        for i in range(self.m_train):               # Load the audios of the data set
            word = self.tags[i // self.m]
            filename = 'audios/' + word + str(i % self.m) + '.wav'
            rate, audio = scipy.io.wavfile.read(filename)
            signal = self.process(audio)
            X[i] = signal

        print("Training the neural network...")
        self.train(X)

    def train(self, signals):
        """
        """
        X = np.zeros(self.m_train * 1287).reshape(self.m_train, 1287)

        for i in range(self.m_train):
            coefs = sf.mfcc(signals[i])
            coefs = coefs.reshape(-1)
            coefs = coefs / 20
            X[i] = coefs

        self.W = np.zeros(self.k_tags * self.n_features).reshape(self.k_tags, self.n_features)
        self.B = np.zeros(self.k_tags).reshape((1, self.k_tags))
        for i in range(self.k_tags):
            a, b, c = np.zeros(self.m * i), np.ones(self.m), np.zeros(self.m * (self.k_tags-i-1))
            Y = np.concatenate((a, b, c))
            w, b = neuralnetwork.train(X.T, Y, 50000, 0.2)
            self.W[i] = w.T
            self.B[0][i] = b

    def process(self, audio):
        signal = audio.T[0] if len(audio.shape) == 2 else audio
        if (signal.size > 16000):
            signal = signal[:16000]
        if (signal.size < 16000):
            signal = np.append(signal, np.zeros(16000 - signal.size))
        return signal

    def predict(self, signal):
        """
        """
        coefs = sf.mfcc(signal)
        coefs = coefs.reshape(-1)
        coefs = coefs / 20

        p = neuralnetwork.sigmoid(np.dot(self.W, coefs.T) + self.B)
        return self.tags[np.argmax(p)]

    def listen(self):
        print("Press enter to record...")
        input()
        fs = 16000
        duration = 3
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()

        signal = self.process(audio[fs:2*fs])

        return self.predict(signal)
