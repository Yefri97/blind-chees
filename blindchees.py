from speech_recognition import SpeechRecognition
import sounddevice as sd
import numpy as np
import scipy.io.wavfile

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

print("Training...")

walker = SpeechRecognition(X, tags)

while True:
    print("Recording...\n")

    fs = 16000
    duration = 3
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()

    audio = audio[fs:2*fs]

    sd.play(audio, fs)
    sd.wait()
    sd.stop()

    print("Prediction --> ", end="")
    print(walker.predict(process(audio)))

    print("\n\n")

"""
for i in range(9):
    rate, audiorec = scipy.io.wavfile.read('audios/test' + str(i) + '.wav')
    signal = process(audiorec)
    print(walker.predict(signal))
"""
