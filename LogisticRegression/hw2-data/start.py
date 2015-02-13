#!/usr/bin/python
from __future__ import division
from numpy import *
import matplotlib.pyplot as plt

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
    X_Test = matrix(X_test)
    Y_Test = matrix(Y_test)
    W_Matrix = transpose(matrix(Weights))
    W_T = matrix(Weights)
    X_T = transpose(X_Matrix)

    wo = 0.0
    eta = 0.1
    lamb = 0.3
    plotArray = []

    # 2.4.2
    # 1000 times
    for t in range(1000):
	# W not wo
    	YJMP = getYJMinusP(X_T, W_T, Y_Matrix, wo)
    	WUpdateXY = (X_T * transpose(YJMP)) / (lenData + 0.0)
    	W_Matrix = W_Matrix - eta * (lamb * W_Matrix - WUpdateXY)
   	# bias without something
    	# wo <= wo + func
    	wo = wo + eta * sum(YJMP) / (lenData + 0.0)
	W_T = transpose(W_Matrix)
	print t,
	print " \t",
	logloss = getLogLoss(lamb, W_Matrix, X_T, W_T, wo, lenData, Y_Matrix).item(0)
	print logloss
	plotArray.append(logloss)
    x = range(1000)
    plt.plot(x, plotArray, linewidth=2.0)
    plt.show()
    learnedWeights = W_Matrix
    CTR = getCTRCorrects(transpose(X_Test), transpose(learnedWeights), Y_test, wo)
    print "CTR correct guess: ",
    print CTR
    print learnedWeights

    # 2.4.3
    episilon = 0.0005
    plotArray = []
    lastLL = None
    Weights = [0] * featureLen
    wo = 0.0
    W_Matrix = transpose(matrix(Weights))
    W_T = matrix(Weights)
    for t in range(1000):
	# W not wo
    	YJMP = getYJMinusP(X_T, W_T, Y_Matrix, wo)
    	WUpdateXY = (X_T * transpose(YJMP)) / (lenData + 0.0)
    	W_Matrix = W_Matrix - eta * (lamb * W_Matrix - WUpdateXY)
   	# bias without something
    	# wo <= wo + func
    	wo = wo + eta * sum(YJMP) / (lenData + 0.0)
	W_T = transpose(W_Matrix)
	print t,
	print " \t",
	logloss = getLogLoss(lamb, W_Matrix, X_T, W_T, wo, lenData, Y_Matrix).item(0)
	print logloss
	if lastLL == None:
		lastLL = logloss
	elif abs(lastLL - logloss) < episilon:
		break
	lastLL = logloss	
	plotArray.append(logloss)
    x = range(len(plotArray))
    plt.plot(x, plotArray, linewidth=2.0)
    plt.show()
    learnedWeights = W_Matrix
    CTR = getCTRCorrects(transpose(X_Test), transpose(learnedWeights), Y_test, wo)
    print "CTR correct guess: ",
    print CTR
    print learnedWeights

    # 2.4.4
    lamb = 0
    episilon = 0.0000
    plotArray = []
    lastLL = None
    Weights = [0] * featureLen
    wo = 0.0
    W_Matrix = transpose(matrix(Weights))
    W_T = matrix(Weights)
    for t in range(1000):
	# W not wo
    	YJMP = getYJMinusP(X_T, W_T, Y_Matrix, wo)
    	WUpdateXY = (X_T * transpose(YJMP)) / (lenData + 0.0)
    	W_Matrix = W_Matrix - eta * (lamb * W_Matrix - WUpdateXY)
   	# bias without something
    	# wo <= wo + func
    	wo = wo + eta * sum(YJMP) / (lenData + 0.0)
	W_T = transpose(W_Matrix)
	#print t,
	#print " \t",
	logloss = getLogLoss(lamb, W_Matrix, X_T, W_T, wo, lenData, Y_Matrix).item(0)
	#print logloss
	if lastLL == None:
		lastLL = logloss
	elif abs(lastLL - logloss) < episilon:
		break
	lastLL = logloss	
	plotArray.append(logloss)
    learnedWeights = W_Matrix
    print "LLNorm: ",
    print getLLNorm(learnedWeights)
    
    lamb = 0.3
    episilon = 0.0000
    plotArray = []
    lastLL = None
    Weights = [0] * featureLen
    wo = 0.0
    W_Matrix = transpose(matrix(Weights))
    W_T = matrix(Weights)
    for t in range(1000):
	# W not wo
    	YJMP = getYJMinusP(X_T, W_T, Y_Matrix, wo)
    	WUpdateXY = (X_T * transpose(YJMP)) / (lenData + 0.0)
    	W_Matrix = W_Matrix - eta * (lamb * W_Matrix - WUpdateXY)
   	# bias without something
    	# wo <= wo + func
    	wo = wo + eta * sum(YJMP) / (lenData + 0.0)
	W_T = transpose(W_Matrix)
	#print t,
	#print " \t",
	logloss = getLogLoss(lamb, W_Matrix, X_T, W_T, wo, lenData, Y_Matrix).item(0)
	#print logloss
	if lastLL == None:
		lastLL = logloss
	elif abs(lastLL - logloss) < episilon:
		break
	lastLL = logloss	
	plotArray.append(logloss)
    learnedWeights = W_Matrix
    print "LLNorm: ",
    print getLLNorm(learnedWeights)

    #2.5.1
    for t in range(5000):
	# W not wo
    	YJMP = getYJMinusP(X_T, W_T, Y_Matrix, wo)
    	WUpdateXY = (X_T * transpose(YJMP)) / (lenData + 0.0)
    	W_Matrix = W_Matrix - eta * (lamb * W_Matrix - WUpdateXY)
   	# bias without something
    	# wo <= wo + func
    	wo = wo + eta * sum(YJMP) / (lenData + 0.0)
	W_T = transpose(W_Matrix)
	#print t,
	#print " \t",
	logloss = getLogLoss(lamb, W_Matrix, X_T, W_T, wo, lenData, Y_Matrix).item(0)
	#print logloss
	plotArray.append(logloss)
    learnedWeights = W_Matrix
    answers = recallPrecision(transpose(X_Test), transpose(learnedWeights), Y_test, wo)
    print "Recall1: ",
    print answers[0]
    print "Precision1: ", 
    print answers[1]
    print "Recall0: ",
    print answers[2]
    print "Precision0: ", 
    print answers[3]

    #2.5.2

    training_data = genfromtxt('oversampled_train.txt', delimiter=',')
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
    X_Test = matrix(X_test)
    Y_Test = matrix(Y_test)
    W_Matrix = transpose(matrix(Weights))
    W_T = matrix(Weights)
    X_T = transpose(X_Matrix)


    for t in range(5000):
	# W not wo
    	YJMP = getYJMinusP(X_T, W_T, Y_Matrix, wo)
    	WUpdateXY = (X_T * transpose(YJMP)) / (lenData + 0.0)
    	W_Matrix = W_Matrix - eta * (lamb * W_Matrix - WUpdateXY)
   	# bias without something
    	# wo <= wo + func
    	wo = wo + eta * sum(YJMP) / (lenData + 0.0)
	W_T = transpose(W_Matrix)
	#print t,
	#print " \t",
	logloss = getLogLoss(lamb, W_Matrix, X_T, W_T, wo, lenData, Y_Matrix).item(0)
	#print logloss
	plotArray.append(logloss)
    learnedWeights = W_Matrix
    answers = recallPrecision(transpose(X_Test), transpose(learnedWeights), Y_test, wo)
    print "Recall1: ",
    print answers[0]
    print "Precision1: ", 
    print answers[1]
    print "Recall0: ",
    print answers[2]
    print "Precision0: ", 
    print answers[3]

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
