import numpy as np
import scipy.sparse as sp
# Load a text file of integers:
y = np.loadtxt("./hw1-data/upvote_labels.txt", dtype=np.int)
# Load a text file of strings:
featureNames = open("./hw1-data/upvote_features_100.txt").read().splitlines()
# Load a csv of floats:
A = sp.csc_matrix(np.genfromtxt("./hw1-data/upvote_data_100.csv", delimiter=","))

