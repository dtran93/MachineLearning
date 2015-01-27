#!/usr/bin/env python
import math

yValueIndex = 2
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

def getConditionalEntropy(data, threshold, attribute):
	# pick higher win ties
	higherYes = 0
	lowerYes = 0
	totalhigher = 0
	totalLower = 0
	for i in range(len(data)):
		if data[i][attribute] < threshold:
			totalLower += 1
			if data[i][yValueIndex] == "Yes":
				lowerYes += 1
		else:
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

def findIG(data, threshold, attribute):
	return getEntropy(data) - getConditionalEntropy(data, threshold, attribute)

def findThreshHoldWithLargestIG(data, attribute):
	thresholdBest = -1
	indexThreshold = -1
	bestIG = -1
	for i in range(len(data)):
		threshold = data[i][attribute]
		theIG = findIG(data, threshold, attribute)
		if theIG > bestIG:
			bestIG = theIG
			thresholdBest = threshold
			indexThreshold = i
	return indexThreshold, thresholdBest, bestIG

def filterDataBasedOnSplit(data, threshold, attribute):
	dataNewHigher = []
	dataNewLower = []
	for i in range(len(data)):
		if data[i][attribute] < threshold:
			dataNewLower.append(data[i])
		else:
			dataNewHigher.append(data[i])
	return dataNewHigher, dataNewLower

indexThreshold, thresholdBest, bestIG =  findThreshHoldWithLargestIG(data, 1)
print "threshold",
print thresholdBest	
print "IG",
print bestIG
higherData, lowerData =  filterDataBasedOnSplit(data, thresholdBest, 1)
print higherData
print lowerData
print 

indexThreshold, thresholdBest, bestIG =  findThreshHoldWithLargestIG(higherData, 0)
print "threshold",
print thresholdBest	
print "IG",
print bestIG
higherData, lowerData =  filterDataBasedOnSplit(higherData, thresholdBest, 0)
print higherData
print lowerData
print 

indexThreshold, thresholdBest, bestIG =  findThreshHoldWithLargestIG(higherData, 1)
print "threshold",
print thresholdBest	
print "IG",
print bestIG
higherData, lowerData =  filterDataBasedOnSplit(higherData, thresholdBest, 1)
print higherData
print lowerData