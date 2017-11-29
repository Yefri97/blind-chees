import numpy as np
import scipy.io.wavfile
# import python_speech_features as sf
import mfcc
import neuralnetwork

k = 8
kk = k + k
X = np.zeros(kk * 1287).reshape(kk, 1287)
Y = np.concatenate((np.zeros(k), np.ones(k)))

for i in range(kk):
    print(i, end=" ")
    word = 'animal' if i < k else 'humano'
    filename = 'audios/prueba1/' + word + str(i % k + 1) + '.wav'
    rate, data = scipy.io.wavfile.read(filename)
    audio = data.T[0]
    coefs = mfcc.getcoeficients(rate, audio)
    #coefs = sf.mfcc(audio)
    #coefs = coefs.reshape(-1)
    #print(np.amax(coefs))
    X[i] = coefs / 500

X = X.T

w, b = neuralnetwork.model(X, Y, num_iterations = 50000, learning_rate = 0.1)

A = neuralnetwork.sigmoid(np.dot(w.T, X) + b)
cost = - (Y * np.log(A) + (1 - Y) * np.log(1 - A)).sum() / kk

print(A > 0.5)
print(cost)

for i in range(6):
    filename = 'audios/prueba1/test' + str(i + 1) + '.wav'
    rate, data = scipy.io.wavfile.read(filename)
    audio = data.T[0]
    coefs = mfcc.getcoeficients(rate, audio)
    #coefs = sf.mfcc(audio)
    #coefs = coefs.reshape(-1)
    #print(np.amax(coefs))
    coefs = coefs / 500
    predict = neuralnetwork.sigmoid(np.dot(w.T, coefs.T) + b)
    print(predict > 0.5)
