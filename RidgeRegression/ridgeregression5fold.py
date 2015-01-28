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

def makeBias(value, length):
	bias = []
	for i in range(length):
		bias.append([value])
	B = coo_matrix(bias)
	return B

def makeIdent():
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
	return identTL

def findError(matrix, lambdaVar, index, size):
	# calculat slice point
	splicePoint = index * size

	# grab the HVal 1/5 set
	HVal = matrix[splicePoint:splicePoint + size]
	TrainPA = HAllBias[0:splicePoint]
	TrainPB = HAllBias[splicePoint + size:5000]

	# print TrainPA.shape
	# print TrainPB.shape

	HTrain = TrainPA
	if splicePoint != 0 and splicePoint != 4000:
		# print type(TrainPA)
		HTrain = np.concatenate((TrainPA, TrainPB), axis =0)
	elif splicePoint == 0:
		HTrain = TrainPB
	elif splicePoint == 4000:
		HTrain = TrainPA
	else:
		print "Error"

	identTL = makeIdent()
	# traspose T
	T = sp.csc_matrix.transpose(sp.csc_matrix(y))
	TPA = T[0:splicePoint]
	TPB = T[splicePoint + size:5000]

	# print TPA.shape
	# print TPB.shape

	TTrain = TPA
	if splicePoint != 0 and splicePoint != 4000:
		# print type(TPA)
		TTrain = vstack([TPA, TPB]).todense()
	elif splicePoint == 0:
		TTrain = TPB
	elif splicePoint == 4000:
		TTrain = TPA
	else:
		print "Error"

	TVal = T[splicePoint:splicePoint + size]
	HTH = HTrain.transpose() * HTrain
	Inverse = linalg.pinv(HTH + (lambdaVar * identTL))
	W = Inverse * HTrain.transpose() * TTrain

	HWT = (HVal * W - TVal)
	HWTTrans = HWT.transpose()
	ResError = HWTTrans * HWT
	RMSE = math.sqrt(ResError/1000.0)


	# print "Heldout",
	# print HVal.shape
	# print "HTrain",
	# print HTrain.shape
	# print "identTL",
	# print identTL.shape
	# print "TTrain",
	# print TTrain.shape
	# print "ResError",
	# print ResError
	# print RMSE

	return RMSE
	


	# HTH = HTrain.transpose()*HTrain
	# inverse = linalg.pinv(HTH + (lambdaVar * identTL))
	# W = inverse * lambdaVar * HTrain.transpose() * T
	# TNew = reshapeY[splicePoint:splicePoint + size]
	# HWt = (TNew - HVal * W)
	# HWtTrans = HWt.transpose()
	# residError = HWtTrans * HWt
	# RMSE = math.sqrt(residError/1000.0)
	# return RMSE

lambdaVar = 1.0
size = 1000
B = makeBias(1, 6000)
HAllBias = hstack([B,A]).todense()
for lambdaSweep in range(20):
	# print "lambda",
	# print lambdaVar,
	sumN = 0
	for crossValIndex in range(5):
		sumN = sumN + findError(HAllBias, lambdaVar, crossValIndex, size)
	lambdaVar = lambdaVar - (lambdaVar * 0.25)
	# print "sumN ",
	print sumN / 5.0
	

#1.9, 1.8