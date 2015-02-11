#!/usr/bin/python
from __future__ import division
from numpy import *

def main():
    training_data = genfromtxt('train.txt', delimiter=',')
    Y_train = training_data[:,0]
    X_train = training_data[:, 1:]
    Y_test = genfromtxt('test_label.txt', delimiter=',')
    X_test = genfromtxt('test.txt', delimiter=',')
    lenData = len(Y_train)
    featureLen = len(training_data[0]) + 1
    baisArray = [1] * lenData
    Weights = [0] * featureLen
    X_Matrix = matrix(X_train)
    Y_Matrix = matrix(Y_train)
    W_Matrix = matrix(Weights)

    wo = 0
    eta = 0.1
    lamb = 0.3
    
    print len(Y_train)
    print len(X_train)

    # 1000 times
    for t in range(1000):
    	# bias without something
    	# wo <= wo + func
    	wo = wo - eta * (-1 / lenData * 1)# matrix stuff
    	X_T = tranpose(X_Matrix)
    	YJMP = getYJMinusP(X_T, W_Matrix)
    	WUpdateXY = (X_T * (Y_Matrix - YJMP)) / featureLen
    	# update each element in matrix??????
    	W_Matrix = W_Matrix - eta (lamb * W_Matrix - WUpdateXY)

def getYJMinusP(X_T, W_Matrix):
	AllWDotX = W_Matrix * X_T
	PYOne = []
	for (i in range(len(AllWDotX))):
		WXi = AllWDotX.item(i)
		PYOne.append(exp(w0 + WXi) / (1 + exp(w0 + WXi)))
	return PYOne

if __name__ == '__main__':
    main()
