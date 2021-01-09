#import packages

import numpy as np
import pickle

#Activation Functions and Derivatives

def softmax(z):
    return np.exp(z)/np.sum(np.exp(z), axis=0, keepdims=True)

def relu(z):
    return np.where(z > 0, z, 0.001*z)

def relu_(z):
    return np.where(z > 0, 1, 0.001)

#forward propagation
def forward_propagation(parameter, L):
    for l in range(1, L):
        parameter["a"+str(l)] = relu(np.dot(parameter["w"+str(l)], parameter["a"+str(l-1)]) + parameter["b"+str(l)])

    parameter["a"+str(L)] = softmax(np.dot(parameter["w"+str(L)], parameter["a"+str(L-1)]) + parameter["b"+str(L)])

    return parameter

#Loading Model

L = pickle.load(open('/API/length.p', 'rb'))
weight = pickle.load(open('/API/weight.p', 'rb'))
bias = pickle.load(open('/API/bias.p', 'rb'))
parameter = {}

for l in range(L):
    parameter["w"+str(l+1)] = weight[l]
    parameter["b"+str(l+1)] = bias[l]

#Prediction function

def predict(x):
    global parameter
    parameter["a0"] = x
    parameter = forward_propagation(parameter,L)
    max_ = 0
    for i in range(10):
        max_ = max_ if parameter["a"+str(L)][max_][0] > parameter["a"+str(L)][i][0] else i
    
    return max_