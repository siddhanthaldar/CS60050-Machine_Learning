'''
Roll No.       : 16EE30025
Name 	       : Siddhant Haldar
Assignment No. : 6
Instructions:
To run the code, type the following command in the terminal
	
	python 16EE30025_6.py 

'''

import math
import numpy as np 
import random

train_file = "data6.csv"
test_file = "test6.csv"
epoch = 10
lr = 0.01  # learning rate 

def read_train_data(filename):
	return np.genfromtxt(train_file, delimiter=',')


def read_test_data(filename):
	return np.genfromtxt(test_file, delimiter=',')

def sigmoid(x):
	return 1/(1+np.exp(-x))

def train_perceptron(train_att, label, epoch, lr):
	np.random.seed()
	w = np.random.randn(1, train_att.shape[1])       # weight matrix
	b = random.uniform(0,1.0)                        # bias
	for i in range(epoch):
		for j in range(train_att.shape[0]):
			y = sigmoid(np.sum(np.dot(train_att[j],w.T))+b)
			dw = lr * (y-label[j]) * train_att[j] * (y*(1-y))
			db = lr * (y-label[j]) * (y*(1-y))
			w += dw
			b += db

	return w,b		

def test_perceptron(test_data, w, b):
	y = np.dot(test_data,w.T) + b
	y = sigmoid(y)
	for i in range(len(y)):
		y[i] = 1 if y[i]>0.5 else 0
	return y

if __name__ == "__main__":
	train_data = read_train_data(train_file)

	# train attributes and labels
	train_att = []
	label = []

	for i in range(len(train_data)):
		train_att.append(train_data[i][:8])
		label.append(train_data[i][8])

	train_att = np.asarray(train_att)
	label = np.asarray(label)	

	w,b = train_perceptron(train_att,label, epoch, lr)

	#Test data
	test_data = read_test_data(test_file)

	output = test_perceptron(test_data, w, b)

	output_str = ""

	for i in range(len(test_data)):
		if int(output[i]):
			output_str += str(1) + " "
		else:
			output_str += str(0) + " "

	print(output_str)	

	#Write to output file
	f = open("16EE30025_6.out",'w')
	f.write(output_str)
	f.close()