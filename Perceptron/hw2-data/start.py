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
	
    Wo250 = 0.0
    W250 = W_Matrix
    Wo500 = 0.0
    W500 = W_Matrix
    Wo100 = 0.0
    W1000 = W_Matrix
    # t = 250, 500, 1000
    for t in range(1000):
        countCorrect = 0
	for i in range(lenData - 1000):
		Y = sign(W_Matrix, X_train[i], wo)
		if Y != Y_train[i]:
			if Y_train[i] == 1:
				W_Matrix = W_Matrix + matrix(X_train[i])
				wo = wo + Y_train[i]
			else:
				W_Matrix = W_Matrix + (-1 * matrix(X_train[i]))			
				wo = wo + (-1)
		else:
			countCorrect += 1
	print t,
	print "\t",
        print countCorrect
        if t == 249:
		Wo250 = wo
		W250 = W_Matrix
        if t == 499:
		Wo500 = wo
		W500 = W_Matrix
        if t == 999:
		Wo1000 = wo
		W1000 = W_Matrix
    print W250
    print W500
    print W1000
    # validate with W250
    countCorrect = 0.0
    for i in range(lenData - 1000, lenData):
	Y = sign(W250, X_train[i], Wo250)
	if Y == Y_train[i]:
		countCorrect += 1
    print countCorrect
    # validate with W500
    countCorrect = 0.0
    for i in range(lenData - 1000, lenData):
	Y = sign(W500, X_train[i], Wo500)
	if Y == Y_train[i]:
		countCorrect += 1
    print countCorrect
    # validate with W1000
    countCorrect = 0.0
    for i in range(lenData - 1000, lenData):
	Y = sign(W1000, X_train[i], Wo1000)
	if Y == Y_train[i]:
		countCorrect += 1  
    print countCorrect
    
    print "LLNorm 250: ",
    print getLLNorm(W250)
    print "LLNorm 500: ",
    print getLLNorm(W500)
    print "LLNorm 1000: ",
    print getLLNorm(W1000)

    # LLNorm 500 wins
    # test set with t = 500
    W_Matrix = matrix(Weights)
    wo = 0
    for t in range(500):
        countCorrect = 0
	for i in range(len(Y_test)):
		Y = sign(W_Matrix, X_test[i], wo)
		if Y != Y_test[i]:
			if Y_test[i] == 1:
				W_Matrix = W_Matrix + matrix(X_test[i])
				wo = wo + Y_train[i]
			else:
				W_Matrix = W_Matrix + (-1 * matrix(X_test[i]))			
				wo = wo + (-1)
		else:
			countCorrect += 1
	print t,
	print "\t",
        print countCorrect
    print W_Matrix
    answers = recallPrec(X_test, W_Matrix, wo, Y_test)
    print "Recall1: ",
    print answers[0]
    print "Precision1: ", 
    print answers[1]
    print "Recall0: ",
    print answers[2]
    print "Precision0: ", 
    print answers[3]

def recallPrec(X_test, W_Matrix, wo, Y_test): 
	countCorrect1 = 0.0
	countY1 = 0.0
	countYIdent1 = 0.0
	countCorrect0 = 0.0
	countY0 = 0.0
	countYIdent0 = 0.0   
    	for i in range(len(Y_test)):
		Y = sign(W_Matrix, X_test[i], wo)
		if Y_test[i] == 1:
			countY1 += 1
		if Y == Y_test[i] and Y_test[i] == 1.0:
			countCorrect1 += 1
		if Y == 1:
			countYIdent1 += 1
		if Y_test[i] == 0:
			countY0 += 1
		if Y == Y_test[i] and Y_test[i] == 0.0:
			countCorrect0 += 1
		if Y == 0:
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
		

def sign(W_T, X_T, wo):
	X_Matrix = transpose(matrix(X_T))
	if (W_T * X_Matrix).item(0) + wo > 0:
		return 1
	else:
		return 0

def getLLNorm(W_Matrix):
	return W_Matrix * transpose(W_Matrix)



if __name__ == '__main__':
    main()
