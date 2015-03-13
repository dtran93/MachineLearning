#!/usr/bin/python
from numpy import *
from copy import deepcopy
X = genfromtxt('digit.txt')
Y = genfromtxt('labels.txt', dtype=int)

# print X
# print Y

number_k = 2;
PointsMeanK = []

def findDist(p1, p2):
	sum = 0
	for i in range(len(p1)):
		sum += (p1[i] - p2[i]) * (p1[i] - p2[i])
	return math.sqrt(sum)

def findMean(PointArray):
	arrayOfZero = [0] * len(PointArray[0])
	for i in range(len(PointArray)):
		for j in range(len(PointArray[0])):
			arrayOfZero[j] += PointArray[i][j]
	return arrayOfZero

# pick points for KMeans
for i in range(number_k):
	PointsMeanK.append(X[i])

for zz in range(20):
	PointsMeanChildren = []
	for i in range(number_k):
		PointsMeanChildren.append([])
	# print PointsMeanChildren

	for i in range(len(X)):
		minDist = float("inf")
		minIndex = 0
		for j in range(number_k):
			dist = findDist(X[i], PointsMeanK[j]);
			if dist < minDist:
				minDist = dist
				minIndex = j
		# print minDist
		# print minIndex
		PointsMeanChildren[minIndex].append(deepcopy(X[i]));

	print PointsMeanK
	for i in range(len(PointsMeanChildren)):
		PointsMeanK[i] = findMean(PointsMeanChildren[i])

print PointsMeanK
# print findDist(PointsMeanK[0], PointsMeanK[1])