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

def findError(HAllBias, lambdaVar):
	T = sp.csc_matrix.transpose(sp.csc_matrix(y))
	TVal = T[5000:6000]
	HVal = HAllBias[5000:6000]
	T = sp.csc_matrix.transpose(sp.csc_matrix(y))
	identTL = makeIdent()
	HTrain = HAllBias[0:5000]
	TTrain = T[0:5000]

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

lambdaVar = 0.042235
B = makeBias(1, 6000)
HAllBias = hstack([B,A]).todense()
print findError(HAllBias, lambdaVar)

	

#1.9, 1.8