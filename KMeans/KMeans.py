#!/usr/bin/python
from numpy import *
X = genfromtxt('digit.txt')
Y = genfromtxt('labels.txt', dtype=int)

# print X
# print Y

number_k = 2;

# pick points for KMeans
for i in range(number_k):
	print X[i]