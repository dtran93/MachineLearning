import numpy as np
import scipy.sparse as sp
from scipy.sparse import coo_matrix, hstack, linalg
# Load a text file of integers:
y = np.loadtxt("./hw1-data/upvote_labels.txt", dtype=np.int)
# Load a text file of strings:
featureNames = open("./hw1-data/upvote_features_100.txt").read().splitlines()
# Load a csv of floats:
A = sp.csc_matrix(np.genfromtxt("./hw1-data/upvote_data_100.csv", delimiter=","))

bias = []
for i in range(6000):
	bias.append([1])
B = coo_matrix(bias)

# print hstack([B,B]).todense()
HFull = hstack([B,A]).todense()
deleteArr = range(5000,6000)
H = np.delete(HFull, deleteArr, 0)
HSparse = sp.csc_matrix(H)
HTrans = sp.csc_matrix.transpose(HSparse)
T = sp.csc_matrix.transpose(sp.csc_matrix(y[:5000]))
HTH = HTrans*(HSparse)
inverse = sp.linalg.inv(HTH)
temp = inverse*HTrans
W = temp*T

