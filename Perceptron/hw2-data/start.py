#!/usr/bin/python
from __future__ import division
from numpy import *
import matplotlib.pyplot as plt

def main():
    wo = 0.0
    eta = 0.1
    lamb = 0.3
    plotArray = []

    training_data = genfromtxt('oversampled_train.txt', delimiter=',')
    Y_train = training_data[:,0]
    X_train = training_data[:, 1:]
    Y_test = genfromtxt('test_label.txt', delimiter=',')
    X_test = genfromtxt('test.txt', delimiter=',')

    lenData = len(Y_train)
    featureLen = len(training_data[0]) - 1
    baisArray = [1] * lenData
    Weights = [0] * featureLen
    W_Matrix = matrix(Weights) 
    X_Matrix_Trans = transpose(matrix(X_train))

    YiNeg = [-1] * featureLen
    YiPos = [1] * featureLen
    
    for t in range(5000):
        countCorrect = 0
	for i in range(lenData):
		Y = sign(W_Matrix, X_train[i], wo)
		if Y != Y_train[i]:
			if Y_train[i] == 1:
				W_Matrix = W_Matrix + YiXi(YiPos, X_train[i])
				wo = wo + Y_train[i]
			else:
				W_Matrix = W_Matrix + YiXi(YiNeg, X_train[i])			
				wo = wo + (-1)
		else:
			countCorrect += 1
	print "t: ",
	print t,
	print "correct: ",
	print countCorrect


def sign(W_T, X_T, wo):
	X_Matrix = transpose(matrix(X_T))
	if (W_T * X_Matrix).item(0) + wo > 0:
		return 1
	else:
		return 0

# returns Xi * constant Yi
def YiXi(Yi, Xi):
	return dot(Yi, Xi)

# from slides
def getLogLoss(lamb, W_Matrix, X_T, W_T, wo, lenData, Y_Matrix):
	return lamb * 0.5 * transpose(W_Matrix)* W_Matrix - 1.0 / lenData * getLW(Y_Matrix, W_T, X_T, wo, lenData)

# helper
def getLW(Y_Matrix, W_T, X_T, wo, lenData):
	return Y_Matrix * transpose(wo + W_T * X_T) - sum(log(1 + exp(wo + W_T * X_T)))

# computes for all data points j, Yj - P(Yj = 1 | X,Wo,W)
# tested
def getYJMinusP(X_T, W_T, Y_Matrix, wo):
	AllWDotX = W_T * X_T
	tempSave = exp(wo + AllWDotX)
	return Y_Matrix - tempSave / (1 + tempSave)
	
def getCTRCorrects(X_T, W_T, Y_test, wo):
	AllWDotX = W_T * X_T
	tempSave = exp(wo + AllWDotX)
	probs = tempSave / (1 + tempSave)
	count = 0.0
	for i in range(len(Y_test)):
		if round(probs.item(i)) == Y_test[i]:
			count += 1
	return count / len(Y_test)

def recallPrecision(X_T, W_T, Y_test, wo):
	AllWDotX = W_T * X_T
	tempSave = exp(wo + AllWDotX)
	probs = tempSave / (1 + tempSave)
	countCorrect1 = 0.0
        countY1 = 0.0
	countYIdent1 = 0.0
	countCorrect0 = 0.0
        countY0 = 0.0
	countYIdent0 = 0.0
	for i in range(len(Y_test)):
		if Y_test[i] == 1:
			countY1 += 1
		if round(probs.item(i)) == Y_test[i] and Y_test[i] == 1.0:
			countCorrect1 += 1
		if round(probs.item(i)) == 1:
			countYIdent1 += 1
		if Y_test[i] == 0:
			countY0 += 1
		if round(probs.item(i)) == Y_test[i] and Y_test[i] == 0.0:
			countCorrect0 += 1
		if round(probs.item(i)) == 0:
			countYIdent0 += 1
	answer = [0,0,0,0]
	if countY1 == 0:
		answer[0] = 0
	else:
		answer[0] = countCorrect1 / countY1
	if countYIdent1 == 0:
		answer[1] = 0
	else:
		answer[1] = countCorrect1 / countYIdent1
	if countY0 == 0:
		answer[2] = 0
	else:
		answer[2] = countCorrect0 / countY0
	if countYIdent0 == 0:
		answer[3] = 0
	else:
		answer[3] = countCorrect0 / countYIdent0
	return answer

def getLLNorm(W_Matrix):
	return transpose(W_Matrix) * W_Matrix



if __name__ == '__main__':
    main()
