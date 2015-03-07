#!/usr/bin/python
from __future__ import division
from numpy import *
from sklearn import tree
from random import randint
import matplotlib.pyplot as plt

X_train = []
Y_train = []
X_test = []
Y_test = []

def seprateAndConvert(line, X, Y):
	x = line[:len(line) - 2]
	y = line[len(line) - 2:].strip()

	# print x
	# print y

	if y == '-':
		Y.append(0)
	if y == '+':
		Y.append(1)

	newX = []

	for i in range(len(x)):
		if x[i] == 'a':
			newX.append(0)
		if x[i] == 't':
			newX.append(1)
		if x[i] == 'c':
			newX.append(2)
		if x[i] == 'g':
			newX.append(3)
	X.append(newX)

def makeData(X_train):
	newTrainDataX = []
	newTrainDataY = []
	for i in range(len(X_train)):
		rand = randint(0,len(X_train) - 1)
		newTrainDataX.append(X_train[rand])
		newTrainDataY.append(Y_train[rand])
	return newTrainDataX, newTrainDataY

def makeDataCountU(X_train):
	array = [0] * len(X_train)
	for i in range(len(X_train)):
		rand = randint(0,len(X_train) - 1)
		array[rand] = 1
	count = 0
	for i in range(len(X_train)):
		if array[i] == 0:
			count += 1
	return  1 - (count + 0.0) / len(X_train)



with open("training.txt", "r") as ins:
    for line in ins:
        seprateAndConvert(line, X_train, Y_train)

with open("test.txt", "r") as ins:
    for line in ins:
        seprateAndConvert(line, X_test, Y_test)

# print matrix(X_test)
# print transpose(matrix(Y_test))


# 2.2.1
# xarr = [0.0] * 100
# for i in range(10):
# 	clfTrees = []
# 	for i in range(100):
# 		newTrainDataX, newTrainDataY = makeData(X_train)
# 		clf = tree.DecisionTreeClassifier(max_depth = 1)
# 		clfFitted = clf.fit(newTrainDataX, newTrainDataY)
# 		clfTrees.append(clfFitted)
# 		count = 0
# 		for j in range(len(X_test)):
# 			oneCount = 0
# 			zeroCount = 0
# 			# vote
# 			for k in range(len(clfTrees)):
# 				if clfTrees[k].predict(X_test[j]) == 0:
# 					zeroCount += 1
# 				else:
# 					oneCount += 1
# 			if oneCount > zeroCount:
# 				if 1 == Y_test[j]:
# 					count += 1
# 			else:
# 				if 0 == Y_test[j]:
# 					count += 1
# 		# print i,
# 		# print " Correct: ",
# 		xarr[i] = xarr[i] + (len(X_test) - count) / (0.0 + len(X_test))
# 		# xarr.append((len(X_test) - count) / (0.0 + len(X_test)))
# for i in range(len(xarr)):
# 	xarr[i] = xarr[i] / 10
# plt.plot(range(1,101), xarr, linewidth=2.0)
# plt.show()

# 2.2.2
# xarr = [0.0] * 100
# for i in range(10):
# 	clfTrees = []
# 	for i in range(100):
# 		newTrainDataX, newTrainDataY = makeData(X_train)
# 		clf = tree.DecisionTreeClassifier(max_depth = 2)
# 		clfFitted = clf.fit(newTrainDataX, newTrainDataY)
# 		clfTrees.append(clfFitted)
# 		count = 0
# 		for j in range(len(X_test)):
# 			oneCount = 0
# 			zeroCount = 0
# 			# vote
# 			for k in range(len(clfTrees)):
# 				if clfTrees[k].predict(X_test[j]) == 0:
# 					zeroCount += 1
# 				else:
# 					oneCount += 1
# 			if oneCount > zeroCount:
# 				if 1 == Y_test[j]:
# 					count += 1
# 			else:
# 				if 0 == Y_test[j]:
# 					count += 1
# 		# print i,
# 		# print " Correct: ",
# 		xarr[i] = xarr[i] + (len(X_test) - count) / (0.0 + len(X_test))
# 		# xarr.append((len(X_test) - count) / (0.0 + len(X_test)))
# for i in range(len(xarr)):
# 	xarr[i] = xarr[i] / 10
# plt.plot(range(1,101), xarr, linewidth=2.0)
# plt.show()

# 2.2.3
# clf = tree.DecisionTreeClassifier(max_depth = 2)
# clfTrees = []
# uniquePer = 0.0
# for i in range(100):
# 	uniquePer += makeDataCountU(X_train)
# print uniquePer / 100

# 2.3.1

# 0 => -1

# DWeights = [1.0 / len(X_train)] * len(X_train)
# hValues = []
# alphas = []
# xarr = []
# for loopIndex in range(100):
# 	clf = tree.DecisionTreeClassifier(max_depth = 2)
# 	clfFitted = clf.fit(X_train, Y_train, sample_weight = DWeights)
# 	hValues.append(clfFitted)
# 	eta = 0.0
# 	for i in range(len(Y_train)):
# 		if clfFitted.predict(X_train[i]) != Y_train[i]:
# 			eta += DWeights[i]
# 	alpha = 0.5 * log((1 - eta) / eta)
# 	alphas.append(alpha)
# 	# update weights
# 	for i in range(len(DWeights)):
# 		yT = Y_train[i]
# 		if Y_train[i] == 0:
# 			yT = -1
# 		hV = clfFitted.predict(X_train[i])[0]
# 		if hV == 0:
# 			hV = -1
# 		DWeights[i] = DWeights[i] * exp(-1 * alpha * yT * hV)
# 	sumW = sum(DWeights)
# 	for i in range(len(DWeights)):
# 		temp = DWeights[i]
# 		DWeights[i] = temp / (sumW + 0.0)

# 	correct = 0
# 	for outter in range(len(X_test)):
# 		valueH = 0.0
# 		for i in range(len(hValues)):
# 			hVP = hValues[i].predict(X_test[outter])[0]
# 			if hVP == 0:
# 				hVP = -1
# 			valueH += hVP * alphas[i]
# 		if valueH >= 0.0:
# 			if 1 == Y_test[outter]:
# 				correct += 1
# 		else:
# 			if 0 == Y_test[outter]:
# 				correct += 1
# 	# print (len(X_test) - correct) / (0.0 + len(X_test))
# 	# break
# 	xarr.append((len(X_test) - correct) / (0.0 + len(X_test)))
# plt.plot(range(1,101), xarr, linewidth=2.0)
# plt.show()


# 2.3.3

# 0 => -1

# DWeights = [1.0 / len(X_train)] * len(X_train)
# hValues = []
# alphas = []
# xarr = []
# for loopIndex in range(300):
# 	clf = tree.DecisionTreeClassifier(max_depth = 2)
# 	clfFitted = clf.fit(X_train, Y_train, sample_weight = DWeights)
# 	hValues.append(clfFitted)
# 	eta = 0.0
# 	for i in range(len(Y_train)):
# 		if clfFitted.predict(X_train[i]) != Y_train[i]:
# 			eta += DWeights[i]
# 	alpha = 0.5 * log((1 - eta) / eta)
# 	alphas.append(alpha)
# 	# update weights
# 	for i in range(len(DWeights)):
# 		yT = Y_train[i]
# 		if Y_train[i] == 0:
# 			yT = -1
# 		hV = clfFitted.predict(X_train[i])[0]
# 		if hV == 0:
# 			hV = -1
# 		DWeights[i] = DWeights[i] * exp(-1 * alpha * yT * hV)
# 	sumW = sum(DWeights)
# 	for i in range(len(DWeights)):
# 		temp = DWeights[i]
# 		DWeights[i] = temp / (sumW + 0.0)

# 	correct = 0
# 	for outter in range(len(X_test)):
# 		valueH = 0.0
# 		for i in range(len(hValues)):
# 			hVP = hValues[i].predict(X_test[outter])[0]
# 			if hVP == 0:
# 				hVP = -1
# 			valueH += hVP * alphas[i]
# 		if valueH >= 0.0:
# 			if 1 == Y_test[outter]:
# 				correct += 1
# 		else:
# 			if 0 == Y_test[outter]:
# 				correct += 1
# 	# print (len(X_test) - correct) / (0.0 + len(X_test))
# 	# break
# 	xarr.append((len(X_test) - correct) / (0.0 + len(X_test)))
# 	print i
# plt.plot(range(1,501), xarr, linewidth=2.0)
# plt.show()

DWeights = [1.0 / len(X_train)] * len(X_train)
hValues = []
alphas = []
xarr = []
for loopIndex in range(300):
	clf = tree.DecisionTreeClassifier(max_depth = 2)
	clfFitted = clf.fit(X_train, Y_train, sample_weight = DWeights)
	hValues.append(clfFitted)
	eta = 0.0
	for i in range(len(Y_train)):
		if clfFitted.predict(X_train[i]) != Y_train[i]:
			eta += DWeights[i]
	alpha = 0.5 * log((1 - eta) / eta)
	alphas.append(alpha)
	# update weights
	for i in range(len(DWeights)):
		yT = Y_train[i]
		if Y_train[i] == 0:
			yT = -1
		hV = clfFitted.predict(X_train[i])[0]
		if hV == 0:
			hV = -1
		DWeights[i] = DWeights[i] * exp(-1 * alpha * yT * hV)
	sumW = sum(DWeights)
	for i in range(len(DWeights)):
		temp = DWeights[i]
		DWeights[i] = temp / (sumW + 0.0)

	correct = 0
	for outter in range(len(X_test)):
		valueH = 0.0
		for i in range(len(hValues)):
			hVP = hValues[i].predict(X_test[outter])[0]
			if hVP == 0:
				hVP = -1
			valueH += hVP * alphas[i]
		if valueH >= 0.0:
			if 1 == Y_test[outter]:
				correct += 1
		else:
			if 0 == Y_test[outter]:
				correct += 1
	# print (len(X_test) - correct) / (0.0 + len(X_test))
	# break
	xarr.append((len(X_test) - correct) / (0.0 + len(X_test)))
	print i
plt.plot(range(1,301), xarr, linewidth=2.0)
plt.show()
