import numpy as np
import scipy.sparse as sp
from scipy import linalg
from scipy.sparse import coo_matrix, hstack, identity, vstack
import math
# Load a text file of integers:
y = np.loadtxt("./hw1-data/upvote_labels.txt", dtype=np.int)
# Load a text file of strings:
featureNames = open("./hw1-data/upvote_features_100.txt").read().splitlines()
# Load a csv of floats:
A = sp.csc_matrix(np.genfromtxt("./hw1-data/upvote_data_100.csv", delimiter=","))
lambdaVar = 1

def findError(lambdaVar, index, size):
	bias = []
	for i in range(6000):
		bias.append([1])
	B = coo_matrix(bias)

	HAllBias = hstack([B,A]).todense()

	HTest = HAllBias[5000:]

	HAllBias = HAllBias[:5000]

	splicePoint = index * size
	HVal = HAllBias[splicePoint:splicePoint + size]

	TrainPA = HAllBias[0:splicePoint]
	TrainPB = HAllBias[splicePoint + size:]
	
	HTrain = TrainPA
	if splicePoint != 0 and splicePoint != 4000:
		HTrain = np.concatenate((TrainPA, TrainPB), axis =0)
	elif splicePoint == 0:
		# print "here"
		HTrain = TrainPB
	elif splicePoint == 4000:
		# print "here2"
		HTrain = TrainPA
	else:
		print "ererer"


	HTH = HTrain.transpose()*HTrain

	pStackTop = []
	for i in range(100):
		pStackTop.append(0)
	top = coo_matrix(pStackTop)

	pStackLeft = []
	for i in range(101):
		pStackLeft.append([0])
	left = coo_matrix(pStackLeft)

	
	ident = identity(100)
	identT = vstack([top, ident]).todense()
	identTL = hstack([left, identT]).todense()

	inverse = linalg.pinv(HTH + identTL)
	T = sp.csc_matrix.transpose(sp.csc_matrix(y[:4000]))

	W = inverse * lambdaVar * HTrain.transpose() * T
	HWt = (HTrain * W - T)
	HWtTrans = HWt.transpose()
	residError = HWtTrans * HWt
	RMSE = math.sqrt(residError/4000.0)
	print " RMSE",
	print RMSE,

lambdaVar = 1
for j in range(20):
	print "lambda",
	print lambdaVar,
	for i in range(5):
		findError(lambdaVar, i, 1000)
	lambdaVar = lambdaVar - (lambdaVar * 0.25)
	print ""
		

#1.9, 1.8