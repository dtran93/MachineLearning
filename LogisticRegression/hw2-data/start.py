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
    featureLen = len(training_data[0]) - 1
    baisArray = [1] * lenData
    Weights = [0] * featureLen
    X_Matrix = matrix(X_train)
    Y_Matrix = matrix(Y_train)
    W_Matrix = transpose(matrix(Weights))
    W_T = matrix(Weights)
    X_T = transpose(X_Matrix)

    wo = 0.0
    eta = 0.1
    lamb = 0.3

    LogLoss = getLogLoss(lamb, W_Matrix, X_T, W_T, wo, lenData, Y_Matrix)
    #LogLoss = getLogLoss2(lamb, W_Matrix, X_T, W_T, wo, lenData)
    print LogLoss


    # 1000 times
    for t in range(1000):
	# the rest of w
    	YJMP = getYJMinusP(X_T, W_T, Y_Matrix, wo)
	#print (X_T * transpose(YJMP)) /100000.0
    	WUpdateXY = (X_T * transpose(YJMP)) / (lenData + 0.0)
    	W_Matrix = W_Matrix + eta * (lamb * abs(W_Matrix) - WUpdateXY)
	#print W_Matrix
   	# bias without something
    	# wo <= wo + func
    	wo = wo + eta * sum(YJMP) / (lenData + 0.0)
	W_T = transpose(W_Matrix)
	print getLogLoss(lamb, W_Matrix, X_T, W_T, wo, lenData, Y_Matrix)
	#print getLogLoss2(lamb, W_Matrix, X_T, W_T, wo, lenData)
    perceptron()

# from slides
def getLogLoss(lamb, W_Matrix, X_T, W_T, wo, lenData, Y_Matrix):
	return lamb * 0.5 * sum(abs(transpose(W_Matrix))) - 1.0 / lenData * getLW(Y_Matrix, W_T, X_T, wo, lenData)

# helper
def getLW(Y_Matrix, W_T, X_T, wo, lenData):
	return Y_Matrix * transpose(wo + W_T * X_T) - sum(log(1 + exp(wo + W_T * X_T)))
	
# def of log
def getLogLoss2(lamb, W_Matrix, X_T, W_T, wo, lenData):
	return lamb * .5 * sum(abs(transpose(W_Matrix))) - 1.0 / lenData * sum(log(getPYXWow(wo, W_T, X_T)))

# computes for all data points j P(Yj = 1 | X,Wo,W)
def getPYXWow(wo, W_T, X_T):
	AllWDotX = W_T * X_T
	tempSave = exp(wo + AllWDotX)
	return tempSave / (1 + tempSave)

# computes for all data points j, Yj - P(Yj = 1 | X,Wo,W)
# tested
def getYJMinusP(X_T, W_T, Y_Matrix, wo):
	AllWDotX = W_T * X_T
	tempSave = exp(wo + AllWDotX)
	return Y_Matrix - tempSave / (1 + tempSave)


###############################################################################################################
####################################################Perceptron#################################################
###############################################################################################################

def perceptron():
	return 0



if __name__ == '__main__':
    main()
