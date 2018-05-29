import sounddevice as sd
import scipy.io.wavfile
import numpy as np

tags0 = ['rey', 'dama', 'alfil', 'caballo', 'torre', 'peon', 'peon', 'peon']
tags1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
tags2 = ['1', '2', '3', '4', '5', '6', '7', '8']

perm0 = np.random.permutation(8)
perm1 = np.random.permutation(8)
perm2 = np.random.permutation(8)

fs = 16000
duration = 4

for i in range(5):
    print("Persona" + str(i) + ":")
    for k in range(8):
        print("Say " + tags0[perm0[k]] + " " + tags1[perm1[k]] + " " + tags2[perm2[k]] + ":")
        input()
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()

        signal0 = audio[fs:2*fs]
        signal1 = audio[2*fs:3*fs]
        signal2 = audio[3*fs:4*fs]

        scipy.io.wavfile.write("audios/persona" + str(i) + "/" + tags0[perm0[k]] + ".wav", fs, signal0)
        scipy.io.wavfile.write("audios/persona" + str(i) + "/" + tags1[perm1[k]] + ".wav", fs, signal1)
        scipy.io.wavfile.write("audios/persona" + str(i) + "/" + tags2[perm2[k]] + ".wav", fs, signal2)
