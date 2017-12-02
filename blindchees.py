import numpy as np
import scipy.io.wavfile
import python_speech_features as sf
import mfcc
import neuralnetwork

m = 5
k_tags = 3
m_test = 9
n_features = 1287
m_train = k_tags * m
tags = ["caballo", "torre", "alfil"]

X = np.zeros(m_train * n_features).reshape(m_train, n_features)

for i in range(m_train):
    #print(i)
    word = tags[i // m]

    filename = 'audios/' + word + str(i % m) + '.wav'
    rate, data = scipy.io.wavfile.read(filename)
    audio = data.T[0] if len(data.shape) == 2 else data

    #coefs = mfcc.getcoeficients(rate, audio)
    #X[i] = coefs / 200

    coefs = sf.mfcc(audio)
    coefs = coefs.reshape(-1)
    X[i] = coefs / 20


X = X.T

W = np.zeros(k_tags * n_features).reshape(k_tags, n_features)
B = np.zeros(k_tags).reshape((1, k_tags))
for i in range(k_tags):
    Y = np.concatenate((np.zeros(m * i), np.ones(m), np.zeros(m * (k_tags - i - 1))))
    w, b = neuralnetwork.model(X, Y, num_iterations = 50000, learning_rate = 0.2)
    W[i] = w.T
    B[0][i] = b

A = neuralnetwork.sigmoid(np.dot(W, X) + B.T)
#cost = - (Y * np.log(A) + (1 - Y) * np.log(1 - A)).sum() / kk

print(np.argmax(A, axis=0))
#print(cost)
print("\n\n")
for i in range(m_test):
    filename = 'audios/test' + str(i) + '.wav'
    rate, data = scipy.io.wavfile.read(filename)
    audio = data.T[0] if len(data.shape) == 2 else data

    #coefs = mfcc.getcoeficients(rate, audio)
    #coefs = coefs / 200

    coefs = sf.mfcc(audio)
    coefs = coefs.reshape(-1)
    coefs = coefs / 20

    predict = neuralnetwork.sigmoid(np.dot(W, coefs.T) + B)
    #print(np.argmax(predict))
    print(tags[np.argmax(predict)])
    #print("\n")
