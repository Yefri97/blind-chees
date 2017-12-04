import numpy as np
import scipy.io.wavfile
from speech_recognition import SpeechRecognition

def process(audio):
    signal = audio.T[0] if len(audio.shape) == 2 else audio
    if (signal.size > 16000):
        signal = signal[:16000]
    if (signal.size < 16000):
        signal = np.append(signal, np.zeros(16000 - signal.size))
    return signal

m = 5 # 10
k_tags = 3 # 22
m_train = k_tags * m # 220
tags = ["caballo", "torre", "alfil"]

X = np.zeros(m_train * 16000).reshape(m_train, 16000)

for i in range(m_train):
    word = tags[i // m]
    filename = 'audios/' + word + str(i % m) + '.wav'
    rate, audio = scipy.io.wavfile.read(filename)
    signal = process(audio)
    X[i] = signal

walker = SpeechRecognition(X, tags)

for i in range(9):
    rate, audiorec = scipy.io.wavfile.read('audios/test' + str(i) + '.wav')
    signal = process(audiorec)
    print(walker.predict(signal))
