#!/usr/bin/env python
import math

yValueIndex = 2
alpha = -1.0 / 30
beta = 1.0 / 20000 
data = [(24, 40000, "Yes"),
(53, 52000, "No"),
(23, 25000, "No"),
(25, 77000, "Yes"),
(32, 48000, "Yes"),
(52, 110000, "Yes"),
(22, 38000, "Yes"),
(43, 44000, "No"),
(52, 27000, "No"),
(48, 65000, "Yes")]

def getEntropy(data):
	countYes = 0
	for i in range(len(data)):
		if data[i][yValueIndex] == "Yes":
			countYes += 1
	pYes = countYes / (len(data) + 0.0)
	pNo = 1 - pYes
	if pYes == 0:
		pYes = 1
	if pNo == 0:
		pNo = 1
	return -1 * (pYes * math.log(pYes) / math.log(2) + pNo * math.log(pNo) / math.log(2))

def getConditionalEntropy(data, ageThresh, incomeThresh):
	# pick higher win ties
	higherYes = 0
	lowerYes = 0
	totalhigher = 0
	totalLower = 0
	global alpha
	global beta
	for i in range(len(data)):
		if alpha * data[i][0] + beta * data[i][1] - 1 < alpha * ageThresh + beta * incomeThresh - 1:
			# print "here"
			totalLower += 1
			if data[i][yValueIndex] == "Yes":
				lowerYes += 1
		else:
			# print "there"
			totalhigher += 1
			if data[i][yValueIndex] == "Yes":
				higherYes += 1

	if totalhigher + totalLower == 0:
		return 0
	pHigher = totalhigher / (0.0 + totalhigher + totalLower)
	pLower = 1 - pHigher
	pHigherYes = 0
	pHigherNo = 0
	if totalhigher != 0:
		pHigherYes = higherYes / (totalhigher + 0.0)
		pHigherNo = 1 - pHigherYes
	
	pLowerYes = 0
	pLowerNo = 0
	if totalLower != 0:
		pLowerYes = lowerYes / (totalLower + 0.0)
		pLowerNo = 1 - pLowerYes

	if pHigherYes == 0:
		pHigherYes = 1
	if pHigherNo == 0:
		pHigherNo = 1
	if pLowerYes == 0:
		pLowerYes = 1
	if pLowerNo == 0:
		pLowerNo = 1
	return -1 * (pHigher * (pHigherYes * math.log(pHigherYes) / math.log(2) + pHigherNo * math.log(pHigherNo) / math.log(2)) 
				+ pLower * (pLowerYes * math.log(pLowerYes) / math.log(2) + pLowerNo * math.log(pLowerNo) / math.log(2)))

def findIG(data, ageThresh, incomeThresh):
	print getEntropy(data) - getConditionalEntropy(data, ageThresh, incomeThresh)
	return getEntropy(data) - getConditionalEntropy(data, ageThresh, incomeThresh)

def findThreshHoldWithLargestIG(data):
	bestAgeThresh = -1
	bestIncomeThresh = -1
	bestIG = -1
	for i in range(len(data)):
		for j in range(len(data)):
			ageThresh = data[i][0]
			incomeThresh = data[j][1]
			theIG = findIG(data, ageThresh, incomeThresh)
			if theIG > bestIG:
				bestIG = theIG
				bestAgeThresh = ageThresh
				bestIncomeThresh = incomeThresh
	return bestAgeThresh, bestIncomeThresh, bestIG

def filterDataBasedOnSplit(data, bestAgeThresh, bestIncomeThresh):
	global alpha
	global beta
	dataNewHigher = []
	dataNewLower = []
	for i in range(len(data)):
		if alpha * data[i][0] + beta * data[i][1] - 1 < alpha * bestAgeThresh + beta * bestIncomeThresh - 1:
			dataNewLower.append(data[i])
		else:
			dataNewHigher.append(data[i])
	return dataNewHigher, dataNewLower

bestAgeThresh, bestIncomeThresh, bestIG =  findThreshHoldWithLargestIG(data)
print "threshold age:",
print bestAgeThresh,
print " income: ",
print bestIncomeThresh
print "IG",
print bestIG
higherData, lowerData =  filterDataBasedOnSplit(data, bestAgeThresh, bestIncomeThresh)
print higherData
print lowerData
print 