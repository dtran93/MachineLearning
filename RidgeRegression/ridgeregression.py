import numpy as np
import scipy.sparse as sp
from scipy import linalg
from scipy.sparse import coo_matrix, hstack
import math
# Load a text file of integers:
y = np.loadtxt("./hw1-data/upvote_labels.txt", dtype=np.int)
# Load a text file of strings:
featureNames = open("./hw1-data/upvote_features_100.txt").read().splitlines()
# Load a csv of floats:
A = sp.csc_matrix(np.genfromtxt("./hw1-data/upvote_data_100.csv", delimiter=","))

def RMSE(W):
	sum = W.sum()
	print sum

bias = []
for i in range(5000):
	bias.append([1])
B = coo_matrix(bias)

HPart = sp.csc_matrix(A[:5000])


HFull = hstack([B,HPart]).todense()
HTrans = HFull.transpose()
HTH = HTrans * HFull
inverse = linalg.pinv(HTH)
T = sp.csc_matrix.transpose(sp.csc_matrix(y[:5000]))
W = inverse * HTrans * T


HWt = (HFull * W - T)
HWtTrans = HWt.transpose()
residError = HWtTrans * HWt
RMSE = math.sqrt(residError/5000.0)
print RMSE

