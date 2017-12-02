import numpy as np
import scipy.io.wavfile
import python_speech_features as sf
import mfcc
import neuralnetwork

k = 10
kk = k + k
X = np.zeros(kk * 1287).reshape(kk, 1287)
Y = np.concatenate((np.zeros(k), np.ones(k)))

for i in range(kk):
    #print(i)
    word = 'caballo' if i < k else 'torre'
    filename = 'audios/' + word + str(i % k) + '.wav'
    rate, data = scipy.io.wavfile.read(filename)
    audio = data.T[0]

    #coefs = mfcc.getcoeficients(rate, audio)
    #X[i] = coefs / 200

    coefs = sf.mfcc(audio)
    coefs = coefs.reshape(-1)
    X[i] = coefs / 20


X = X.T

w, b = neuralnetwork.model(X, Y, num_iterations = 50000, learning_rate = 0.2)

A = neuralnetwork.sigmoid(np.dot(w.T, X) + b)
cost = - (Y * np.log(A) + (1 - Y) * np.log(1 - A)).sum() / kk

print(A > 0.5)
print(cost)

for i in range(4):
    filename = 'audios/test' + str(i) + '.wav'
    rate, data = scipy.io.wavfile.read(filename)
    audio = data.T[0]

    #coefs = mfcc.getcoeficients(rate, audio)
    #coefs = coefs / 200

    coefs = sf.mfcc(audio)
    coefs = coefs.reshape(-1)
    coefs = coefs / 20

    predict = neuralnetwork.sigmoid(np.dot(w.T, coefs.T) + b)
    print(predict)
